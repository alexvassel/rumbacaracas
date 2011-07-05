# legacy/management/commands/importlegacydb.py

from django.core.management.base import NoArgsCommand
import legacy.models as L
import people.models as P
import locations.models as LS
import events.models as E
import yourphotos.models as YP
import zinnia.models as Z
import news.models as N

from django.utils.html import strip_tags
from locations.templatetags.tools import truncate

from datetime import datetime, timedelta
from django.core.files.base import ContentFile

from django.conf import settings
from django.template.defaultfilters import slugify

import os, glob, string, re, sys
from utils import *



def import_yourphotos ():

    oldphotos = L.Tusfotos.objects.all()

    #TODO probably it will be good to import views count
    #TODO  IMPORT USERS

    for oldphoto in oldphotos:
        photo = YP.Photo(
                      user = 1,
                      description = oldphoto.leyenda,
                      status = convert_status( oldphoto.status ),
                      datetime_added = compile_date( oldphoto.dia, oldphoto.mes, oldphoto.ano )
                      )

        fi_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/' + oldphoto.archivo, 'r' ).read() )
        photo.image.save( oldphoto.archivo, fi_content, save = False )
        photo.save()



def import_events ():

    oldevents = L.Eventos.objects.all()
    for oldevent in oldevents:
        oldevent = L.Eventos()
        event = E.Event(
            title = oldevent.titulo,
            slug = slugify(oldevent.titulo),
            from_date = compile_date(oldevent.dia, oldevent.mes, oldevent.ano),
            to_date = compile_date(oldevent.dia2, oldevent.mes2, oldevent.ano2),
            repeat = parse_event_weekday(oldevent.dias),
            category = parse_event_category(oldevent.categoria),
            #ignored vestuario
            time = parse_event_time(oldevent.hora),
            price = oldevent.entrada,
            address = oldevent.direccion,
            #TODO carefully import locations
            location = oldevent.local,
            #music
            #area
            place = oldevent.localn,
            #city
            #phone
            url = oldevent.url,
            email = oldevent.email,
            position = oldevent.jerarquia,
            user = oldevent.usuario,
            description = oldevent.descripcion,
            status = 1,
            datetime_added = compile_date(oldevent.da, oldevent.ma, oldevent.aa),
        )
        
        #TODO Investigate where main image is
        ei_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldevent.imagen, 'r' ).read() )
        event.image.save( oldevent.imagen, ei_content, save = False )
        event.save()




def import_blog_category (table):

    oldarticles = table.objects.all()

    for oldarticle in oldarticles:
        oldarticle = L.MusicNews()
        article = Z.Entry(
            title = oldarticle.titulo,
            #Ignore titcone
            categories = list(detect_news_category(table)),
            slug = slugify(oldarticle.titulo),
            status = Z.PUBLISHED,
            creation_date = compile_date(oldarticle.da, oldarticle.ma, oldarticle.aa),
            last_update = compile_date(oldarticle.du, oldarticle.mu, oldarticle.au),
            start_publication = compile_date(oldarticle.dia, oldarticle.mes, oldarticle.ano),
            #TODO carefully import sites
            sites = 1,
            short = truncate( strip_tags( oldarticle.contenido ), 100 ),
            source = oldarticle.info,
            #author
        )
        #import one photo as main, insert other in bottom
        additional_image = false
        if oldarticle.imagen1:
            bi_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldarticle.imagen1, 'r' ).read() )
            article.image.save( oldarticle.imagen1, bi_content, save = False )
            if oldarticle.imagen2:
                #Add second image as external
                article.save()
                additional_image = N.EntryImage(entry=article)
                bii_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldarticle.imagen2, 'r' ).read() )
                additional_image.image.save( oldarticle.imagen2, bii_content, save = False )
        elif oldarticle.imagen2:
            bi_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldarticle.imagen2, 'r' ).read() )
            article.image.save( oldarticle.imagen2, bi_content, save = False )

        #Import subtitle as part of content!!!!!!
        article.content = compile_news_content(oldarticle.contenido,oldarticle.subtitulo, additional_image),
        article.save()


