import os, codecs
from django.conf import settings
from compressor.exceptions import UncompressableFileError
from compressor.cache import get_hexdigest, get_mtime
from compressor.utils.decorators import cached_property, memoize
from compressor.base import Compressor, SOURCE_FILE, SOURCE_HUNK

class CustomCssCompressor(Compressor):

    def __init__(self, content=None, output_prefix="css", context=None):
        super(CustomCssCompressor, self).__init__(content=content,
            output_prefix=output_prefix, context=context)
        self.filters = list(settings.COMPRESS_CSS_FILTERS)
        self.type = output_prefix

    def split_contents(self):
        if self.split_content:
            return self.split_content
        self.media_nodes = []
        for elem in self.parser.css_elems():
            data = None
            elem_name = self.parser.elem_name(elem)
            elem_attribs = self.parser.elem_attribs(elem)
            if elem_name == 'link' and elem_attribs['rel'] == 'stylesheet':
                basename = self.get_basename(elem_attribs['href'])
                filename = self.get_filename(basename)
                data = (SOURCE_FILE, filename, basename, elem)
            elif elem_name == 'style':
                data = (SOURCE_HUNK, self.parser.elem_content(elem), None, elem)
            if data:
                self.split_content.append(data)
                media = elem_attribs.get('media', None)
                # Append to the previous node if it had the same media type,
                # otherwise create a new node.
                if self.media_nodes and self.media_nodes[-1][0] == media:
                    self.media_nodes[-1][1].split_content.append(data)
                else:
                    node = CustomCssCompressor(content=self.parser.elem_str(elem),
                                         context=self.context)
                    node.split_content.append(data)
                    self.media_nodes.append((media, node))
        return self.split_content

    def output(self, *args, **kwargs):
        if (settings.COMPRESS_ENABLED or settings.COMPRESS_PRECOMPILERS or
                kwargs.get('forced', False)):
            # Populate self.split_content
            self.split_contents()
            if hasattr(self, 'media_nodes'):
                ret = []
                for media, subnode in self.media_nodes:
                    subnode.extra_context.update({'media': media})
                    ret.append(subnode.output(*args, **kwargs))
                return ''.join(ret)
        return super(CustomCssCompressor, self).output(*args, **kwargs)

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

    @cached_property
    def cachekey(self):
        return get_hexdigest(''.join(
            [self.content] + self.mtimes).encode(self.charset), 12)