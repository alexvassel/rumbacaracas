from django.core.files.storage import get_storage_class
from cuddlybuddly.storage.s3 import S3Storage

class CachedS3Storage(S3Storage):
    """
    S3 storage backend that saves the files locally, too.
    """
    def __init__(self, *args, **kwargs):
        super(S3Storage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        name = super(S3Storage, self).save(name, content)
        self.local_storage._save(name, content)
        return name

    def path(self, name):
        return self.local_storage.path(name)