def import_locations ():

    oldlocations = L.Local.objects.all()
    for oldlocation in oldlocations:
        oldlocation = L.Local()
        location = LS.Location(
            title = oldlocation.nombre,
            slug = slugify(oldlocation.nombre),
            type = parse_location_type(oldlocation.tipo),
            restaurant = parse_location_food(oldlocation.restaurant),
            address = oldlocation.direccion,
            city = oldlocation.ciudad,
            #district
            phone_1 = oldlocation.telefono,
            #phone_2
            fax = oldlocation.fax,
            url = oldlocation.url,
            email = oldlocation.email,
            hours_of_operation = oldlocation.horario,
            
            #days_of_operation
            #area
            # Ignored oldlocation.ambiente
            # Ignored oldlocation.dj
            # Ignored oldlocation.vestuario
            # Ignored oldlocation.capacidad
            #ignored oldlocation.dia, oldlocation.mes, oldlocation.ano
            
            music = parse_location_music(oldlocation.musica),
            description = oldlocation.descripcion,
            owner = oldlocation.gerente,
            contact_type = oldlocation.actualizaciones,
            contact = oldlocation.contacto,
            phones = oldlocation.telefonosc,
            contact_email = oldlocation.emailc,
            status = 1,
            datetime_added = compile_date(oldlocation.da, oldlocation.ma, oldlocation.aa),
        )

        #Import old image

        #TODO Investigate where main image is
        li_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldlocation.imagen, 'r' ).read() )
        location.image_logo.save( oldlocation.imagen, li_content, save = False )
        location.save()




def import_people ():

    oldevents = L.Fotos.objects.all()

    #TODO Carefully import locations
    #TODO Import second date

    for oldevent in oldevents:
        oldevent = L.Fotos()
        event = P.PhotoEvent( 
                    title = oldevent.titulo,
                    slug = slugify( oldevent.titulo ),
                    date = compile_date( oldevent.du, oldevent.mu, oldevent.au ),
                    category = parse_people_category( oldevent.categoria ),
                    article = oldevent.resena,
                    location = not_empty_or_null( oldevent.lugar ),
                    author = oldevent.reportero,
                    author_email = oldevent.email,
                    city = oldevent.ciudad,
                    status = 1,
                    datetime_added = compile_date( oldevent.dia, oldevent.mes, oldevent.ano ),
                  )

        #TODO Investigate where main image is
        ei_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldevent.imagen_principal, 'r' ).read() )
        event.image.save( oldevent.imagen_principal, ei_content, save = False )

        #Then import images

        os.chdir( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldevent.directorio )

        images_list = list()

        #TODO Investigate where description is

        legends = list()

        def byNumbers( str ):
            g = re.search( r'_(\d+)\.jpg', str )
            return int( g.group( 1 ) )

        thumb_list = sorted( glob.glob( '*_peq_*.jpg' ) , key = byNumbers )

        for thumb in thumb_list:
            image_file = string.replace( thumb, '_peq_', '_big_' )
            images_list.append( image_file )
            legends.append ( '' )

        for photo in zip( legends, images_list, thumb_list ) :
            p = P.Photo( description = photo[0], event = event )

            fi_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldevent.directorio + '/' + photo[1], 'r' ).read() )
            ft_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldevent.directorio + '/' + photo[2], 'r' ).read() )

            p.image.save( photo[1], fi_content, save = False )
            p.thumb.save( photo[2], ft_content, save = False )

            p.save()
        event.save()


class Command( NoArgsCommand ):
    help = "Import data from legacy db."

    def handle_noargs( self, **options ):
        """
        Read data from legacy db to new db.
        """
        print "Importing legacy data"

        print "Importing legacy your photos"
        import_yourphotos()

        print "Importing legacy people"
        import_people()

        print "Importing legacy events"
        import_events()

        print "Importing legacy locations"
        import_locations()

        print "Importing legacy rumba news"
        import_blog_category (L.RumbaNews)

        print "Importing legacy music news"
        import_blog_category (L.MusicNews)

        print "Importing legacy interviews"
        import_blog_category (L.Entrevista)

        print "Importing legacy specials"
        import_blog_category (L.Especial)

        print "Done."
