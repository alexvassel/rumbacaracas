from django.shortcuts import render_to_response, get_object_or_404, redirect
from main.models import Slide
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to, json_view
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from datetime import *;
from dateutil.relativedelta import *

@render_to( 'main/index.html' )
def index( request ):

    slides = Slide.objects.published_slides().order_by( '?' )[:4]

    return {'slides': slides}

