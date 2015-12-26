from django.conf.urls import url

from .views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^ignored/$', index),
]
