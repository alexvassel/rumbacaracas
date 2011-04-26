from imagekit.specs import ImageSpec
from imagekit import processors

# first we define our thumbnail resize processor
class ResizeThumb( processors.Resize ):
    width = 168
    height = 168
    crop = True

class BigImage( processors.Resize ):
    width = 540
    height = 540
    upscale = False
    crop = False

# now let's create an adjustment processor to enhance the image at small sizes
class EnchanceThumb( processors.Adjustment ):
    contrast = 1.2
    sharpness = 1.1

# now we can define our thumbnail spec
class Thumbnail( ImageSpec ):
    access_as = 'thumbnail'
    pre_cache = False
    processors = [ResizeThumb, EnchanceThumb]


# now we can define our thumbnail spec
class PhotoBig( ImageSpec ):
    access_as = 'bigimg'
    pre_cache = False
    processors = [BigImage]
