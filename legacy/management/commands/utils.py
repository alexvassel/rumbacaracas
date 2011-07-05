__author__ = 'maksim'


write = sys.stdout.write

def get_user_id ():
    pass

def compile_date ( day, month, year ):
    date = datetime( year, month, day )
    return date

def convert_status ( oldstatus ):
    return oldstatus




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
        type_id = {
            "Bar": 2,
            "Café": 3,
            "Centro Cultural / Museo": 5,
            "Club Privado": 4,
            "Discoteca": 1,
            "Lounge": 2,
            "Restaurant": 2,
        }[type]
        id_list.append(type_id)
    return id_list

def compile_news_content (content, subtitle, additional_image):

    if subtitle:
        content +=  '<p><strong>%s</strong></p>' % (subtitle,)

    if additional_image:
        content +=  '<p><img src="%s" /></p>' % (additional_image.image.url,)


def detect_news_category (table):
    category = 5 #blog
    if table is L.Entrevista:
        category = 4 #interviews
    if table is L.Especial:
        category = 5 #?????
    if table is L.MusicNews:
        category = 2 #music news
    if table is L.RumbaNews:
        category = 1 #rumba news

    return category

def parse_location_music ( input_value ):
    result = {
        "": None,
        "Ambiental / Chill-Out": 2,
        "Bailable Latina": None,
        "Electrónica": 4,
        "Jazz / Blues": 5,
        "Mariachis": 6,
        "Pop / Rock": 7,
        "Reggae / Ska": 8,
        "Salsa Cabilla": 10,
        "Variada" : 12,
    }[input_value]

    return result





def parse_location_food(token):
    types = token.split(";");
    id_list = list()
    #Check if not empty
    for type in types:
        type_id = {
            "Americano" : 2,
            "Tasca" : None,
            "Árabe": 3,
            "Carnes": 7,
            "Chino": 8,
            "Comida Rápida" : None,
            "Criollo" None,
            "Español" : 14,
            "Internacional": 20,
            "Italiano": 22,
            "Marisquería" : 25,
            "Mediterráneo" : 26,
            "Mejicano": 27,
            "Pizzeria": 29,
            "Vegetariano": 34,
        }[type]
        id_list.append(type_id)
    return id_list


def parse_event_weekday(token):
    days = token.split(";");
    id_list = list()
    #Check if not empty
    for days in days:
        type_id = {
            "Lunes":0,
            "Martes":1,
            "Miércoles":2,
            "Jueves":3,
            "Viernes":4,
            "Sábados":5,
            "Domingos":6,
        }[type]
        id_list.append(type_id)
    return id_list


def parse_event_category ( input_value ):
    result = {
        "": None,
        "Adulto Contemporáneo": None,
        "Arte y Cultura": 4,
        "Conciertos y Bandas":3,
        "Electrónica y DJs":2,
        "En Ambiente": None,
        "Eventos y Más": None,
        "Promociones": None,
        "Rumbas": 5,
    }[input_value]
    return result

def parse_event_time(hours):
    if hours:
        hours + ':00'
    else:
        return None