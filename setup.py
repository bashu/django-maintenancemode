#!/usr/bin/env python

import os
import re
import sys
import codecs
import subprocess

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class TestRunner(TestCommand):
    user_options = []

    def run(self):
        raise SystemExit(subprocess.call([sys.executable, 'runtests.py']))


def read(*parts):
    file_path = os.path.join(os.path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-maintenancemode',
    version=find_version('maintenancemode', '__init__.py'),
    license='BSD License',

    install_requires=[
        'django-appconf',
        'ipy',
    ],
    requires=[
    ],

    description="django-maintenancemode allows you to temporary shutdown your site for maintenance work",
    long_description=read('README.rst'),

    author='Remco Wendt',
    author_email='remco@maykinmedia.nl',
    
    maintainer='Basil Shubin',
    maintainer_email='basil.shubin@gmail.com',

    url='http://github.com/shanx/django-maintenancemode',
    download_url='https://github.com/shanx/django-maintenancemode/zipball/master',

    packages=find_packages(exclude=('example*', '*.tests*')),
    include_package_data=True,

    tests_require=[
    ],
    cmdclass={
        'test': TestRunner,
    },

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',        
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
