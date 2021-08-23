# -*- coding: utf-8 -*-

import re
from django import VERSION as django_version
from django.conf import urls
from django.urls import get_resolver
from django.urls import resolvers
from django.utils.deprecation import MiddlewareMixin

from . import utils as maintenance
from .conf import settings

urls.handler503 = "maintenancemode.views.temporary_unavailable"
urls.__all__.append("handler503")

IGNORE_URLS = tuple([re.compile(u) for u in settings.MAINTENANCE_IGNORE_URLS])
DJANGO_VERSION_MAJOR = django_version[0]
DJANGO_VERSION_MINOR = django_version[1]

class MaintenanceModeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Allow access if middleware is not activated
        allow_staff = getattr(settings, "MAINTENANCE_ALLOW_STAFF", True)
        allow_superuser = getattr(settings, "MAINTENANCE_ALLOW_SUPERUSER", True)

        if not (settings.MAINTENANCE_MODE or maintenance.status()):
            return None

        INTERNAL_IPS = maintenance.IPList(settings.INTERNAL_IPS)

        # Preferentially check HTTP_X_FORWARDED_FOR b/c a proxy
        # server might have obscured REMOTE_ADDR
        for ip in request.META.get("HTTP_X_FORWARDED_FOR", "").split(","):
            if ip.strip() in INTERNAL_IPS:
                return None

        # Allow access if remote ip is in INTERNAL_IPS
        if request.META.get("REMOTE_ADDR") in INTERNAL_IPS:
            return None

        # Allow access if the user doing the request is logged in and a
        # staff member.
        if hasattr(request, "user"):
            if allow_staff and request.user.is_staff:
                return None

            if allow_superuser and request.user.is_superuser:
                return None

        # Check if a path is explicitly excluded from maintenance mode
        for url in IGNORE_URLS:
            if url.match(request.path_info):
                return None
        # Otherwise show the user the 503 page

        if DJANGO_VERSION_MAJOR >= 3 and DJANGO_VERSION_MINOR >= 2:
            # Checks if DJANGO version is great than 3.2.0 for breaking change
            resolver = resolvers.get_resolver(None)
            resolve = resolver.resolve_error_handler
            callback = resolve('503')

            return callback(request)
        else:
            resolver = get_resolver()

            callback, param_dict = resolver.resolve_error_handler("503")

            return callback(request, **param_dict)



