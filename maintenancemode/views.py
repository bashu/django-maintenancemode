# -*- coding: utf-8 -*-

import django

if django.get_version() >= '1.8':
    from django.template.loader import render_to_string
else:
    from django.template import loader, RequestContext

    def render_to_string(template_name, context=None, request=None):
        context_instance = RequestContext(request) if request else None

        return loader.render_to_string(
            template_name, context, context_instance)

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
    context = {
        'request_path': request.path,
    }
    return http.HttpResponseTemporaryUnavailable(
        render_to_string(template_name, context))
