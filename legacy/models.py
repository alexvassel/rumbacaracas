# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Tusfotos(models.Model):
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    archivo = models.CharField(max_length=750)
    usuario = models.CharField(max_length=750)
    leyenda = models.CharField(max_length=750)
    visitas = models.BigIntegerField()
    status = models.IntegerField()
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=750)
    thumbnail = models.TextField()
    day = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'tusfotos'

class TusfotosFotos(models.Model):
    nick = models.CharField(max_length=450, blank=True)
    archivo = models.TextField(blank=True)
    nombre = models.TextField(blank=True)
    status = models.CharField(max_length=6)
    cat = models.CharField(max_length=6)
    id = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'tusfotos_fotos'

class TusfotosVideos(models.Model):
    nick = models.CharField(max_length=450, blank=True)
    video = models.TextField(blank=True)
    nombre = models.TextField(blank=True)
    status = models.CharField(max_length=6)
    id = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=9)
    fecha = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'tusfotos_videos'



class Usuarios(models.Model):
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    telefono_contacto = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    direccion = models.TextField()
    estado = models.CharField(max_length=300)
    codigo_postal = models.CharField(max_length=300)
    dia = models.CharField(max_length=300)
    mes = models.CharField(max_length=300)
    ano = models.CharField(max_length=300)
    sexo = models.CharField(max_length=300)
    pais = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=300)
    codigo = models.CharField(max_length=300)
    celular = models.CharField(max_length=300)
    user = models.CharField(max_length=300)
    pass_field = models.CharField(max_length=300, db_column='pass') # Field renamed because it was a Python reserved word.
    directorio = models.CharField(max_length=300)
    status = models.IntegerField()
    dia2 = models.IntegerField()
    mes2 = models.IntegerField()
    ano2 = models.IntegerField()
    comentario = models.TextField()
    youtube = models.TextField()
    stars = models.IntegerField()
    imagen_principal = models.TextField()
    imagen_original = models.TextField()
    nick = models.CharField(max_length=300)
    me_gusta = models.TextField()
    edad = models.CharField(max_length=300)
    cumpleanos = models.CharField(max_length=300)
    estatus = models.TextField()
    estoy_buscando = models.TextField()
    me_encuentro_en = models.TextField()
    sobre_mi = models.TextField()
    quisiera_conocer = models.TextField()
    intereses = models.TextField()
    musica_favorita = models.TextField()
    artistas = models.TextField()
    peliculas_favoritas = models.TextField()
    avatar = models.CharField(max_length=300)
    feat = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    nivel = models.CharField(max_length=6)
    fecharegistro = models.DateTimeField()
    facebook_id = models.CharField(max_length=150)
    twitter_id = models.CharField(max_length=150)
    class Meta:
        db_table = u'usuarios'

class Fotos(models.Model):
    titulo = models.CharField(max_length=750)
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    ciudad = models.CharField(max_length=750)
    categoria = models.CharField(max_length=750)
    lugar = models.CharField(max_length=750)
    reportero = models.CharField(max_length=750)
    email = models.CharField(max_length=750)
    resena = models.TextField()
    directorio = models.CharField(unique=True, max_length=255)
    imagen1 = models.CharField(max_length=750)
    imagen2 = models.CharField(max_length=750)
    imagen_principal = models.CharField(max_length=750)
    s_picts = models.CharField(max_length=750)
    u_picts = models.CharField(max_length=750)
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    fecha = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'fotos'

class Local(models.Model):
    nombre = models.CharField(max_length=750)
    tipo = models.CharField(max_length=750)
    restaurant = models.TextField()
    direccion = models.CharField(max_length=750)
    ciudad = models.CharField(max_length=750)
    telefono = models.CharField(max_length=750)
    fax = models.CharField(max_length=750)
    url = models.CharField(max_length=750)
    email = models.CharField(max_length=750)
    horario = models.CharField(max_length=750)
    ambiente = models.CharField(max_length=750)
    musica = models.CharField(max_length=750)
    dj = models.CharField(max_length=750)
    vestuario = models.CharField(max_length=750)
    capacidad = models.CharField(max_length=750)
    descripcion = models.TextField()
    cerveza_nacional = models.CharField(max_length=750)
    cerveza_importada = models.CharField(max_length=750)
    trago_nacional = models.CharField(max_length=750)
    trago_importado = models.CharField(max_length=750)
    whisky_nacional = models.CharField(max_length=750)
    whisky_importado = models.CharField(max_length=750)
    otros_tragos = models.CharField(max_length=750)
    prom_lun_vie = models.CharField(max_length=750)
    prom_lun = models.CharField(max_length=750)
    prom_mar = models.CharField(max_length=750)
    prom_mie = models.CharField(max_length=750)
    prom_jue = models.CharField(max_length=750)
    prom_vie = models.CharField(max_length=750)
    prom_sab = models.CharField(max_length=750)
    prom_dom = models.CharField(max_length=750)
    prom_info = models.CharField(max_length=750)
    prog_lun_vie = models.CharField(max_length=750)
    prog_lun = models.CharField(max_length=750)
    prog_mar = models.CharField(max_length=750)
    prog_mie = models.CharField(max_length=750)
    prog_jue = models.CharField(max_length=750)
    prog_vie = models.CharField(max_length=750)
    prog_sab = models.CharField(max_length=750)
    prog_dom = models.CharField(max_length=750)
    prog_info = models.CharField(max_length=750)
    especialidades = models.CharField(max_length=750)
    platos = models.CharField(max_length=750)
    comentarios = models.CharField(max_length=750)
    dia = models.CharField(max_length=750)
    mes = models.CharField(max_length=750)
    ano = models.CharField(max_length=750)
    imagen = models.CharField(max_length=750)
    gerente = models.CharField(max_length=750)
    contacto = models.CharField(max_length=750)
    actualizaciones = models.CharField(max_length=750)
    telefonosc = models.CharField(max_length=750)
    emailc = models.CharField(max_length=750)
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    user = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    discoteca = models.CharField(max_length=6, blank=True)
    lounge = models.CharField(max_length=6, blank=True)
    rest = models.CharField(max_length=6, blank=True)
    bar = models.CharField(max_length=6, blank=True)
    cafe = models.CharField(max_length=6, blank=True)
    club = models.CharField(max_length=6, blank=True)
    cultural = models.CharField(max_length=6, blank=True)
    webcast = models.TextField(blank=True)
    class Meta:
        db_table = u'local'

