from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
                         host(r'manager', 'manager.urls', name='manager_urls'),
                         host(r'corporate', 'corporate.urls', name='corporate_urls'),
                         host(r'public', 'public.urls', name='public_urls'),
                         host(r'', settings.ROOT_URLCONF, name='common_urls'),
                         )
