try:
    from django.conf.urls import include, url
except ImportError:
    from django.conf.urls.defaults import include, url

from django.http import HttpResponse

# URL test patterns for popularity. Use this file to ensure a consistent
# set of URL patterns are used when running unit tests. This test_urls
# module should be referred to by your test class.

urlpatterns = [
    url('^$', lambda r: HttpResponse('Rendered response page'), name='test'),
    url('^ignored/$', lambda r: HttpResponse('Rendered response page'), name='test'),
]
