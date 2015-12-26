# -*- coding: utf-8 -*-

import re
import django

from django.conf import urls
from django.core import urlresolvers

from .conf import settings
from . import utils as maintenance

urls.handler503 = 'maintenancemode.views.temporary_unavailable'
urls.__all__.append('handler503')

IGNORE_URLS = tuple([re.compile(u) for u in settings.MAINTENANCE_IGNORE_URLS])


class MaintenanceModeMiddleware(object):

    def process_request(self, request):
        # Allow access if middleware is not activated
        if not (settings.MAINTENANCE_MODE or maintenance.status()):
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

        return callback(request, **param_dict)
