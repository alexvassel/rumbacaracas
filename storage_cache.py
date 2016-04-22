from django.conf import settings
from django.utils.encoding import smart_str
from django.utils.hashcompat import md5_constructor

from cuddlybuddly.storage.s3.cache import Cache
from django.core.cache import get_cache

class DjangoCache(Cache):
    def __init__(self):
        #Use CUDDLYBUDDLY_STORAGE_S3_CACHE_BACKEND backend otherwise use default
        cache_backend = getattr(settings, 'CUDDLYBUDDLY_STORAGE_S3_CACHE_BACKEND', 'default')
        #Use CUDDLYBUDDLY_STORAGE_S3_CACHE_TIMEOUT timeout otherwise use backend value
        self.cache_timeout = getattr(settings, 'CUDDLYBUDDLY_STORAGE_S3_CACHE_TIMEOUT', None)
        self.cache = get_cache(cache_backend)
        
    def _key(self, name):
        return md5_constructor(smart_str(name)).hexdigest()

    def exists(self, name):
        file_dict = self.cache.get(self._key(name))
        if file_dict:
            return True
        return None

    def size(self, name):
        file_dict = self.cache.get(self._key(name))
        if file_dict:
            return file_dict['size']
        return None

    def modified_time(self, name):
        file_dict = self.cache.get(self._key(name))
        if file_dict:
            return file_dict['mtime']
        return None

    def save(self, name, size, getmtime):
        self.cache.add(self._key(name), dict(name=name, size=size, mtime=getmtime), timeout=self.cache_timeout)

    def remove(self, name):
        self.cache.delete(self._key(name))
