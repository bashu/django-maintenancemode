from django.conf import settings

MAINTENANCE_MODE = getattr(settings, 'MAINTENANCE_MODE', False)