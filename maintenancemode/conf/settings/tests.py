import django
import os

TEST_ROOT = os.path.dirname(os.path.abspath(__file__))

if django.VERSION[:2] < (1, 3):
    DATABASE_ENGINE = 'sqlite3'           # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
    DATABASE_NAME = 'testproject.db'             # Or path to database file if using sqlite3.
    DATABASE_USER = ''             # Not used with sqlite3.
    DATABASE_PASSWORD = ''         # Not used with sqlite3.
    DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }

SITE_ID = 1

TEST_TEMPLATE_DIR = os.path.join(TEST_ROOT, os.pardir, os.pardir, 'tests', 'templates')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'maintenancemode.middleware.MaintenanceModeMiddleware',
)

ROOT_URLCONF = 'maintenancemode.conf.urls.tests'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django_jenkins',
    'maintenancemode',
)

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',
)
