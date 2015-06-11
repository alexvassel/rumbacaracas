from django.template.defaultfilters import slugify
from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

def SlugifyUniquely(value, model, slugfield="slug", maxlength=50):
    """Returns a slug on a name which is unique within a model's table

    This code suffers a race condition between when a unique
    slug is determined and when the object with that slug is saved.
    It's also not exactly database friendly if there is a high
    likelyhood of common slugs being attempted.

    A good usage pattern for this code would be to add a custom save()
    method to a model with a slug field along the lines of:



            def save(self):
                if not self.id:
                    # replace self.name with your prepopulate_from field
                    self.slug = SlugifyUniquely(self.name, self.__class__)
            super(self.__class__, self).save()

    Original pattern discussed at
    http://www.b-list.org/weblog/2006/11/02/django-tips-auto-populated-fields
    """
    suffix = 0
    potential = base = slugify(value)
    while True:
        if suffix:
            calculated_max_length = maxlength - 1 - len(str(suffix))
            potential = "-".join([base[:calculated_max_length], str(suffix)])
        if not model.objects.filter(**{slugfield: potential}).count():
            return potential
        # we hit a conflicting slug, so bump the suffix & try again
        suffix += 1




class ContentTypeRestrictedFileField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file
        file.storage = RUMBACR_STORAGE
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('Please keep filesize under %(maxsize)s. Current filesize %(current)s') % dict(maxsize=filesizeformat(self.max_upload_size), current=filesizeformat(file._size)))
            else:
                raise forms.ValidationError(_('File type is not supported'))
        except AttributeError:
            pass

        return data

class ImageRestrictedFileField(ContentTypeRestrictedFileField):
    """
    Same as ContentTypeRestrictedFileField, but with default:
        * content_types - ['image/gif','image/jpeg','image/pjpeg','image/png','image/tiff','image/bmp']
        * max_upload_size - 5MB - 5242880
    """
    def __init__(self, *args, **kwargs):
        kwargs["content_types"] = settings.IMAGE_CONTENT_TYPES
        kwargs["max_upload_size"] = settings.IMAGE_MAX_UPLOAD_SIZE
        
        super(ImageRestrictedFileField, self).__init__(*args, **kwargs)


from cuddlybuddly.storage.s3.storage import S3Storage
#TODO FIX ON PRODUCTION
RUMBACR_STORAGE = S3Storage(bucket='rumba_test', base_url='http://s3.amazonaws.com/rumba_test/')
#RUMBACR_STORAGE = S3Storage(bucket='rumba_test', base_url='http://s3.amazonaws.com/rumba_test/')