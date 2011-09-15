FIXTURE_DIRS = ( 
   '/www/rumba/rumbacaracas/locations/fixtures/',
 )

TEMPLATE_DIRS = ( 
    '/www/rumba/rumbacaracas/templates',
 )

OLDBOGOTA_PHOTO_PATH = '/home/maksim/Documents/Develop/oldcaracas/processed'

OLDDATABOGOTA_PHOTO_PATH = '/www/rumba/rumbacaracas/olddata/'
FAKE_IMPORT_IMAGE = '/home/maksim/test_images/tst_imgs/1.jpg'


FULL_BASE_URL = 'http://localhost:8000/'

MEDIA_ROOT = '/www/rumba/rumbacaracas/media'

STATIC_DOC_ROOT = '/www/rumba/rumbacaracas/media'

LOCALE_PATHS = ( 
    '/www/rumba/rumbacaracas/locale/',
 )



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'caracas', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cydemAjD', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
    'olddata': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'oldcaracasdata', # Or path to database file if using sqlite3.
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


FACEBOOK_APP_ID = '148108908569986'
FACEBOOK_API_KEY = FACEBOOK_APP_ID #'15d12186d338568b8b5634e27aafb7cd'
FACEBOOK_SECRET_KEY = '56fa7f47fe58a05ba2659f812c11f7d4'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
 )
