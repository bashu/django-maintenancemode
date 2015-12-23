from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'index'),
    url(r'^ignored/$', 'index'),
]
