from django.conf import settings

MAINTENANCE_MODE = getattr(settings, 'MAINTENANCE_MODE', False)
MAINTENANCE_IGNORE_URLS = getattr(settings, 'MAINTENANCE_IGNORE_URLS', ())
MAINTENANCE_VIEW = getattr(settings, 'MAINTENANCE_VIEW', 'maintenancemode.views.defaults.temporary_unavailable')