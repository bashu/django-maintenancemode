from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'testproject.testapp.views.index'),
    url(r'^ignored/$', 'testproject.testapp.views.index'),
)
