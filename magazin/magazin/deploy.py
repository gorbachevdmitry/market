"""
WSGI config for magazin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/dmitrygorbachev/market/magazin'  # use your own PythonAnywhere username here
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "magazin.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
