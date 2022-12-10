import os

from django.conf import settings  # noqa

from appconf import AppConf


class MaintenanceSettings(AppConf):
    IGNORE_URLS = ()
    LOCKFILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "maintenance.lock")
    MODE = False
    ONLY_EVALUATE_DURING_RELOAD = False

    class Meta:
        prefix = "maintenance"
        holder = "maintenancemode.conf.settings"
