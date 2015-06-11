from cuddlybuddly.storage.s3.storage import S3Storage

class CustomS3Storage(S3Storage):
    def __init__(self, bucket=None, access_key=None, secret_key=None,
                 headers=None, calling_format=None, cache=None, base_url=None):
        super(CustomS3Storage, self).__init__(bucket, access_key, secret_key,
                 headers, calling_format, cache, base_url)

    def path(self, name):
        return self._path(name)
  