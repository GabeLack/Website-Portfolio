from django.conf import settings


def site_url_prefix(request):
    return {
        'site_url_prefix': getattr(settings, 'URL_PREFIX', ''),
    }
