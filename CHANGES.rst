Changes
-------

0.11.5
~~~~~~

- Made sure the app runs on Django 3.2, dropped support for Django < 2.x. It may
  still work with Django 1.11, but this is no longer tested.

0.11.4
~~~~~~

- Changed the middleware to not fetch the user instance if both
  ``MAINTENANCE_ALLOW_STAFF`` and ``MAINTENANCE_ALLOW_SUPERUSER`` are
  ``False``.
- Added support for django 3.1.

0.11.3
~~~~~~

- Added support for django 2.x, dropped support for django < 1.11. It may
  still work with django 1.8, but this is no longer tested.

0.11.2
~~~~~~

- Getting ready for Django 1.10 release.
- Dropped support for Django 1.3 and older.

0.11.1
~~~~~~

- Enable network specify in INTERNAL_IPS

0.11.0
~~~~~~

- Added management command to set maintenance mode on/off

0.10.1
~~~~~~

- Made sure the app runs on Django 1.8.

0.10.0
~~~~~~

- Got rid of dependency on setuptools
- Added ability to exclude specific paths from maintenance mode with the
  ``MAINTENANCE_IGNORE_URLS`` setting.
- Use RequestContext when rending the ``503.html`` template.
- Use tox for running the tests instead of buildout.
- Made sure the app runs on Django 1.4.

0.9.3
~~~~~~

- Minor documentation updates for the switch to github, expect more changes to follow soon.

0.9.2
~~~~~~

- Fixed an issue with setuptools, thanks for reporting this ksato9700

0.9.1
~~~~~~

- Tested django-maintenancemode with django-1.0 release (following the 1.0.X release branch)
- Bundled buildout.cfg and bootstrap with the source version of the project, allowing repeatable buildout
- The middleware now uses its own default config file, thanks to a patch by semente
- Use INTERNAL_IPS to check for users that need access. user.is_staff will stay in place
  for backwards incompatibility. Thanks for the idea Joshua Works
- Have setup.py sdist only distribute maintenancemode itself, no longer distribute tests and buildout stuff
- Use README and CHANGES in setup.py's long_description, stolen from Jeroen's djangorecipe :)
- Updated the documentation and now use pypi as the documentation source (link there from google code)

0.9
~~~~~~

First release
