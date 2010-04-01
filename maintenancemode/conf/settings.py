from django.conf import settings

MAINTENANCE_MODE = getattr(settings, 'MAINTENANCE_MODE', False)
MAINTENANCE_IGNORE_URLS = getattr(settings, 'MAINTENANCE_IGNORE_URLS', ())