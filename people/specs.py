from imagekit.specs import ImageSpec
from imagekit import processors

class BigImage( processors.Resize ):
    width = 540
    height = 540
    upscale = False
    crop = False

class FullWidthImage( processors.Resize ):
    width = 640
    height = 2000
    upscale = False
    crop = False

class ResizeThumb( processors.Resize ):
    width = 316
    height = 196
    crop = True

class ThinThumb( processors.Resize ):
    width = 168
    height = 99
    crop = True


class SquareThumb( processors.Resize ):
    width = 286
    height = 196
    crop = True

class SmallThumb( processors.Resize ):
    width = 135
    height = 135
    crop = True


class MainThumb( processors.Resize ):
    width = 295
    height = 185
    crop = True

class MainMiniThumb( processors.Resize ):
    width = 126
    height = 78
    crop = True
    
class RightColumnThumb( processors.Resize ):
    width = 300
    height = 220
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

class FullWidth( ImageSpec ):
    access_as = 'fullwidth'
    pre_cache = False
    processors = [FullWidthImage]

class SmallThumbnail( ImageSpec ):
    access_as = 'smallthumb'
    pre_cache = False
    processors = [SmallThumb, EnchanceThumb]


class SquareThumbnail( ImageSpec ):
    access_as = 'squarethumb'
    pre_cache = False
    processors = [SquareThumb, EnchanceThumb]

class MainThumbnail( ImageSpec ):
    access_as = 'mainthumb'
    pre_cache = False
    processors = [MainThumb, EnchanceThumb]

class MainMiniThumbnail( ImageSpec ):
    access_as = 'mainminithumb'
    pre_cache = False
    processors = [MainMiniThumb, EnchanceThumb]



class ThinThumbnail( ImageSpec ):
    access_as = 'thinthumb'
    pre_cache = False
    processors = [ThinThumb, EnchanceThumb]
    
class RightColumnThumbnail( ImageSpec ):
    access_as = 'rightcolumnthumb'
    pre_cache = False
    processors = [RightColumnThumb]