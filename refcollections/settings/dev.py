
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
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

    INSTALLED_APPS += ('debug_toolbar',)

    # Debug Toolbar configuration
    INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False
    }

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
   }   
}