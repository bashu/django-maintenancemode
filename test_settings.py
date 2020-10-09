import os, re

SECRET_KEY = 'DUMMY_SECRET_KEY'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

INTERNAL_IPS = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'test_templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

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
    'django.contrib.messages',
    'django.contrib.sites',

    'maintenancemode',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'maintenancemode.middleware.MaintenanceModeMiddleware',
)

ROOT_URLCONF = 'test_urls'

SITE_ID = 1

MAINTENANCE_MODE = False  # or ``True`` and use ``maintenance`` command
MAINTENANCE_IGNORE_URLS = (
    re.compile(r'^/ignored.*'),
)
