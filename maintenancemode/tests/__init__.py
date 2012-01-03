import re
import os.path

from django.test import TestCase
from django.test.client import Client
from django.template import TemplateDoesNotExist
from django.conf import settings

from maintenancemode import middleware as mw

class MaintenanceModeMiddlewareTestCase(TestCase):
    def setUp(self):
        # Reset config options adapted in the individual tests
        mw.MAINTENANCE_MODE = False
        settings.TEMPLATE_DIRS = ()
        settings.INTERNAL_IPS = ()

    def test_implicitly_disabled_middleware(self):
        "Middleware should default to being disabled"
        response = self.client.get('/')
        self.assertContains(response, text='Rendered response page', count=1, status_code=200)

    def test_disabled_middleware(self):
        "Explicitly disabling the MAINTENANCE_MODE should work"
        mw.MAINTENANCE_MODE = False

        response = self.client.get('/')
        self.assertContains(response, text='Rendered response page', count=1, status_code=200)

    def test_enabled_middleware_without_template(self):
        "Enabling the middleware without a proper 503 template should raise a template error"
        mw.MAINTENANCE_MODE = True

        self.assertRaises(TemplateDoesNotExist, self.client.get, '/')

    def test_enabled_middleware_with_template(self):
        "Enabling the middleware having a 503.html in any of the template locations should return the rendered template"
        mw.MAINTENANCE_MODE = True
        settings.TEMPLATE_DIRS = (settings.TEST_TEMPLATE_DIR,)

        response = self.client.get('/')
        self.assertContains(response, text='Temporary unavailable', count=1, status_code=503)
        self.assertContains(response, text='You requested: /', count=1, status_code=503)

    def test_middleware_with_non_staff_user(self):
        "A logged in user that is not a staff user should see the 503 message"
        mw.MAINTENANCE_MODE = True
        settings.TEMPLATE_DIRS = (settings.TEST_TEMPLATE_DIR,)

        from django.contrib.auth.models import User
        User.objects.create_user(username='maintenance', email='maintenance@example.org', password='maintenance_pw')

        self.client.login(username='maintenance', password='maintenance_pw')

        response = self.client.get('/')
        self.assertContains(response, text='Temporary unavailable', count=1, status_code=503)

    def test_middleware_with_staff_user(self):
        "A logged in user that _is_ a staff user should be able to use the site normally"
        mw.MAINTENANCE_MODE = True
        settings.TEMPLATE_DIRS = (settings.TEST_TEMPLATE_DIR,)

        from django.contrib.auth.models import User
        user = User.objects.create_user(username='maintenance', email='maintenance@example.org', password='maintenance_pw')
        user.is_staff = True
        user.save()

        self.client.login(username='maintenance', password='maintenance_pw')

        response = self.client.get('/')
        self.assertContains(response, text='Rendered response page', count=1, status_code=200)

    def test_middleware_with_internal_ips(self):
        "A user that visits the site from an IP in INTERNAL_IPS should be able to use the site normally"
        mw.MAINTENANCE_MODE = True
        settings.INTERNAL_IPS = ('127.0.0.1', )

        # Use a new Client instance to be able to set the REMOTE_ADDR used by INTERNAL_IPS
        client = Client(REMOTE_ADDR='127.0.0.1')

        response = client.get('/')
        self.assertContains(response, text='Rendered response page', count=1, status_code=200)

    def test_ignored_path(self):
        "A path is ignored when applying the maintanance mode and should be reachable normally"
        mw.MAINTENANCE_MODE = True
        mw.IGNORE_URLS = (
            re.compile(r'^/ignored.*'),
        )
        settings.TEMPLATE_DIRS = (settings.TEST_TEMPLATE_DIR,)

        response = self.client.get('/ignored/')
        self.assertContains(response, text='Rendered response page', count=1, status_code=200)
