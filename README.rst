django-maintenancemode
======================

django-maintenancemode is a middleware that allows you to temporary shutdown
your site for maintenance work.

Logged in users having staff credentials can still fully use
the site as can users visiting the site from an IP address defined in
Django's ``INTERNAL_IPS``.

Authored by `Remco Wendt <https://github.com/shanx>`_, and some great `contributors <https://github.com/shanx/django-maintenancemode/contributors>`_.

.. image:: https://img.shields.io/pypi/v/django-maintenancemode.svg
    :target: https://pypi.python.org/pypi/django-maintenancemode/

.. image:: https://img.shields.io/pypi/dm/django-maintenancemode.svg
    :target: https://pypi.python.org/pypi/django-maintenancemode/

.. image:: https://img.shields.io/github/license/shanx/django-maintenancemode.svg
    :target: https://pypi.python.org/pypi/django-maintenancemode/

.. image:: https://img.shields.io/travis/shanx/django-maintenancemode.svg
    :target: https://travis-ci.org/shanx/django-maintenancemode/

How it works
------------

``maintenancemode`` works the same way as handling 404 or 500 error in
Django work. It adds a ``handler503`` which you can override in your
main ``urls.py`` or you can add a ``503.html`` to your templates
directory.

* If user is logged in and staff member, the maintenance page is
  not displayed.

* If user's IP is in ``INTERNAL_IPS``, the maintenance page is
  not displayed.

* To override the default view which is used if the maintenance mode
  is enabled you can simply define a ``handler503`` variable in your
  ROOT_URLCONF_, similar to how you would customize other `error handlers`_,
  e.g. :

  .. code-block:: python

      handler503 = 'example.views.maintenance_mode'

Installation
------------

1. Either checkout ``maintenancemode`` from GitHub, or install using pip :

   .. code-block:: bash

       pip install django-maintenancemode

2. Add ``maintenancemode`` to your ``INSTALLED_APPS`` :

   .. code-block:: python

       INSTALLED_APPS = (
           ...
           'maintenancemode',
       )

3. Add ``MaintenanceModeMiddleware`` to ``MIDDLEWARE_CLASSES``, make sure it comes after ``AuthenticationMiddleware`` :

   .. code-block:: python

       MIDDLEWARE_CLASSES = (
           ...
           'django.contrib.auth.middleware.AuthenticationMiddleware',
           'maintenancemode.middleware.MaintenanceModeMiddleware',
       )                

4. Add variable called ``MAINTENANCE_MODE`` in your project's ``settings.py`` file :

   .. code-block:: python

       MAINTENANCE_MODE = True  # Setting this variable to ``True`` activates the middleware.

   or set ``MAINTENANCE_MODE`` to ``False`` and use ``maintenance`` command :

   .. code-block:: shell

       python ./manage.py maintenance <on|off>

Please see ``example`` application. This application is used to
manually test the functionalities of this package. This also serves as
a good example...

You need only Django 1.4 or above to run that. It might run on older
versions but that is not tested.

Configuration
-------------

There are various optional configuration options you can set in your ``settings.py``

.. code-block:: python

    # Enable / disable maintenance mode.
    # Default: False
    MAINTENANCE_MODE = True  # or ``False`` and use ``maintenance`` command
    
    # Sequence of URL path regexes to exclude from the maintenance mode.
    # Default: ()
    MAINTENANCE_IGNORE_URLS = (
        r'^/docs/.*',
        r'^/contact'
    )

License
-------

``django-maintenancemode`` is released under the BSD license.

.. _ROOT_URLCONF: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
.. _`error handlers`: https://docs.djangoproject.com/en/dev/topics/http/views/#customizing-error-views
