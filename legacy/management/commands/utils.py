#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from events.models import EventCategory
import legacy.models as L
from locations.models import LocationMusic, Location, LocationArea, WeekDay

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

        u"Caracas / Altamira": 1,
        u"Caracas / Alto Prado": 3,
        u"Caracas / Baruta": 3,
        u"Caracas / Bellas Artes": 4,
        u"Caracas / Bello Campo": 5,
        u"Caracas / Campo Alegre": 6,
        u"Caracas / Chacaito": 7,
        u"Caracas / Chacao": 8,
        u"Caracas / Chuao": 9,
        u"Caracas / El Hatillo": 10,
        u"Caracas / El Marqués": 11,
        u"Caracas / El Paraíso": 12,
        u"Caracas / El Rosal": 13,
        u"Caracas / La Boyera": 14,
        u"Caracas / La Candelaria": 15,
        u"Caracas / La Castellana": 16,
        u"Caracas / La Floresta": 17,
        u"Caracas / La Lagunita": 18,
        u"Caracas / La Trinidad": 19,
        u"Caracas / Las Mercedes": 20,
        u"Caracas / Los Caobos": 21,
        u"Caracas / Los Cedros": 22,
        u"Caracas / Los Chaguaramos": 23,
        u"Caracas / Los Cortijos": 24,
        u"Caracas / Los Palos Grandes": 25,
        u"Caracas / Los Ruices": 26,
        u"Caracas / Macaracuay": 27,
        u"Caracas / Parque Central": 28,
        u"Caracas / Plaza Venezuela": 29,
        u"Caracas / Prados del Este": 30,
        u"Caracas / Sabana Grande": 31,
        u"Caracas / San Román": 32,
        u"Caracas / Santa Fé": 33,
        u"Caracas / Santa Mónica": 34,
        u"Caracas / Terrazas del Ávila": 35,
        u"Caracas / Zona Oeste": 36,
        u"Litoral / Playa Grande": 37,
        u"Litoral / Caraballeda": 38,
        u"Gran Caracas / Guatire": 39,
        u"Gran Caracas / San Antonio de los Altos": 40,
        u"Gran Caracas / Guarenas": 41,

    }[unicode(value).strip()]

    city = 'caracas'
    if result in (37,38):
        city = 'Litoral'
    if result in (39,40, 41):
        city = 'Gran Caracas'

    if result:
        result = LocationArea.objects.get(pk=result)

    return city, result,



def not_empty_or_null( value ):
    if not value:
        return None
    try :
        result = Location.objects.get(pk=value)
        return result
    except Location.DoesNotExist:
        return None



def parse_people_category ( input_value ):
    result = {
        "": 'rumbas',
        "Discos y Bares": 'clubs',
        "Eventos y Conciertos": 'concerts',
        "Fashion": 'fashion',
        "Lanzamiento": 'launches',
        "Rumbas": 'rumbas',
        "Fuera de Caracas": 'outside'
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
    try :
        result = User.objects.get(pk=user_id)
        return result
    except User.DoesNotExist:
        return None
    
def get_user_instance_by_name (user_name):
    try :
        result = User.objects.get(username=user_name)
        return result
    except User.DoesNotExist:
        print 'Ignored username - ' + user_name
        return None


def compile_news_content (content, subtitle, additional_image, youtube_url):

    if subtitle:
        content +=  '<p><strong>%s</strong></p>' % (subtitle,)

    if additional_image:
        content +=  '<p><img src="%s" /></p>' % (additional_image.image.url,)

    if youtube_url:
        content += youtube(youtube_url)

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
        u'Criolla Folklórica': None,
        "Metal / Alternativo": 1,
    }[input_value]
    if result:
        result = LocationMusic.objects.get(pk=result)

    return result


def parse_photo_category ( input_value ):

    if input_value in (1,"1"):
        result = 'sexy'
    elif input_value in (2,"2"):
        result = 'amigos'
    elif input_value in (3,"3"):
        result = 'sexy'
    elif input_value in (4,"4"):
        result = 'humor'
    else:
        result = ''

    return result



from django.template.defaultfilters import stringfilter
import re

@stringfilter
def youtube(url):
    regex = re.compile(r"^[^v]+v=(?P<id>.{11}).*")
    match = regex.match(url)
    if not match: return ""
    video_id = match.group('id')
    return """
    <br />
    <object width="425" height="344">
    <param name="movie" value="http://www.youtube.com/v/%s"></param>
    <param name="allowFullScreen" value="true"></param>
    <embed src="http://www.youtube.com/v/%s" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344"></embed>
    </object>
    """ % (video_id, video_id)


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
                #NEW!
                u'Pollo en Brasa': '',
                u'Japonés': 24,
                u'Francés': 15,
                u'Tex-Mex': '',
                u'Hindú': 19,
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
                "Domingo":6,
            }[day]
            real_day = WeekDay.objects.get(value=type_id)
            id_list.append(real_day)
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

    #TODO check cevent category for empty


    if input_value:
        input_value = EventCategory.objects.get(pk=input_value)
    else:
        input_value = EventCategory.objects.get(pk=5)
    return input_value

def parse_event_time(hours):
    if hours:
        hours + ':00'
    else:
        return None



def parse_old_sex(sex):
    if sex == "Masculino":
        return 'male'
    elif sex == "Femenino":
        return 'female'
    else:
        return None



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




def f4(seq):
    # order preserving
    noDupes = []
    [noDupes.append(i) for i in seq if not noDupes.count(i)]
    return noDupes

def is_int_as_str(istr):
    try:
        return str(int(istr)) == istr
    except Exception, e:
        return  False

    
def hacer_link(titulo) :

    str = string.lower(string.strip(titulo))

    str = re.sub(u"[áàâãª]", "a", str)
    str = re.sub(u"[íìî]", "i", str)
    str = re.sub(u"[éèê]", "e", str)
    str = re.sub(u"[óòôõº]", "o", str)
    str = re.sub(u"[úùû]", "u", str)
    str = re.sub(u"[ç]", "c", str)
    str = re.sub(u"[ñ]", "n", str)
    str = re.sub(u"[^0-9^a-z-]", " ", str)
    str = re.sub(u"[0-9]", " ", str)

    convertida = f4(str.split())
    convertida = [word for word in convertida if len(word)>2]
    #convertida = [word for word in convertida if not is_int_as_str(word)]

    convertida = convertida[:7]

    str = "-".join(convertida)

    return str
