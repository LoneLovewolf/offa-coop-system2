import os
import sys

# Add your project root directory to Python path
path = '/home/LoneLovewolf'
if path not in sys.path:
    sys.path.insert(0, path)

# Point Django to your settings file
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Load the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()