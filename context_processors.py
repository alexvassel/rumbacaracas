from django.conf import settings # import the settings file


def base_url(context):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'ADMIN_MEDIA_URL': settings.ADMIN_MEDIA_PREFIX}