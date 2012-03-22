import re
import django
from django.conf import settings
from django.core import urlresolvers


if django.VERSION[:2] <= (1, 3):
    from django.conf.urls import defaults as urls
else:
    from django.conf import urls

from maintenancemode.conf.settings.defaults import (MAINTENANCE_MODE,
                                                    MAINTENANCE_IGNORE_URLS)

urls.handler503 = 'maintenancemode.views.defaults.temporary_unavailable'
urls.__all__.append('handler503')

IGNORE_URLS = tuple([re.compile(url) for url in MAINTENANCE_IGNORE_URLS])


class MaintenanceModeMiddleware(object):
    def process_request(self, request):
        # Allow access if middleware is not activated
        if not MAINTENANCE_MODE:
            return None

        # Preferentially check HTTP_X_FORWARDED_FOR b/c a proxy server might have obscured REMOTE_ADDR
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
        if x_forwarded_for:
            remote_addr = x_forwarded_for.split(',')[0].strip()
        else:
            remote_addr = request.META.get('REMOTE_ADDR', None)

        # Allow access if remote ip is in INTERNAL_IPS
        if remote_addr in settings.INTERNAL_IPS:
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

        callback, param_dict = resolver._resolve_special('503')
        return callback(request, **param_dict)
