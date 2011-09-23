FIXTURE_DIRS = ( 
   '/home/maksim/Documents/Develop/rumbabogota/locations/fixtures/',
 )

TEMPLATE_DIRS = ( 
    '/home/maksim/Documents/Develop/rumbabogota/templates',
 )

OLDBOGOTA_PHOTO_PATH = '/home/maksim/Documents/Develop/oldbogota/processed'

OLDDATABOGOTA_PHOTO_PATH = '/mnt/rumbacaracas/www/vhosts/rumbacaracas.com/httpdocs/'
FAKE_IMPORT_IMAGE = '/home/maksim/test_images/tst_imgs/1.jpg'


FULL_BASE_URL = 'http://localhost.td'

MEDIA_ROOT = '/home/maksim/Documents/Develop/rumbabogota/media'

STATIC_DOC_ROOT = '/home/maksim/Documents/Develop/rumbabogota/media'

LOCALE_PATHS = ( 
    '/home/maksim/Documents/Develop/rumbabogota/locale/',
 )



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'caracas', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'cleopatra', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
    'olddata': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'oldcaracas', # Or path to database file if using sqlite3.
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


FACEBOOK_APP_ID = '237180929639489'
FACEBOOK_API_KEY = FACEBOOK_APP_ID #'15d12186d338568b8b5634e27aafb7cd'
FACEBOOK_SECRET_KEY = '68e652ad4024ba1c2a563e7ff833f856'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
 )


# Amazon S3 configs
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJAVN6BXUTZ3VMAVA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'rumba_test'