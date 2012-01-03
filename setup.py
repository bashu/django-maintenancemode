from ez_setup import use_setuptools
use_setuptools()

import os
from setuptools import setup, find_packages

version = '0.9.2'

def read_file(name):
    return open(os.path.join(os.path.dirname(__file__), 
                             name)).read()    

readme = read_file('README')
changes = read_file('CHANGES')

setup(
    name='django-maintenancemode',
    version=version,
    description='Django-maintenancemode allows you to temporary shutdown your site for maintenance work',
    long_description='\n\n'.join([readme, changes]),
    author='Remco Wendt',
    author_email='remco@maykinmedia.nl',
    license = "BSD",
    platforms = ["any"],
    url='http://code.google.com/p/django-maintenancemode/',
    download_url='',
    packages=['maintenancemode', 'maintenancemode.conf',  'maintenancemode.conf.urls', 'maintenancemode.views'],
    include_package_data = False,
    classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Utilities',
    ],
    zip_safe=False,
)
