# -*- coding: utf-8 -*-

import os

from maintenancemode.conf import settings


def get_maintenance_mode():
    return os.path.isfile(settings.MAINTENANCE_LOCKFILE_PATH)

def set_maintenance_mode(value):
    if value is True:
        try:
            open(settings.MAINTENANCE_LOCKFILE_PATH, 'ab', 0).close()
        except OSError:
            pass  # shit happens

    if value is False and get_maintenance_mode():
        os.remove(settings.MAINTENANCE_LOCKFILE_PATH)
