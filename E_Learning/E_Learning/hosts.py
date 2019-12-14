# E_Learning/Hosts.py

from django.conf import settings
from django_hosts import patterns, host

# Defines the host patterns which will load the corresponding urls file for the subdomain that the user is connecting to
host_patterns = patterns('',
                         host(r'manager', 'manager.urls', name='manager'),
                         host(r'corporate', 'corporate.urls', name='corporate'),
                         host(r'public', 'public.urls', name='public'),
                         host(r'', settings.ROOT_URLCONF, name='common'),
                         )
