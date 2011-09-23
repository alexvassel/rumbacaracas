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
import yourvideos.models as YV

import django.contrib.auth.models as DU

from django.utils.html import strip_tags

from datetime import datetime, timedelta
from django.core.files.base import ContentFile

from django.conf import settings
from django.template.defaultfilters import slugify
from main.modelFields import SlugifyUniquely

import os, glob, string, re, sys
from utils import *
from progress import ProgressBar


def hack_for_user_id(id):
    if id in (1, "1") :
        return 5000
    else:
        return id

def import_users ():

    DU.User.objects.all().exclude(username="admin").delete()
    oldusers = L.Usuarios.objects.all()

    prog = ProgressBar(0, len(oldusers), mode='fixed')
    e_list = list()

    for olduser in oldusers:
        prog.increment_amount()
        print prog, '\r',
        sys.stdout.flush()

        user = DU.User(
            id = hack_for_user_id(olduser.id),
            first_name = olduser.nombre[:30],
            last_name = olduser.apellido[:30],
            username = olduser.user[:30],
            email = olduser.email
        )
        user.set_password(olduser.pais)
        try :
            user.save()
            user.groups.add(1)
        except Exception, e:
            e_list.append(e)
            pass#print e

    print e_list



def import_subscriptions ():

    S.User.objects.all().delete()
    oldusers = L.Usuarios.objects.all()

    for olduser in oldusers[0:10]:
        user = S.User(
            first_name = olduser.nombre,
            last_name = olduser.apellido,
            sex = parse_old_sex (olduser.sexo),
            #birthday = olduser.cumpleanos,
            country = olduser.pais,
            city = olduser.ciudad,
            email = olduser.email,
            status = 1
        )
        user.save()



def import_yourphotos ():

    YP.Photo.objects.all().delete()
    oldphotos = L.TusfotosFotos.objects.all()

    wrong_ids = list()

    prog = ProgressBar(0, len(oldphotos), mode='fixed')

    for oldphoto in oldphotos:

        prog.increment_amount()
        print prog, '\r',
        sys.stdout.flush()


        user = get_user_instance_by_name(oldphoto.nick)
        if user:
            photo = YP.Photo(
                          user = user,
                          description = oldphoto.nombre,
                          category = parse_photo_category(oldphoto.cat),
                          status = convert_status( oldphoto.status ),
                          datetime_added = oldphoto.fecha
                          )


            if oldphoto.archivo:
                #   "http://www.rumbacaracas.com/tusfotos/" . substr($foto_nick,0,1) . "/" . $foto_nick. "/" . $foto_id . "/" . hacer_link($foto_titulo,'') . "/" . $foto_archivo

                file_name = settings.OLDDATABOGOTA_PHOTO_PATH + 'tusfotos/' + string.lower(oldphoto.nick)[0:1] + '/' + string.lower(oldphoto.nick) + '/' + str(oldphoto.id) + '/' + hacer_link(oldphoto.nombre) + '/' + oldphoto.archivo

                if os.path.isfile(file_name):
                    fi_content = ContentFile( open( file_name, 'r' ).read() )
                    photo.image.save( oldphoto.archivo[-75:], fi_content, save = False )
                    photo.save()
                    photo.datetime_added = oldphoto.fecha
                    photo.save()
                else:
                    #print "wrong file for yourphotos!!!!!!!!!!\n"
                    #print file_name
                    wrong_ids.append(str(oldphoto.id))

    if wrong_ids:
        print ",".join(wrong_ids)



def import_yourvideos ():

    YV.Video.objects.all().delete()
    oldvideos = L.TusfotosVideos.objects.all()

    prog = ProgressBar(0, len(oldvideos), mode='fixed')

    for oldvideo in oldvideos:

        prog.increment_amount()
        print prog, '\r',
        sys.stdout.flush()

        video = YV.Video(
                      user = get_user_instance_by_name(oldvideo.nick),
                      youtube_id = oldvideo.video,
                      description = oldvideo.nombre,
                      status = convert_status( oldvideo.status )
        )
        video.save()
        video_datetime_added = oldvideo.fecha
        if video_datetime_added:
            video.datetime_added = video_datetime_added
        video.save()




