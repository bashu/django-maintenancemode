# -*- coding: utf-8 -*-

from django.http import HttpResponse


class HttpResponseTemporaryUnavailable(HttpResponse):
    status_code = 503
