from django.conf.urls.defaults import *

urlpatterns = patterns('maintenancemode.views.tests',
    url(r'^$', 'index'),
    url(r'^ignored/$', 'index'),
)
