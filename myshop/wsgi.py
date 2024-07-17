"""
WSGI config for myshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Add the project directory to the sys.path
project_home = '/home/Aasem/django-shop-project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Add the virtualenv site-packages directory to the sys.path
virtualenv_site_packages = '/home/Aasem/.local/share/virtualenvs/django-shop-project-PUeEk25Q/lib/python3.8/site-packages'
if virtualenv_site_packages not in sys.path:
    sys.path.insert(1, virtualenv_site_packages)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'yourproject.settings'  # Replace 'yourproject' with the actual project name

# Import Django and get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
