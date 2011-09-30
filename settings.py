# Django settings for rumbacaracas project.
#from django.middleware.cache import FetchFromCacheMiddleware
import os
import datetime
from django.utils.encoding import force_unicode, smart_str

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = ( 
    # ('Your Name', 'your_email@domain.com'),
 )

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

SHORT_DATE_FORMAT = 'd.m.Y'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'es'



SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/admin-media/'
#ADMIN_MEDIA_PREFIX = MEDIA_URL + "grappelli/"
ADMIN_MEDIA_PREFIX = MEDIA_URL + "admin/"



# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xk(sgv%96^$2)1h_c#^vx0svfqufou8)-8#^2n6nn590sw(a)3'

# List of callables that know how to import templates from various sources.

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
#     'django.template.loaders.eggs.Loader',
 )

BREADCRUMBS = True
BREADCRUMBS_AUTO_HOME = True



MIDDLEWARE_CLASSES = (

    'django.middleware.cache.UpdateCacheMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'socialregistration.middleware.FacebookMiddleware',
    #'profiler_middleware.ProfileMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
 )

CACHE_MIDDLEWARE_SECONDS = 300
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
CACHE_MIDDLEWARE_KEY_PREFIX = 'car'


PROFILE_MIDDLEWARE_SORT = 'cumulative',
PROFILE_MIDDLEWARE_RESTRICTIONS = (50,)


AUTHENTICATION_BACKENDS = ( 
    'socialregistration.auth.FacebookAuth',
    'socialregistration.auth.TwitterAuth',
    'django.contrib.auth.backends.ModelBackend',
 )



FACEBOOK_APP_ID = '195992407109917'
FACEBOOK_API_KEY = FACEBOOK_APP_ID #'15d12186d338568b8b5634e27aafb7cd'
FACEBOOK_SECRET_KEY = '4266850c560e8f9266b07eb9d4e4137f'
FACEBOOK_REQUEST_PERMISSIONS = 'email,user_birthday,user_photos,user_events'



TWITTER_CONSUMER_KEY = 'IYdcJdgtroX4yE7tuqUscA'
TWITTER_CONSUMER_SECRET_KEY = 'nLD3noOIPwSZeyXZaUpwSVLIw9yZOKkAkNjpY85SqLw'
TWITTER_REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
TWITTER_AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'

SOCIALREGISTRATION_GENERATE_USERNAME = False

AUTH_PROFILE_MODULE = 'main.models.UserProfile'

ZINNIA_ENTRY_BASE_MODEL = 'news.zinniaModels.MyEntry'

def upload_to(instance, filename):
    import os
    format='uploads/news/%Y/%m/%d'
    date_field='creation_date'
    if getattr(instance, date_field, None):
        dt = getattr(instance, date_field)
    else:
        dt = datetime.datetime.now()
    path = os.path.normpath(force_unicode(dt.strftime(smart_str(format))))
    
    return os.path.join(path, filename)

ZINNIA_UPLOAD_TO = upload_to

ISSUU_API_KEY = "3g5tlt235dhwzwu9lf8yveetczya50u0"
ISSUU_API_SECRET = "0unbbypa2ck7ls8yjstzelyyssax2026"


OPENX_URL = 'http://ads.2rumba.com/www/api/v2/xmlrpc/'
#OPENX_URL = 'http://ads.2rumba.com/www/delivery/axmlrpc.php'
OPENX_USERNAME = 'eli'
OPENX_PASSWORD = 'adminbanners'


#TINYMCE_COMPRESSOR=True

#TINYMCE_DEFAULT_CONFIG = {
#    'plugins': "table,spellchecker,paste,searchreplace",
#    'theme': "advanced",
#    'cleanup_on_startup': True,
#    'custom_undo_redo_levels': 10,
#}
#ZINNIA_WYSIWYG = 'tinymce'

LOGIN_REDIRECT_URL = "/"

INTERNAL_IPS = ( '127.0.0.1', )


ROOT_URLCONF = 'urls'

#FULL_BASE_URL = 'http://rumbacaracas.com'


TEMPLATE_CONTEXT_PROCESSORS = ( 
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'zinnia.context_processors.version', # Optional
    'zinnia.context_processors.media',
    "django.core.context_processors.debug",
 )


INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'tinymce',
    'socialregistration',
    'events',
    'locations',
    'yourphotos',
    'yourvideos',
    'people',
    'main',
    'sortable',
    'tagging',
    #'mptt',
    'zinnia',
    'news',
    'preferences',
    'googlesearch',
    'debug_toolbar',
    'magazine',
    'subscribe',
    'legacy',
    'erumba',
    'storages',
    'cuddlybuddly.storage.s3',
    'compressor',
    #'photologue',
    #'tagging',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
 )

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

IMAGE_CONTENT_TYPES = ['image/gif','image/jpeg','image/pjpeg','image/png','image/tiff','image/bmp' ]
IMAGE_MAX_UPLOAD_SIZE = 5242880


GRAPPELLI_ADMIN_TITLE = "RUMBACARACAS"

DATABASE_ROUTERS = ['db_router.MyAppRouter']

try:
    import socket
    hostname = socket.gethostname().replace( '.', '_' ).replace( '-', '_' )
    exec "from host_settings.%s import *" % hostname
except ImportError, e:
    raise e

GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'