# -*- coding: utf-8 -*-

from django.template import RequestContext, loader

from . import http 


def temporary_unavailable(request, template_name='503.html'):
    """
    Default 503 handler, which looks for the requested URL in the
    redirects table, redirects if found, and displays 404 page if not
    redirected.

    Templates: ``503.html``
    Context:
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/')

    """
    t = loader.get_template(template_name)  # You need to have a 503.html template.
    context = RequestContext(request, {
        'request_path': request.path,
    })

    return http.HttpResponseTemporaryUnavailable(t.render(context))
