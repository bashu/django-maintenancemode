from django.conf.urls import url

from django.http import HttpResponse

urlpatterns = [
    url("^$", lambda r: HttpResponse("Rendered response page"), name="test"),
    url("^ignored/$", lambda r: HttpResponse("Rendered response page"), name="test"),
]
