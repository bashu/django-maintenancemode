import os
from distutils.core import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

from maintenancemode import __version__

setup(
    name='django-maintenancemode',
    version=__version__,
    packages=[
        'maintenancemode',
    ],
    include_package_data=True,
    license='BSD License',
    description="Django-maintenancemode allows you to temporary shutdown your site for maintenance work",
    long_description=README,
    url='https://github.com/shanx/django-maintenancemode',
    author='Remco Wendt',
    author_email='remco@maykinmedia.nl',
    maintainer='Basil Shubin',
    maintainer_email='basil.shubin@gmail.com',
    install_requires=[
        'django',
        'django-appconf',
    ],    
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
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
    zip_safe=False,
)
