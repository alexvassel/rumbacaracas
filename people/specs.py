from imagekit.specs import ImageSpec
from imagekit import processors

class BigImage( processors.Resize ):
    width = 540
    height = 540
    upscale = False
    crop = False

# now we can define our thumbnail spec
class PhotoBig( ImageSpec ):
    access_as = 'bigimg'
    pre_cache = False
    processors = [BigImage]
