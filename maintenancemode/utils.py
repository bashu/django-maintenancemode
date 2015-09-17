# -*- coding: utf-8 -*-

import os

from .conf import settings


def activate():
    try:
        open(settings.MAINTENANCE_LOCKFILE_PATH, 'ab', 0).close()
    except OSError:
        pass  # shit happens


def deactivate():
    if os.path.isfile(settings.MAINTENANCE_LOCKFILE_PATH):
        os.remove(settings.MAINTENANCE_LOCKFILE_PATH)


def status():
    return settings.MAINTENANCE_MODE or os.path.isfile(
        settings.MAINTENANCE_LOCKFILE_PATH)
