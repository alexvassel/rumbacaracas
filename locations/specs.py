from imagekit.specs import ImageSpec
from imagekit import processors

# first we define our thumbnail resize processor
class ResizeThumb( processors.Resize ):
    width = 183
    height = 98
    crop = True

class LogoThumb( processors.Resize ):
    width = 188
    crop = False

class SquareLogoThumb( processors.Resize ):
    width = 98
    height = 98
    crop = True


class BigLogoThumb( processors.Resize ):
    width = 192
    height = 162
    crop = True

class EventBigThumb( processors.Resize ):
    width = 595
    height = 244
    crop = True

class EventBigHighThumb( processors.Resize ):
    width = 188
    height = 290
    crop = True


class EventSmallThumb( processors.Resize ):
    width = 112
    height = 76
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
class Square( ImageSpec ):
    access_as = 'square'
    pre_cache = False
    processors = [SquareLogoThumb, EnchanceThumb]



# now we can define our thumbnail spec
class BigLogo( ImageSpec ):
    access_as = 'biglogo'
    pre_cache = False
    processors = [BigLogoThumb, EnchanceThumb]


# now we can define our thumbnail spec
class Logo( ImageSpec ):
    access_as = 'logo'
    pre_cache = False
    processors = [LogoThumb, EnchanceThumb]


# now we can define our thumbnail spec
class EventBig( ImageSpec ):
    access_as = 'bigimg'
    pre_cache = False
    processors = [EventBigThumb]

# now we can define our thumbnail spec
class EventSmall( ImageSpec ):
    access_as = 'smallimg'
    pre_cache = False
    processors = [EventSmallThumb, EnchanceThumb]

# now we can define our thumbnail spec
class EventLogo( ImageSpec ):
    access_as = 'eventlogo'
    pre_cache = False
    processors = [EventBigHighThumb, EnchanceThumb]


