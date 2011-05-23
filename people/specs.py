from imagekit.specs import ImageSpec
from imagekit import processors

class BigImage( processors.Resize ):
    width = 540
    height = 540
    upscale = False
    crop = False

class ResizeThumb( processors.Resize ):
    width = 316
    height = 196
    crop = True

class SquareThumb( processors.Resize ):
    width = 286
    height = 196
    crop = True

class SmallThumb( processors.Resize ):
    width = 135
    height = 135
    crop = True


class EnchanceThumb( processors.Adjustment ):
    contrast = 1.2
    sharpness = 1.1

class PhotoBig( ImageSpec ):
    access_as = 'bigimg'
    pre_cache = False
    processors = [BigImage]

class WideThumbnail( ImageSpec ):
    access_as = 'widethumb'
    pre_cache = False
    processors = [ResizeThumb, EnchanceThumb]

class SmallThumbnail( ImageSpec ):
    access_as = 'smallthumb'
    pre_cache = False
    processors = [SmallThumb, EnchanceThumb]


class SquareThumbnail( ImageSpec ):
    access_as = 'squarethumb'
    pre_cache = False
    processors = [SquareThumb, EnchanceThumb]
