import os, codecs
from django.conf import settings
from compressor.css import CssCompressor
from compressor.exceptions import UncompressableFileError
from compressor.cache import get_hexdigest, get_mtime
from compressor.utils.decorators import cached_property, memoize
from compressor.base import SOURCE_FILE, SOURCE_HUNK

class CustomCssCompressor(CssCompressor):

    def __init__(self, content=None, output_prefix="css", context=None):
        super(CustomCssCompressor, self).__init__(content=content,
            output_prefix=output_prefix, context=context)

    def get_filecontent(self, filename, charset):
        filename = os.path.abspath(os.path.join(settings.APPLICATION_ROOT, filename))
        with codecs.open(filename, 'rb', charset) as fd:
            try:
                return fd.read()
            except IOError, e:
                raise UncompressableFileError("IOError while processing "
                                               "'%s': %s" % (filename, e))
            except UnicodeDecodeError, e:
                raise UncompressableFileError("UnicodeDecodeError while "
                                              "processing '%s' with "
                                              "charset %s: %s" %
                                              (filename, charset, e))

    @cached_property
    def mtimes(self):
        return [str(get_mtime(os.path.abspath(os.path.join(settings.APPLICATION_ROOT, value))))
                for kind, value, basename, elem in self.split_contents()
                if kind == SOURCE_FILE]