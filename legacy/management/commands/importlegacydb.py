# legacy/management/commands/importlegacydb.py

from django.core.management.base import NoArgsCommand
import legacy.models as L
import people.models as P
import locations.models as LS
import events.models as E
import yourphotos.models as YP
import zinnia.models as Z
import news.models as N
import subscribe.models as S

import django.contrib.auth.models as DU

from django.utils.html import strip_tags

from datetime import datetime, timedelta
from django.core.files.base import ContentFile

from django.conf import settings
from django.template.defaultfilters import slugify

import os, glob, string, re, sys
from utils import *



def hack_for_user_id(id):
    if id in (1, "1") :
        return 5000
    else:
        return id

def import_users ():

    DU.User.objects.all().exclude(username="admin").delete()
    oldusers = L.Usuarios.objects.all()

    for olduser in oldusers:

        user = DU.User(
            id = hack_for_user_id(olduser.id),
            first_name = olduser.nombre,
            last_name = olduser.apellido,
            username = olduser.user,
            email = olduser.email
        )
        user.set_password(olduser.pais)
        user.save()
        user.groups.add(1)


def import_subscriptions ():

    S.User.objects.all().delete()
    oldusers = L.EmailsRumbabogota.objects.all()

    for olduser in oldusers:
        user = S.User(
            first_name = olduser.nombre,
            last_name = olduser.apellido,
            company = olduser.compania,
            sex = parse_old_sex (olduser.sexo),
            birthday = olduser.cumpleanos,
            country = olduser.pais,
            city = olduser.ciudad,
            email = olduser.email,
            status = 1
        )
        user.save()





def import_yourphotos ():

    YP.Photo.objects.all().delete()
    oldphotos = L.Tusfotos.objects.all()

    for oldphoto in oldphotos:
        photo = YP.Photo(
                      user = get_user_instance(hack_for_user_id(oldphoto.usuario)),
                      description = oldphoto.leyenda,
                      status = convert_status( oldphoto.status ),
                      datetime_added = compile_date( oldphoto.dia, oldphoto.mes, oldphoto.ano )
                      )

        fi_content = ContentFile( open( settings.FAKE_IMPORT_IMAGE, 'r' ).read() )
        #fi_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/' + oldphoto.archivo, 'r' ).read() )

        photo.image.save( oldphoto.archivo[:-100], fi_content, save = False )
        photo.save()