def import_events ():

    E.EventCategory.objects.all().delete()
    oldeventscats = L.EventosCategorias.objects.all()

    for oldeventcat in oldeventscats:
        eventcat = E.EventCategory(
            id = oldeventcat.id,
            title = oldeventcat.nombre
        )
        eventcat.save()



    E.Event.objects.all().delete()

    oldevents = L.Eventos.objects.all()

    prog = ProgressBar(0, len(oldevents), mode='fixed')

    for oldevent in oldevents:

        prog.increment_amount()
        print prog, '\r',
        sys.stdout.flush()

        #oldevent = L.Eventos()
        if oldevent.titulo:
            if len(oldevent.email) > 75:
                oldevent.email = oldevent.email[:75]
            event = E.Event(
                title = oldevent.titulo,

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
                datetime_added = compile_date(oldevent.da, oldevent.ma, oldevent.aa)
            )
            
            event.slug = SlugifyUniquely(oldevent.titulo[:50], event.__class__)

            if oldevent.url:
                event.url = 'http://' + oldevent.url

            #TODO Investigate where main image is



            if oldevent.imagen:
                file_name = settings.OLDDATABOGOTA_PHOTO_PATH + 'eventos/pics/' + oldevent.imagen
                if os.path.isfile(file_name):
                    ei_content = ContentFile( open( file_name, 'r' ).read() )
                    event.image.save( oldevent.imagen, ei_content, save = False )
                else:
                    print "wrong file for event!!!!!!!!!!\n"
                    print oldevent.titulo + "\n"
            event.save()

            event_datetime_added = compile_date(oldevent.da, oldevent.ma, oldevent.aa)
            if event_datetime_added:
                event.datetime_added = event_datetime_added

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

    wrong_ids = list()

    prog = ProgressBar(0, len(oldarticles), mode='fixed')
    for oldarticle in oldarticles:

        prog.increment_amount()
        print prog, '\r',
        sys.stdout.flush()


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

            

            last_update = oldarticle.fecha #compile_date(oldarticle.du, oldarticle.mu, oldarticle.au)
            creation_date = oldarticle.fecha #compile_date(oldarticle.da, oldarticle.ma, oldarticle.aa)
            start_publication = compile_date(oldarticle.dia, oldarticle.mes, oldarticle.ano)

            if not creation_date:
                creation_date = start_publication

            if last_update:
                article.last_update = last_update

            if creation_date:
                article.creation_date = creation_date

            if start_publication:
                article.start_publication = start_publication

            #import one photo as main, insert other in bottom
            additional_image = False
            image_name = oldarticle.imagen1
            if oldarticle.imagen2:
                image_name = oldarticle.imagen2






            if image_name:
                file_name = settings.OLDDATABOGOTA_PHOTO_PATH + 'contenido/pics/' + image_name
                if os.path.isfile(file_name):
                    #bi_content = ContentFile( open( settings.FAKE_IMPORT_IMAGE, 'r' ).read() )
                    bi_content = ContentFile( open( file_name, 'r' ).read() )
                    article.image.save( image_name, bi_content, save = False )
                else:
                    #print "Wrong file "
                    #print file_name
                    wrong_ids.append(oldarticle.id)

            #Import subtitle as part of content!!!!!!
            article.content = compile_news_content(oldarticle.contenido,oldarticle.subtitulo, additional_image)
            article.save()
            article.categories.add(detect_news_category(table))
            #TODO carefully import sites
            article.sites.add(1)

    print wrong_ids


