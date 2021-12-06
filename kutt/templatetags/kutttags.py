from django import template
from django.urls import is_valid_path, reverse
from urllib.parse import parse_qsl
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters

register = template.Library()

def get_current_app(request):
    app = None
    if hasattr(request, 'current_app'):
        app = getattr(request, 'current_app')
    elif hasattr(request, 'model_admin'):
        model_admin = getattr(request, 'model_admin')
        if hasattr(model_admin, 'opts'):
            opts = getattr(model_admin, 'opts')
            app = opts.app_config.name
    return app

def get_model_url(context):
    url = ''
    try:
        opts = context.get("opts")
        request = context.get("request")

        key = "{}:{}_{}_changelist".format(
            get_current_app(request), opts.app_label, opts.model_name
        )
        url = reverse(key)
        preserved_filters = dict(parse_qsl(context.get("preserved_filters")))
        if "_changelist_filters" in preserved_filters:
            preserved_filters = preserved_filters["_changelist_filters"]
            url = add_preserved_filters({"preserved_filters": preserved_filters, "opts": opts}, url)
    except:
       pass
    return url

@register.simple_tag(takes_context=True)
def get_kprevious_url(context):
    referer = context.request.META.get("HTTP_REFERER")
    if not referer or context.request.META.get("PATH_INFO") in referer:
        # return to model list
        return get_model_url(context)
    return context.request.META.get("HTTP_REFERER")
