# -*- coding: utf-8 -*-

from django.conf import settings  # pylint: disable=W0611
from appconf import AppConf


class MaintenanceSettings(AppConf):
    IGNORE_URLS = ()
    MODE = False

    class Meta:
        prefix = 'maintenance'
        holder = 'maintenancemode.conf.settings'
