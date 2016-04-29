from imagekit.specs import ImageSpec
from imagekit import processors

# first we define our thumbnail resize processor
class ResizeThumb( processors.Resize ):
    width = 168
    height = 168
    crop = True

# first we define our thumbnail resize processor
class ThinThumb( processors.Resize ):
    width = 168
    height = 99
    crop = True

class BigImage( processors.Resize ):
    width = 540
    height = 540
    upscale = False
    crop = False

class WidgetImage( processors.Resize ):
    width = 148
    height = 118
    crop = True

class SlideImage( processors.Resize ):
    width = 619
    height = 258
    upscale = True
    crop = True

class SliderImage( processors.Resize ):
    width = 600
    height = 330
    upscale = True
    crop = True

class BlogThumb( processors.Resize ):
    width = 228
    height = 168
    upscale = True
    crop = True

class MainThumb( processors.Resize ):
    width = 295
    height = 185
    crop = True

class MainMiniThumb( processors.Resize ):
    width = 126
    height = 78
    crop = True


class NewsThumb( processors.Resize ):
    width = 250
    height = 200
    crop = True
    
class RightColumnThumb( processors.Resize ):
    width = 300
    height = 220
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
class PhotoBig( ImageSpec ):
    access_as = 'bigimg'
    pre_cache = False
    processors = [BigImage]


# now we can define our thumbnail spec
class PhotoSlide( ImageSpec ):
    access_as = 'slide'
    pre_cache = False
    processors = [SlideImage]

# Custom, slider size
class CustomSlider( ImageSpec ):
    access_as = 'slider'
    pre_cache = False
    processors = [SliderImage]

# now we can define our thumbnail spec
class PhotoThumbSlide( ImageSpec ):
    access_as = 'blogthumb'
    pre_cache = False
    processors = [BlogThumb]


class MainThumbnail( ImageSpec ):
    access_as = 'mainthumb'
    pre_cache = False
    processors = [MainThumb]

class MainMiniThumbnail( ImageSpec ):
    access_as = 'mainminithumb'
    pre_cache = False
    processors = [MainMiniThumb, EnchanceThumb]

class ThinThumbnail( ImageSpec ):
    access_as = 'thinthumb'
    pre_cache = False
    processors = [ThinThumb, EnchanceThumb]

class WidgetThumbnail( ImageSpec ):
    access_as = 'widgetethumb'
    pre_cache = False
    processors = [WidgetImage, EnchanceThumb]


class NewsThumbnail( ImageSpec ):
    access_as = 'newsthumb'
    pre_cache = False
    processors = [NewsThumb]
    
class RightColumnThumbnail( ImageSpec ):
    access_as = 'rightcolumnthumb'
    pre_cache = False
    processors = [RightColumnThumb]
