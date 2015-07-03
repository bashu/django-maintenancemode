import django

if django.VERSION < (1, 3):
    from django.conf.urls.defaults import *
else:
    from django.conf.urls import *

urlpatterns = patterns('example.views',
    url(r'^$', 'index'),
    url(r'^ignored/$', 'index'),
)

