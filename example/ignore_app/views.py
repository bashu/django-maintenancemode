from django.http import HttpResponse


def home(request):
    return HttpResponse('Excluded App from maintenance mode')


def page_x(request):
    return HttpResponse('Excluded App Page from maintenance mode')
