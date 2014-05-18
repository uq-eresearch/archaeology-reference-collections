
from common import *


######## DEBUG

DEBUG = True
TEMPLATE_DEBUG = DEBUG

############################



#############################
### DJANGO DEBUG TOOLBAR

try:
    __import__('debug_toolbar')
except ImportError:
    DEBUG_TOOLBAR = False
else:
    DEBUG_TOOLBAR = True

if DEBUG_TOOLBAR:
    INSTALLED_APPS += ('debug_toolbar',)


### END DEBUG TOOLBAR
#############################



LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'formatters': {
       'simple': {
           'format': '%(levelname)s %(message)s',
       },
   },
   'handlers': {
       'console':{
           'level':'DEBUG',
           'class':'logging.StreamHandler',
           'formatter': 'simple'
       },
   },
   'loggers': {
       'django': {
           'handlers': ['console'],
           'level': 'DEBUG',
       },
       'django.request': {
           'handlers': ['console'],
           'level': 'DEBUG',
       },
       'refcollections': {
          'handlers': ['console'],
          'level': 'DEBUG'
       },
       'bulkimport': {
          'handlers': ['console'],
          'level': 'DEBUG'
       },
       '': {
          'handlers': ['console'],
          'level': 'DEBUG'
       }
   }
}