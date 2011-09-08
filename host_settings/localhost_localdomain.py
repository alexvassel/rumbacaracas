FIXTURE_DIRS = ( 
   '/www/rumba/rumbabogota/locations/fixtures/',
 )

TEMPLATE_DIRS = ( 
    '/www/rumba/rumbabogota/templates',
 )

OLDBOGOTA_PHOTO_PATH = '/home/maksim/Documents/Develop/oldbogota/processed'

OLDDATABOGOTA_PHOTO_PATH = '/www/rumba/rumbabogota/olddata/'
FAKE_IMPORT_IMAGE = '/home/maksim/test_images/tst_imgs/1.jpg'


FULL_BASE_URL = 'http://localhost.td'

MEDIA_ROOT = '/www/rumba/rumbabogota/media'

STATIC_DOC_ROOT = '/www/rumba/rumbabogota/media'

LOCALE_PATHS = ( 
    '/www/rumba/rumbabogota/locale/',
 )



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bogota', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cydemAjD', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
    'olddata': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'oldbogotadata', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cleopatra', # Not used with sqlite3.
    }
}

DEBUG=True
#LANGUAGE_CODE = 'es'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


FACEBOOK_APP_ID = '180051822005393'
FACEBOOK_API_KEY = FACEBOOK_APP_ID #'15d12186d338568b8b5634e27aafb7cd'
FACEBOOK_SECRET_KEY = 'aa512e0baa4dc6609320c8ce53b74dd1'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
 )
