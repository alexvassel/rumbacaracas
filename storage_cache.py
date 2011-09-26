import os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import smart_str
from django.utils.hashcompat import md5_constructor

from cuddlybuddly.storage.s3.cache import Cache
from django.core.cache import cache

CACHE_TIMEOUT = 30

#cache.set('my_key', 'hello, world!', 30)
#cache.get('my_key')
#ache.get('my_key', 'has expired')
#cache.add('add_key', 'New value')
#cache.delete('a')


class FileSystemCache(Cache):
    def __init__(self, cache_dir=None):
        if cache_dir is None:
            cache_dir = getattr(settings, 'CUDDLYBUDDLY_STORAGE_S3_FILE_CACHE_DIR', None)
            if cache_dir is None:
                raise ImproperlyConfigured(
                    '%s requires CUDDLYBUDDLY_STORAGE_S3_FILE_CACHE_DIR to be set to a directory.' % type(self)
                )
        self.cache_dir = cache_dir

    def _path(self, name):
        return os.path.join(self.cache_dir, md5_constructor(smart_str(name)).hexdigest())

    def exists(self, name):
        if self.modified_time(name):
            return True
        return None

    def size(self, name):
        try:
            file = open(self._path(name))
            size = int(file.readlines()[1])
            file.close()
        except:
            size = None
        return size

    def modified_time(self, name):
        try:
            file = open(self._path(name))
            mtime = float(file.readlines()[2])
            file.close()
        except:
            mtime = None
        return mtime

    def save(self, name, size, mtime):
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        file = open(self._path(name), 'w')
        file.write(smart_str(name)+'\n'+str(size)+'\n'+str(mtime))
        file.close()

    def remove(self, name):
        name = self._path(name)
        if os.path.exists(name):
            os.remove(name)
