import os, codecs
from django.conf import settings
from compressor.js import JsCompressor
from compressor.exceptions import UncompressableFileError

class CustomJsCompressor(JsCompressor):

    def __init__(self, content=None, output_prefix="js", context=None):
        super(CustomJsCompressor, self).__init__(content, output_prefix, context)

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
  