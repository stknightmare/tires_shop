import os
import sys

path = '/home/programming/django/tires_shop'
if path not in sys.path:
#    sys.path.append('/home/programming')
#    sys.path.append('/home/programming/django')

    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'tires_shop.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
