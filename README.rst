======================
django-maintenancemode
======================

django-maintenancemode is a middleware that allows you to temporary shutdown
your site for maintenance work.

Logged in users having staff credentials can still fully use
the site as can users visiting the site from an ip address defined in
Django's INTERNAL_IPS.


Installation
============

* Download django-maintenancemode from http://pypi.python.org/pypi/django-maintenancemode
  or https://github.com/shanx/django-maintenancemode
* Install using: `python setup.py install`
* In your Django settings file add maintenancemode to your MIDDLEWARE_CLASSES.
  Make sure it comes after Django's AuthenticationMiddleware. Like so::

   MIDDLEWARE_CLASSES = (
       'django.middleware.common.CommonMiddleware',
       'django.contrib.sessions.middleware.SessionMiddleware',
       'django.contrib.auth.middleware.AuthenticationMiddleware',
       'django.middleware.doc.XViewMiddleware',
   
       'maintenancemode.middleware.MaintenanceModeMiddleware',
   )

* django-maintenancemode works the same way as handling 404 or 500 error in
  Django work. It adds a handler503 which you can override in your main urls.py
  or you can add a 503.html to your templates directory.
* In your Django settings file add a variable called MAINTENANCE_MODE. Setting
  this variable to True activates the middleware.


Configuration
=============
If you do not configure the settings below in your own project settings.py,
they assume default values:

``MAINTENANCE_MODE``
--------------------

:Default: ``False``

Boolean. Enable/disable maintenance mode.

``MAINTENANCE_IGNORE_URLS``
---------------------------

:Default: ``()``

Sequence of URL path regexes to exclude from the maintenance mode.

Example::

    MAINTENANCE_IGNORE_URLS = (
        r'^/docs/.*',
        r'^/contact'
    )

Some observations:

* If user is logged in and staff member, the maintenance page is
  not displayed.

* If user's ip is in INTERNAL_IPS, the maintenance page is
  not displayed.

``MAINTENANCE_VIEW``
--------------------

:Default: ``maintenancemode.views.defaults.temporary_unavailable``

String. View function for page generation if you need custom template engine like Jinja2 or some.