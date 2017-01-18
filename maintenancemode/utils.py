# -*- coding: utf-8 -*-

import os

from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.core.cache import get_cache
from django.core.exceptions import ImproperlyConfigured

from .conf import settings

LOCKING_METHOD = settings.MAINTENANCE_LOCKING_METHOD

CACHE_BACKEND = settings.MAINTENANCE_CACHE_BACKEND

cache = get_cache(CACHE_BACKEND)


class IPList(list):
    """Stolen from https://djangosnippets.org/snippets/1362/"""

    def __init__(self, ips):
        try:
            from IPy import IP
            for ip in ips:
                self.append(IP(ip))
        except ImportError:
            pass

    def __contains__(self, ip):
        try:
            for net in self:
                if ip in net:
                    return True
        except:
            pass
        return False


def activate(maintenance_duration=None):
    if maintenance_duration:
        cache_value = (
            datetime.now() + relativedelta(seconds=maintenance_duration)
        )
    else:
        cache_value = True
    if LOCKING_METHOD == "file":
        try:
            open(settings.MAINTENANCE_LOCKFILE_PATH, 'ab', 0).close()
        except OSError:
            pass  # shit happens
    elif LOCKING_METHOD == "cache":
        cache.set(
            settings.MAINTENANCE_CACHE_KEY,
            cache_value,
            settings.MAINTENANCE_CACHE_TTL
        )
    else:
        raise ImproperlyConfigured(
            "Unknown locking method %s" % LOCKING_METHOD)


def deactivate():
    LOCKING_METHOD = settings.MAINTENANCE_LOCKING_METHOD
    if LOCKING_METHOD == "file":
        if os.path.isfile(settings.MAINTENANCE_LOCKFILE_PATH):
            os.remove(settings.MAINTENANCE_LOCKFILE_PATH)
    elif LOCKING_METHOD == "cache":
        cache.delete(
            settings.MAINTENANCE_CACHE_KEY
        )
    else:
        raise ImproperlyConfigured(
            "Unknown locking method %s" % LOCKING_METHOD)


def status():
    LOCKING_METHOD = settings.MAINTENANCE_LOCKING_METHOD
    if LOCKING_METHOD == "file":
        return settings.MAINTENANCE_MODE or os.path.isfile(
            settings.MAINTENANCE_LOCKFILE_PATH)
    elif LOCKING_METHOD == "cache":
        return cache.get(settings.MAINTENANCE_CACHE_KEY)
    else:
        raise ImproperlyConfigured(
            "Unknown locking method %s" % LOCKING_METHOD)
