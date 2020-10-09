# -*- coding: utf-8 -*-

import os

from .conf import settings


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
        except:  # noqa
            pass
        return False


def activate():
    try:
        open(settings.MAINTENANCE_LOCKFILE_PATH, "ab", 0).close()
    except OSError:
        pass  # shit happens


def deactivate():
    if os.path.isfile(settings.MAINTENANCE_LOCKFILE_PATH):
        os.remove(settings.MAINTENANCE_LOCKFILE_PATH)


def status():
    return settings.MAINTENANCE_MODE or os.path.isfile(settings.MAINTENANCE_LOCKFILE_PATH)