def import_locations ():

    LS.Location.objects.all().delete()

    oldlocations = L.Local.objects.all()
    wrong_ids = list()

    prog = ProgressBar(0, len(oldlocations), mode='fixed')

    for oldlocation in oldlocations:

        prog.increment_amount()
        print prog, '\r',
        sys.stdout.flush()

        #oldlocation = L.Local()1

        location = LS.Location(
            id = oldlocation.id,
            title = oldlocation.nombre,
            #slug = slugify(oldlocation.nombre),

            address = oldlocation.direccion,

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

        location.slug = SlugifyUniquely(oldlocation.nombre, location.__class__)

        location.city, location.area = parse_city_area(oldlocation.ciudad)



        if oldlocation.url:
            location.url = 'http://' + oldlocation.url

        #Import old image

        #TODO Investigate where main image is
        #li_content = ContentFile( open( settings.FAKE_IMPORT_IMAGE, 'r' ).read() )

        if oldlocation.imagen:
            file_name = settings.OLDDATABOGOTA_PHOTO_PATH + 'locales/pics/' + oldlocation.imagen
            if os.path.isfile(file_name):
                li_content = ContentFile( open( file_name, 'r' ).read() )
                location.image_logo.save( oldlocation.imagen, li_content, save = False )
            else:
                #print "wrong file for location!!!!!!!!!!\n"
                #print file_name + "\n"
                wrong_ids.append(str(oldlocation.id))

        location.save()
        location_datetime_added = compile_date(oldlocation.da, oldlocation.ma, oldlocation.aa)
        if location_datetime_added:
            location.datetime_added = location_datetime_added
        location.save()

        location.restaurant.add(*parse_location_food(oldlocation.restaurant))
        location.type.add(*parse_location_type(oldlocation.tipo))

    if wrong_ids:
        print ",".join(wrong_ids)


def reimport_people_locations ():
    oldevents = L.Fotos.objects.all()
    for oldevent in oldevents:
        try :
            event = P.PhotoEvent.objects.get(
                title = oldevent.titulo,
                category = parse_people_category( oldevent.categoria ),
                author = oldevent.reportero,
                author_email = oldevent.email,
                city = oldevent.ciudad,
                date = compile_date( oldevent.dia, oldevent.mes, oldevent.ano )
            )
            print "Found"
            print not_empty_or_null( oldevent.lugar )
            print oldevent.lugar
            event.location = not_empty_or_null( oldevent.lugar )
            event.save()
        except P.PhotoEvent.DoesNotExist:
            print oldevent.titulo
        except Exception, e:
            print e

        
def import_people ():

    P.PhotoEvent.objects.all().delete()

    oldevents = L.Fotos.objects.all().order_by('-fecha')

    #TODO Carefully import locations
    #TODO Import second date

    prog = ProgressBar(0, len(oldevents[0:500]), mode='fixed')
    wrong_locations = list()
    all_locations = list()

    for oldevent in oldevents[0:500]:

        try:

            prog.increment_amount()
            print prog, '\r',
            sys.stdout.flush()

            if oldevent.titulo:
                #oldevent = L.Fotos()

                eve_datetime_added = compile_date( oldevent.da, oldevent.ma, oldevent.aa ) or oldevent.fecha

                old_location = not_empty_or_null( oldevent.lugar )
                
                if oldevent.lugar:
                    try:
                        all_locations.append(int(oldevent.lugar))
                    except Exception, e:
                        all_locations.append(oldevent.lugar)


                if oldevent.lugar and not old_location:
                    try:
                        wrong_locations.append(int(oldevent.lugar))
                    except Exception, e:
                        wrong_locations.append(oldevent.lugar)





                event = P.PhotoEvent(
                            title = oldevent.titulo,
                            #slug = slugify( oldevent.titulo )[:50],

                            category = parse_people_category( oldevent.categoria ),
                            article = oldevent.resena,
                            location = old_location,
                            author = oldevent.reportero,
                            author_email = oldevent.email,
                            city = oldevent.ciudad,
                            status = 1,
                            datetime_added = eve_datetime_added
                          )

                event.slug = SlugifyUniquely(oldevent.titulo[:50], event.__class__)

                people_date = compile_date( oldevent.dia, oldevent.mes, oldevent.ano )
                if people_date:
                    event.date = people_date
                elif eve_datetime_added:
                    event.date = eve_datetime_added

                #TODO Investigate where main image is
                #ei_content = ContentFile( open( settings.FAKE_IMPORT_IMAGE, 'r' ).read() )

                import os

                main_file = settings.OLDDATABOGOTA_PHOTO_PATH + 'fotos/pics/' + oldevent.directorio + '/' +  oldevent.imagen_principal
                basename, extension = os.path.splitext(oldevent.imagen_principal)
                from PIL import Image

                #MEDIA_ROOT
                if extension == '.gif':
                    new_dir = settings.MEDIA_ROOT + '/image_cache/people_fotos_convert/' + oldevent.directorio + ''
                    new_file =  new_dir +  basename + '.jpg'
                    if not os.path.isdir(new_dir):
                        os.makedirs(new_dir)
                    Image.open(main_file).convert('RGB').save(new_file)
                    main_file = new_file
                    oldevent.imagen_principal = basename + '.jpg'

                if os.path.isfile(main_file):
                    ei_content = ContentFile( open( main_file, 'r' ).read() )
                    event.image.save( oldevent.imagen_principal, ei_content, save = False )

                event.save()

                if eve_datetime_added:
                    event.datetime_added = eve_datetime_added
                    event.save()

                #Then import images

                os.chdir( settings.OLDDATABOGOTA_PHOTO_PATH + 'fotos/pics/' + oldevent.directorio )

                images_list = list()

                legends_file = settings.OLDDATABOGOTA_PHOTO_PATH + 'fotos/pics/' + oldevent.directorio + '/resena.dat'
                if os.path.isfile(legends_file):
                    legends = open( legends_file, "r" ).readlines()
                else:
                    legends = list()

                fileencoding = "iso-8859-1"

                ulegends = list()
                for legend in legends:
                    ulegends.append(legend.decode(fileencoding))


                def byNumbers( str ):
                    g = re.search( r'_(\d+)\.jpg', str )
                    return int( g.group( 1 ) )

                thumb_list = sorted( glob.glob( '*_peq_*.jpg' ) , key = byNumbers )

                for thumb in thumb_list:
                    image_file = string.replace( thumb, '_peq_', '_big_' )
                    images_list.append( image_file )
                    legends.append ( '' )

                for photo in zip( ulegends, images_list, thumb_list ) :
                    p = P.Photo( description = photo[0][:256], event = event, datetime_added = event.datetime_added )

                    fi_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + 'fotos/pics/' + oldevent.directorio + '/' + photo[1], 'r' ).read() )
                    ft_content = ContentFile( open( settings.OLDDATABOGOTA_PHOTO_PATH + 'fotos/pics/' + oldevent.directorio + '/' + photo[2], 'r' ).read() )

                    p.image.save( photo[1][-75:], fi_content, save = False )
                    p.thumb.save( photo[2][-75:], ft_content, save = False )

                    p.save()
                    p.datetime_added = event.datetime_added
                    p.save()
        except Exception, e:
            print "\n"
            print e
            print "\n"

    #print wrong_locations
    #print all_locations



class Command( NoArgsCommand ):
    help = "Import data from legacy db."

    def handle_noargs( self, **options ):
        """
        Read data from legacy db to new db.
        """
        print datetime.now()


        print "\n"
        print "Importing legacy data \n-----------------------------------------------"

        print "Importing legacy users"
        #import_users()


        #print "Importing legacy subscriptions"
        #import_subscriptions()




        print "\nImporting legacy locations"
        #import_locations()

        print "\nImporting legacy events"
        #import_events()

        print "\nImporting legacy people"
        import_people()
        #reimport_people_locations()

        print "\nImporting legacy rumba news"
        #import_blog_category (L.RumbaNews)

        print "\nImporting legacy music news"
        #import_blog_category (L.MusicNews)

        print "\nImporting legacy interviews"
        #import_blog_category (L.Entrevista)

        print "\nImporting legacy specials"
        #import_blog_category (L.Especial)

        #Z.Entry.objects.filter(categories=5).delete()

        print "\nImporting legacy your photos"
        #import_yourphotos()

        print "\nImporting legacy your videos"
        #import_yourvideos()

        print "------------------------------------------------- \nDone."
        print datetime.now()
        print "\n"