def import_events ():
    E.Event.objects.all().delete()
    oldevents = L.Eventos.objects.all()
    for oldevent in oldevents:
        #oldevent = L.Eventos()
        if oldevent.titulo:
            if len(oldevent.email) > 75:
                oldevent.email = oldevent.email[:75]
            event = E.Event(
                title = oldevent.titulo,
                slug = slugify(oldevent.titulo)[:50],
                from_date = compile_date(oldevent.dia, oldevent.mes, oldevent.ano),
                to_date = compile_date(oldevent.dia2, oldevent.mes2, oldevent.ano2),

                category = parse_event_category(oldevent.categoria),
                #ignored vestuario
                time = parse_event_time(oldevent.hora),
                price = oldevent.entrada,
                address = oldevent.direccion,
                #TODO carefully import locations
                location = parse_location(oldevent.local),
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

            if oldevent.url:
                event.url = 'http://' + oldevent.url

            #TODO Investigate where main image is

            ei_content = ContentFile( open( settings.FAKE_IMPORT_IMAGE, 'r' ).read() )
            #ei_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldevent.imagen, 'r' ).read() )
            event.image.save( oldevent.imagen, ei_content, save = False )
            event.save()

            event.repeat.add(*parse_event_weekday(oldevent.dias))


def disconnect_zinnia_signals():
    """Disconnect all the signals provided by Zinnia"""
    from zinnia.models import Entry
    from django.db.models.signals import post_save
    
    post_save.disconnect(
        sender=Entry, dispatch_uid='zinnia.entry.post_save.ping_directories')
    post_save.disconnect(
        sender=Entry, dispatch_uid='zinnia.entry.post_save.ping_external_urls')




def import_blog_category (table):

    oldarticles = table.objects.all()

    Z.Entry.objects.filter(categories=detect_news_category(table)).delete()

    disconnect_zinnia_signals()

    for oldarticle in oldarticles:
        #oldarticle = L.MusicNews()
        if oldarticle.titulo:
            title = oldarticle.titulo
        else:
            title = truncate( strip_tags( oldarticle.contenido ), 255 )[:255]
        if title:

            article = Z.Entry(
                title = title,
                #Ignore titcone

                slug = slugify(title),
                status = Z.PUBLISHED,

                short = truncate( strip_tags( oldarticle.contenido ), 100 ),
                source = oldarticle.info,
                #author
            )


            last_update = compile_date(oldarticle.du, oldarticle.mu, oldarticle.au)
            creation_date = compile_date(oldarticle.da, oldarticle.ma, oldarticle.aa)
            start_publication = compile_date(oldarticle.dia, oldarticle.mes, oldarticle.ano)

            if last_update:
                article.last_update = last_update

            if creation_date:
                article.creation_date = creation_date

            if start_publication:
                article.start_publication = start_publication

            #import one photo as main, insert other in bottom
            additional_image = False
            if oldarticle.imagen1:
                bi_content = ContentFile( open( settings.FAKE_IMPORT_IMAGE, 'r' ).read() )
                #bi_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldarticle.imagen1, 'r' ).read() )
                article.image.save( oldarticle.imagen1, bi_content, save = False )
                if oldarticle.imagen2:
                    #Add second image as external
                    article.save()
                    #additional_image = N.EntryImage(entry=article)
                    #bii_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldarticle.imagen2, 'r' ).read() )
                    #additional_image.image.save( oldarticle.imagen2, bii_content, save = False )
            elif oldarticle.imagen2:
                bi_content = ContentFile( open( settings.FAKE_IMPORT_IMAGE, 'r' ).read() )
                #bi_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldarticle.imagen2, 'r' ).read() )
                article.image.save( oldarticle.imagen2, bi_content, save = False )

            #Import subtitle as part of content!!!!!!
            article.content = compile_news_content(oldarticle.contenido,oldarticle.subtitulo, additional_image)
            article.save()
            article.categories.add(detect_news_category(table))
            #TODO carefully import sites
            article.sites.add(1)


def import_locations ():

    LS.Location.objects.all().delete()

    oldlocations = L.Local.objects.all()
    for oldlocation in oldlocations:
        #oldlocation = L.Local()1

        location = LS.Location(
            id = oldlocation.id,
            title = oldlocation.nombre,
            slug = slugify(oldlocation.nombre),

            address = oldlocation.direccion,
            city = oldlocation.ciudad,
            #district
            phone_1 = oldlocation.telefono,
            #phone_2
            fax = oldlocation.fax,

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

        if oldlocation.url:
            location.url = 'http://' + oldlocation.url

        #Import old image

        #TODO Investigate where main image is
        li_content = ContentFile( open( settings.FAKE_IMPORT_IMAGE, 'r' ).read() )
        #li_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldlocation.imagen, 'r' ).read() )
        location.image_logo.save( oldlocation.imagen, li_content, save = False )
        location.save()

        location.restaurant.add(*parse_location_food(oldlocation.restaurant))
        location.type.add(*parse_location_type(oldlocation.tipo))






def import_people ():

    P.PhotoEvent.objects.all().delete()

    oldevents = L.Fotos.objects.all()

    #TODO Carefully import locations
    #TODO Import second date

    for oldevent in oldevents[:20]:
        if oldevent.titulo:
            #oldevent = L.Fotos()
            event = P.PhotoEvent(
                        title = oldevent.titulo,
                        slug = slugify( oldevent.titulo )[:50],

                        category = parse_people_category( oldevent.categoria ),
                        article = oldevent.resena,
                        location = not_empty_or_null( oldevent.lugar ),
                        author = oldevent.reportero,
                        author_email = oldevent.email,
                        city = oldevent.ciudad,
                        status = 1,
                        datetime_added = compile_date( oldevent.da, oldevent.ma, oldevent.aa ),
                      )

            people_date = compile_date( oldevent.dia, oldevent.mes, oldevent.ano )
            if people_date:
                event.date = people_date

            #TODO Investigate where main image is
            ei_content = ContentFile( open( settings.FAKE_IMPORT_IMAGE, 'r' ).read() )
            #ei_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + '/fotos/' + oldevent.imagen_principal, 'r' ).read() )
            event.image.save( oldevent.imagen_principal, ei_content, save = False )

            event.save()
            
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

                p.image.save( photo[1][:-100], fi_content, save = False )
                p.thumb.save( photo[2][:-100], ft_content, save = False )

                p.save()



class Command( NoArgsCommand ):
    help = "Import data from legacy db."

    def handle_noargs( self, **options ):
        """
        Read data from legacy db to new db.
        """
        print "Importing legacy data \n-----------------------------------------------"

        print "Importing legacy users"
        import_users()


        print "Importing legacy subscriptions"
        #import_subscriptions()


        print "Importing legacy people"
        #import_people()

        print "Importing legacy locations"
        #import_locations()

        print "Importing legacy events"
        #import_events()

        print "Importing legacy rumba news"
        #import_blog_category (L.RumbaNews)

        print "Importing legacy music news"
        #import_blog_category (L.MusicNews)

        print "Importing legacy interviews"
        #import_blog_category (L.Entrevista)

        print "Importing legacy specials"
        #import_blog_category (L.Especial)

        print "Importing legacy your photos"
        import_yourphotos()

        print "------------------------------------------------- \nDone."
