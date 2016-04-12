# -*- coding: utf-8 -*-

import re
from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time
from time import sleep
import logging

import django
from django.conf import urls
from django.core import urlresolvers

from . import utils as maintenance
from .conf import settings

urls.handler503 = 'maintenancemode.views.temporary_unavailable'
urls.__all__.append('handler503')

IGNORE_URLS = tuple([re.compile(u) for u in settings.MAINTENANCE_IGNORE_URLS])

MAX_WAIT_FOR_END = settings.MAINTENANCE_MAX_WAIT_FOR_END

logger = logging.getLogger(__name__)

class MaintenanceModeMiddleware(object):

    def cond_wait_for_end_of_maintenance(self, request, retry_after):
        """
        Wait for remaining maintenance time if waiting time is
        less than MAX_WAIT_FOR_END
        """
        ends_in = (retry_after - datetime.now()).total_seconds()
        max_wait = MAX_WAIT_FOR_END
        if ends_in > 0 and ends_in < max_wait:
            logger.info(
                u"[%s] waiting for %ss" % (
                    request.path, ends_in
                )
            )
            sleep(ends_in)
        return

    def process_request(self, request):
        # Allow access if middleware is not activated
        value = settings.MAINTENANCE_MODE or maintenance.status()
        if not value:
            return None

        if isinstance(value, datetime):
            retry_after = value
        else:
            retry_after = None

        # used by template
        request.retry_after = retry_after

        if retry_after:
            self.cond_wait_for_end_of_maintenance(request, retry_after)

        if retry_after and datetime.now() > retry_after:
            # maintenance ended
            return None

        INTERNAL_IPS = maintenance.IPList(settings.INTERNAL_IPS)

        # Preferentially check HTTP_X_FORWARDED_FOR b/c a proxy
        # server might have obscured REMOTE_ADDR
        for ip in request.META.get('HTTP_X_FORWARDED_FOR', '').split(','):
            if ip.strip() in INTERNAL_IPS:
                return None

        # Allow access if remote ip is in INTERNAL_IPS
        if request.META.get('REMOTE_ADDR') in INTERNAL_IPS:
            return None

        # Allow access if the user doing the request is logged in and a
        # staff member.
        if hasattr(request, 'user') and request.user.is_staff:
            return None

        # Check if a path is explicitly excluded from maintenance mode
        for url in IGNORE_URLS:
            if url.match(request.path_info):
                return None

        # Otherwise show the user the 503 page
        resolver = urlresolvers.get_resolver(None)

        if django.VERSION < (1, 8):
            callback, param_dict = resolver._resolve_special('503')
        else:
            callback, param_dict = resolver.resolve_error_handler('503')

        response = callback(request, **param_dict)

        if retry_after:
            response["Retry-After"] = format_date_time(
                mktime(retry_after.timetuple())
            )

        return response
