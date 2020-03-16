from django.conf.urls import url

from .views import home, page_x

urlpatterns = [
    url(r'^ignore_app/?$', home),
    url(r'^ignore_app/page_x/?$', page_x),
]
