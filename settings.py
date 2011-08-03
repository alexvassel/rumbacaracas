# Django settings for rumbabogota project.
from django.middleware.cache import FetchFromCacheMiddleware

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
ADMIN_MEDIA_PREFIX = MEDIA_URL + "grappelli/"

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

CACHE_MIDDLEWARE_SECONDS = 60
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True


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
FACEBOOK_REQUEST_PERMISSIONS = 'email'



TWITTER_CONSUMER_KEY = 'zSTLzRjnKz2uQvSX5AgQ'
TWITTER_CONSUMER_SECRET_KEY = 'nwE8Y5CNllSMocUDom1K3k4FyVml8l5FU2W1uH0o'
TWITTER_REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
TWITTER_AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'

SOCIALREGISTRATION_GENERATE_USERNAME = False

AUTH_PROFILE_MODULE = 'main.models.UserProfile'

ZINNIA_ENTRY_BASE_MODEL = 'news.zinniaModels.MyEntry'


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

#FULL_BASE_URL = 'http://rumbabogota.com'


TEMPLATE_CONTEXT_PROCESSORS = ( 
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'zinnia.context_processors.version', # Optional
    'zinnia.context_processors.media',
    "django.core.context_processors.debug",
 )


INSTALLED_APPS = ( 
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sites',
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
    #'photologue',
    #'tagging',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
 )

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


DATABASE_ROUTERS = ['db_router.MyAppRouter']

try:
    import socket
    hostname = socket.gethostname().replace( '.', '_' ).replace( '-', '_' )
    exec "from host_settings.%s import *" % hostname
except ImportError, e:
    raise e
