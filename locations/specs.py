from imagekit.specs import ImageSpec
from imagekit import processors

# first we define our thumbnail resize processor
class ResizeThumb( processors.Resize ):
    width = 183
    height = 98
    crop = True

class LogoThumb( processors.Resize ):
    width = 188
    height = 138
    crop = True


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
class Logo( ImageSpec ):
    access_as = 'logo'
    pre_cache = False
    processors = [LogoThumb, EnchanceThumb]
