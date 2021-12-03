"""
WSGI config for Scheduler project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'Scheduler.settings'

application = get_wsgi_application()
