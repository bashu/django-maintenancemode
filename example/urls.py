from django.conf.urls import url
from django.conf.urls import include

from .views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^ignored/$', index),
    url(r'', include('ignore_app.urls')),
]
