#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from events.models import EventCategory
import legacy.models as L
from locations.models import LocationMusic, Location, LocationArea

import os, glob, string, re, sys
from datetime import datetime, timedelta

write = sys.stdout.write

def get_user_id ():
    pass

def compile_date ( day, month, year ,dt = False):
    if year and month and day:
        try:
            date = datetime( int(year), int(month), int(day) )
        except ValueError:
            date = datetime( int(year), int(month), int(day)-1 )
    else:
        date = None

    return date

def convert_status ( oldstatus ):
    return oldstatus


def parse_city_area (value):

    result = {
        u'': None,
        u'Bogota / 82 y Calle T': 1,
        u'Bogota / 93 y Chico': 2,
        u'Bogota / Centro': 3,
        u'Bogota / Chapineros': 4,
        u'Bogota / Fuera de la Ciudad': 5,
        u'Bogota / Macarena': 6,
        u'Bogota / Norte': 7,
        u'Bogota / Occidente': 8,
        u'Bogota / Usaquén': 9,
        u'Bogota / Zona G y Quinta Camacho': 10,
        u'Bogota / Tuesaquillo y La Soledad': 11
        u'Bogota / 72': 12
    }[unicode(value).strip()]

    if result:
        result = LocationArea.objects.get(pk=result)

    return 'Bogota', result,



def not_empty_or_null( value ):
    if not value:
        return None

def parse_people_category ( input_value ):
    result = {
        "": None,
        "Discos y Bares": 'clubs',
        "Eventos y Conciertos": 'concerts',
        "Fashion": 'fashion',
        "Lanzamiento": 'launches',
        "Rumbas": 'rumbas',
    }[input_value]

    return result



def parse_location_type(token):
    types = token.split(";");
    id_list = list()
    for type in types:
        if type:
            type_id = {
                "Bar": 2,
                u'Café': 3,
                "Centro Cultural / Museo": 7,
                "Club Privado": 4,
                "Discoteca": 1,
                "Lounge": 2,
                "Restaurant": 11,
            }[type]
            id_list.append(type_id)
    return id_list

def get_user_instance (user_id):
    return User.objects.get(pk=user_id)


def compile_news_content (content, subtitle, additional_image):

    if subtitle:
        content +=  '<p><strong>%s</strong></p>' % (subtitle,)

    if additional_image:
        content +=  '<p><img src="%s" /></p>' % (additional_image.image.url,)

    return content


def detect_news_category (table):
    category = 5 #blog
    if table is L.Entrevista:
        category = 4 #interviews
    if table is L.Especial:
        category = 3 # Actualidad
    if table is L.MusicNews:
        category = 2 #music news
    if table is L.RumbaNews:
        category = 1 #rumba news

    return category

def parse_location_music ( input_value ):
    result = {
        "": None,
        "Ambiental / Chill-Out": 2,
        "Bailable Latina": 10,
        u'Electrónica': 4,
        "Jazz / Blues": 5,
        "Mariachis": 6,
        "Pop / Rock": 7,
        "Reggae / Ska": 8,
        "Salsa Cabilla": 10,
        "Variada" : 12,
    }[input_value]
    if result:
        result = LocationMusic.objects.get(pk=result)

    return result





def parse_location_food(token):
    types = token.split(";");
    id_list = list()
    #Check if not empty
    for type in types:
        if type:
            type_id = {
                "Americano" : 2,
                "Tasca" : 14,
                u'Árabe': 3,
                "Carnes": 7,
                "Chino": 8,
                u'Comida Rápida' : 20,
                "Criollo": 10,
                u'Español' : 14,
                "Internacional": 20,
                "Italiano": 22,
                u'Marisquería' : 25,
                u'Mediterráneo' : 26,
                "Mejicano": 27,
                "Pizzeria": 29,
                "Vegetariano": 34,
            }[type]
            if type_id:
                id_list.append(type_id)
    return id_list


def parse_event_weekday(token):
    days = token.split(";");
    id_list = list()
    #Check if not empty
    for day in days:
        if day:
            type_id = {
                "Lunes":0,
                "Martes":1,
                u'Miércoles':2,
                "Jueves":3,
                "Viernes":4,
                u'Sábados':5,
                "Domingos":6,
            }[day]
            id_list.append(type_id)
    return id_list


def parse_location ( input_value ):
    result = None
    if input_value:
        try:
            result = Location.objects.get(pk=input_value)
        except:
            pass
    return result



def parse_event_category ( input_value ):
    result = {
        "": None,
        u'Adulto Contemporáneo': 1,
        "Arte y Cultura": 4,
        "Conciertos y Bandas":3,
        u'Electrónica y DJs':2,
        "En Ambiente": 7,
        u'Eventos y Más': 1,
        "Promociones": 6,
        "Rumbas": 5,
    }[input_value]
    #TODO check cevent category for empty
    if result:
        result = EventCategory.objects.get(pk=result)
    else:
        result = EventCategory.objects.get(pk=5)
    return result

def parse_event_time(hours):
    if hours:
        hours + ':00'
    else:
        return None



def parse_old_sex(sex):
    if sex == 1:
        return 'male'
    else:
        return 'female'



def truncate( value, length ):
    """
    Truncates a string after a given number of chars
    return abbr with title
    Argument: Number of chars to truncate after
    """
    if not isinstance( value, basestring ):
        value = str( value )
    if ( len( value ) > length ):
        return value[:length] + "..."
    else:
        return value

