from compressor.filters.css_default import CssAbsoluteFilter, URL_PATTERN
from compressor.conf import settings
import os

class CustomCssAbsoluteFilter(CssAbsoluteFilter):

    def __init__(self, *args, **kwargs):
        super(CustomCssAbsoluteFilter, self).__init__(*args, **kwargs)

    def input(self, filename=None, basename=None, **kwargs):
        if filename is not None:
            filename = os.path.normcase(os.path.abspath(os.path.join(settings.APPLICATION_ROOT, filename)))
        if (not (filename and filename.startswith(self.root)) and
                not self.find(basename)):
            return self.content
        self.path = basename.replace(os.sep, '/')
        self.path = self.path.lstrip('/')
        if self.url.startswith(('http://', 'https://')):
            self.has_scheme = True
            parts = self.url.split('/')
            self.url = '/'.join(parts[2:])
            self.url_path = '/%s' % '/'.join(parts[3:])
            self.protocol = '%s/' % '/'.join(parts[:2])
            self.host = parts[2]
        self.directory_name = '/'.join((self.url, os.path.dirname(self.path)))
        self.directory_name = self.directory_name.replace("static/static", "static")
        return URL_PATTERN.sub(self.url_converter, self.content)