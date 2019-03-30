import os, re

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.sites',

    'maintenancemode',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'maintenancemode.middleware.MaintenanceModeMiddleware',
)

ROOT_URLCONF = 'maintenancemode.tests'

SITE_ID = 1

MAINTENANCE_MODE = True  # or ``False`` and use ``maintenance`` command
MAINTENANCE_IGNORE_URLS = (
    re.compile(r'^/ignored.*'),
)
