# -*- coding: utf-8 -*-

import os

from django.conf import settings  # pylint: disable=W0611
from appconf import AppConf


class MaintenanceSettings(AppConf):
    IGNORE_URLS = ()
    LOCKFILE_PATH = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'maintenance.lock')
    MODE = False
    LOCKING_METHOD = 'file'
    CACHE_KEY = "DJANGO_MAINTENANCE_MODE_ON"
    CACHE_TTL = 60 * 60 * 24
    CACHE_BACKEND = "default"

    class Meta:
        prefix = 'maintenance'
        holder = 'maintenancemode.conf.settings'
