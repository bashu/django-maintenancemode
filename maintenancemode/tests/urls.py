from django.urls import re_path

from django.http import HttpResponse

urlpatterns = [
    re_path("^$", lambda r: HttpResponse("Rendered response page"), name="test"),
    re_path("^ignored/$", lambda r: HttpResponse("Rendered response page"), name="test"),
]