class EventosCategorias(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=750, blank=True)
    class Meta:
        db_table = u'eventos_categorias'

class Eventos(models.Model):
    titulo = models.CharField(max_length=750)
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=18)
    dia2 = models.CharField(max_length=6)
    mes2 = models.CharField(max_length=6)
    ano2 = models.CharField(max_length=18)
    dias = models.CharField(max_length=750)
    categoria = models.CharField(max_length=750)
    imagen = models.CharField(max_length=750)
    vestuario = models.CharField(max_length=750)
    entrada = models.CharField(max_length=750)
    direccion = models.CharField(max_length=750)
    local = models.CharField(max_length=750)
    url = models.CharField(max_length=750)
    email = models.CharField(max_length=750)
    jerarquia = models.IntegerField()
    descripcion = models.TextField()
    hora = models.CharField(max_length=6)
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    localn = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    inicio = models.DateField(null=True, blank=True)
    fin = models.DateField(null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    otrolugar = models.TextField()
    otrociudad = models.TextField()
    usuario = models.CharField(max_length=150, blank=True)
    tuticket = models.CharField(max_length=6, blank=True)
    status = models.CharField(max_length=6, blank=True)
    evento_id = models.CharField(max_length=150)
    propietario_nombre = models.CharField(max_length=150)
    propietario_id = models.CharField(max_length=150)
    class Meta:
        db_table = u'eventos'


class RumbaNews(models.Model):
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    titulo = models.CharField(max_length=750)
    subtitulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    imagen2 = models.CharField(max_length=750)
    titcon = models.CharField(max_length=750)
    contenido = models.TextField()
    info = models.CharField(max_length=750)
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    fecha = models.DateField(null=True, blank=True)
    tags = models.TextField(blank=True)
    plantilla = models.CharField(max_length=60, blank=True)
    imagen3 = models.CharField(max_length=750, blank=True)
    youtube = models.TextField(blank=True)
    usuario = models.TextField(blank=True)
    class Meta:
        db_table = u'rumba_news'

class MusicNews(models.Model):
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    titulo = models.CharField(max_length=750)
    subtitulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    imagen2 = models.CharField(max_length=750)
    titcon = models.CharField(max_length=750)
    contenido = models.TextField()
    info = models.CharField(max_length=750)
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    fecha = models.DateField(null=True, blank=True)
    tags = models.TextField(blank=True)
    plantilla = models.CharField(max_length=60, blank=True)
    imagen3 = models.CharField(max_length=750, blank=True)
    youtube = models.TextField(blank=True)
    usuario = models.TextField(blank=True)
    class Meta:
        db_table = u'music_news'

class Entrevista(models.Model):
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    titulo = models.CharField(max_length=750)
    subtitulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    imagen2 = models.CharField(max_length=750)
    titcon = models.CharField(max_length=750)
    contenido = models.TextField()
    info = models.CharField(max_length=750)
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    fecha = models.DateField(null=True, blank=True)
    tags = models.TextField(blank=True)
    plantilla = models.CharField(max_length=60, blank=True)
    imagen3 = models.CharField(max_length=750, blank=True)
    youtube = models.TextField(blank=True)
    usuario = models.TextField(blank=True)
    class Meta:
        db_table = u'entrevista'


class Especial(models.Model):
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    titulo = models.CharField(max_length=750)
    subtitulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    imagen2 = models.CharField(max_length=750)
    titcon = models.CharField(max_length=750)
    contenido = models.TextField()
    info = models.CharField(max_length=750)
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    fecha = models.DateField(null=True, blank=True)
    tags = models.TextField(blank=True)
    plantilla = models.CharField(max_length=60, blank=True)
    imagen3 = models.CharField(max_length=750, blank=True)
    youtube = models.TextField(blank=True)
    usuario = models.TextField(blank=True)
    class Meta:
        db_table = u'especial'


class Dj(models.Model):
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    titulo = models.CharField(max_length=750)
    subtitulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    imagen2 = models.CharField(max_length=750)
    titcon = models.CharField(max_length=750)
    contenido = models.TextField()
    info = models.CharField(max_length=750)
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    int = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    fecha = models.DateField(null=True, blank=True)
    tags = models.TextField(blank=True)
    plantilla = models.CharField(max_length=60, blank=True)
    imagen3 = models.CharField(max_length=750, blank=True)
    youtube = models.TextField(blank=True)
    usuario = models.TextField(blank=True)
    class Meta:
        db_table = u'dj'