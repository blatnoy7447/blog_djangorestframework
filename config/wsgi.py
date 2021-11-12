import os
import sys

# project home directory to the sys.path
project_home = '/home/blatnoy/blog_djangorestframework'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog_drf.settings'

# server django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
