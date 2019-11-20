from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'manager', 'manager.urls', name='manager'),
    host(r'corporate', 'corporate.urls', name='corporate'),
    host(r'public', 'public.urls', name='public'),
    host(r'', settings.ROOT_URLCONF, name='common'),
)