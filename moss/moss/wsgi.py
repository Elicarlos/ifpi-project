# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/ElicarlosFerreira/mysite/mysite/settings.py'
## and your manage.py is is at '/home/ElicarlosFerreira/mysite/manage.py'
path = '/home/ElicarlosFerreira/ifpi-project/moss'
if path not in sys.path:
    sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'moss.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
