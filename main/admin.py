from main.models import  Slide
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class SlideAdmin( admin.ModelAdmin ):
    list_display = ( 'title', 'datetime_added', 'get_is_actual', 'get_is_visible', 'status' )
    list_editable = ( 'status', )
    list_filter = ( 'is_visible', )

    def get_is_actual( self, slide ):
        """Admin wrapper for slide.is_actual"""
        return slide.is_actual
    get_is_actual.boolean = True
    get_is_actual.short_description = _( 'is actual' )

    def get_is_visible( self, slide ):
        """Admin wrapper for slide.is_visible"""
        return slide.is_visible
    get_is_visible.boolean = True
    get_is_visible.short_description = _( 'is visible' )


admin.site.register( Slide, SlideAdmin )
