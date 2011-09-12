# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Archivogaleria(models.Model):
    id = models.IntegerField(primary_key=True)
    articulo = models.IntegerField()
    plantilla = models.TextField()
    archivo = models.TextField()
    titulo = models.TextField(blank=True)
    class Meta:
        db_table = u'ArchivoGaleria'

class Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    class Meta:
        db_table = u'admin'

class Administrador(models.Model):
    nombre = models.CharField(max_length=750)
    apellido = models.CharField(max_length=750)
    user = models.CharField(unique=True, max_length=750)
    pass_field = models.CharField(max_length=750, db_column='pass') # Field renamed because it was a Python reserved word.
    status = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'administrador'

class AdultoContemporaneo(models.Model):
    titulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    pr_link = models.CharField(max_length=750)
    rumba_news_pr = models.CharField(max_length=750)
    music_news_pr = models.CharField(max_length=750)
    entrevista_pr = models.CharField(max_length=750)
    especial_pr = models.CharField(max_length=750)
    dj_mix_pr = models.CharField(max_length=750)
    dj_school_pr = models.CharField(max_length=750)
    que_vida_pr = models.CharField(max_length=750)
    local_pr = models.CharField(max_length=750)
    evento_pr = models.CharField(max_length=750)
    local_se1 = models.CharField(max_length=750)
    evento_se1 = models.CharField(max_length=750)
    local_se2 = models.CharField(max_length=750)
    evento_se2 = models.CharField(max_length=750)
    encuesta = models.CharField(max_length=750)
    evento_fotos = models.CharField(max_length=750)
    imagen_evento = models.CharField(max_length=750)
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    se1_link = models.CharField(max_length=750)
    rumba_news_se1 = models.CharField(max_length=750)
    music_news_se1 = models.CharField(max_length=750)
    entrevista_se1 = models.CharField(max_length=750)
    especial_se1 = models.CharField(max_length=750)
    dj_mix_se1 = models.CharField(max_length=750)
    dj_school_se1 = models.CharField(max_length=750)
    que_vida_se1 = models.CharField(max_length=750)
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField(max_length=750)
    rumba_news_se2 = models.CharField(max_length=750)
    music_news_se2 = models.CharField(max_length=750)
    entrevista_se2 = models.CharField(max_length=750)
    especial_se2 = models.CharField(max_length=750)
    dj_mix_se2 = models.CharField(max_length=750)
    dj_school_se2 = models.CharField(max_length=750)
    que_vida_se2 = models.CharField(max_length=750)
    se2_res = models.TextField()
    se1_imagen = models.CharField(max_length=750)
    se2_imagen = models.CharField(max_length=750)
    fotosv_pr = models.CharField(max_length=750)
    fotosv_se1 = models.CharField(max_length=750)
    fotosv_se2 = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'adulto_contemporaneo'

class Ambiente(models.Model):
    titulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    pr_link = models.CharField(max_length=750)
    rumba_news_pr = models.CharField(max_length=750)
    music_news_pr = models.CharField(max_length=750)
    entrevista_pr = models.CharField(max_length=750)
    especial_pr = models.CharField(max_length=750)
    dj_mix_pr = models.CharField(max_length=750)
    dj_school_pr = models.CharField(max_length=750)
    que_vida_pr = models.CharField(max_length=750)
    local_pr = models.CharField(max_length=750)
    evento_pr = models.CharField(max_length=750)
    local_se1 = models.CharField(max_length=750)
    evento_se1 = models.CharField(max_length=750)
    local_se2 = models.CharField(max_length=750)
    evento_se2 = models.CharField(max_length=750)
    encuesta = models.CharField(max_length=750)
    evento_fotos = models.CharField(max_length=750)
    imagen_evento = models.CharField(max_length=750)
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    se1_link = models.CharField(max_length=750)
    rumba_news_se1 = models.CharField(max_length=750)
    music_news_se1 = models.CharField(max_length=750)
    entrevista_se1 = models.CharField(max_length=750)
    especial_se1 = models.CharField(max_length=750)
    dj_mix_se1 = models.CharField(max_length=750)
    dj_school_se1 = models.CharField(max_length=750)
    que_vida_se1 = models.CharField(max_length=750)
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField(max_length=750)
    rumba_news_se2 = models.CharField(max_length=750)
    music_news_se2 = models.CharField(max_length=750)
    entrevista_se2 = models.CharField(max_length=750)
    especial_se2 = models.CharField(max_length=750)
    dj_mix_se2 = models.CharField(max_length=750)
    dj_school_se2 = models.CharField(max_length=750)
    que_vida_se2 = models.CharField(max_length=750)
    se2_res = models.TextField()
    se1_imagen = models.CharField(max_length=750)
    se2_imagen = models.CharField(max_length=750)
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'ambiente'

class Amorciego(models.Model):
    tu_sexo = models.CharField(max_length=750)
    edad = models.CharField(max_length=750)
    sexo_te_gusta = models.CharField(max_length=750)
    color_ojos = models.CharField(max_length=750)
    color_pelo = models.CharField(max_length=750)
    color_piel = models.CharField(max_length=750)
    estatura = models.CharField(max_length=750)
    contextura = models.CharField(max_length=750)
    gancho = models.CharField(max_length=750)
    enloquecer = models.TextField()
    producto = models.TextField()
    estudias = models.CharField(max_length=750)
    donde_estudias = models.CharField(max_length=750)
    que_haces = models.CharField(max_length=750)
    donde_haces = models.CharField(max_length=750)
    nombre = models.CharField(max_length=750)
    telefono = models.CharField(max_length=750)
    celular = models.CharField(max_length=750)
    email = models.CharField(max_length=750)
    puntuacion = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'amorciego'

class Anunciantes(models.Model):
    usuario = models.CharField(max_length=750)
    nombre = models.CharField(max_length=750)
    dia1 = models.CharField(max_length=6)
    dia2 = models.CharField(max_length=6)
    mes1 = models.CharField(max_length=6)
    mes2 = models.CharField(max_length=6)
    ano1 = models.CharField(max_length=12)
    ano2 = models.CharField(max_length=12)
    impresiones = models.CharField(max_length=750)
    tipo = models.CharField(max_length=750)
    url = models.CharField(max_length=750)
    imagen = models.CharField(max_length=750)
    beg = models.BigIntegerField()
    end = models.BigIntegerField()
    dias = models.BigIntegerField()
    clicks = models.BigIntegerField()
    total_imp = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'anunciantes'

class ArteCultura(models.Model):
    titulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    pr_link = models.CharField(max_length=750)
    rumba_news_pr = models.CharField(max_length=750)
    music_news_pr = models.CharField(max_length=750)
    entrevista_pr = models.CharField(max_length=750)
    especial_pr = models.CharField(max_length=750)
    dj_mix_pr = models.CharField(max_length=750)
    dj_school_pr = models.CharField(max_length=750)
    que_vida_pr = models.CharField(max_length=750)
    local_pr = models.CharField(max_length=750)
    evento_pr = models.CharField(max_length=750)
    local_se1 = models.CharField(max_length=750)
    evento_se1 = models.CharField(max_length=750)
    local_se2 = models.CharField(max_length=750)
    evento_se2 = models.CharField(max_length=750)
    encuesta = models.CharField(max_length=750)
    evento_fotos = models.CharField(max_length=750)
    imagen_evento = models.CharField(max_length=750)
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    se1_link = models.CharField(max_length=750)
    rumba_news_se1 = models.CharField(max_length=750)
    music_news_se1 = models.CharField(max_length=750)
    entrevista_se1 = models.CharField(max_length=750)
    especial_se1 = models.CharField(max_length=750)
    dj_mix_se1 = models.CharField(max_length=750)
    dj_school_se1 = models.CharField(max_length=750)
    que_vida_se1 = models.CharField(max_length=750)
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField(max_length=750)
    rumba_news_se2 = models.CharField(max_length=750)
    music_news_se2 = models.CharField(max_length=750)
    entrevista_se2 = models.CharField(max_length=750)
    especial_se2 = models.CharField(max_length=750)
    dj_mix_se2 = models.CharField(max_length=750)
    dj_school_se2 = models.CharField(max_length=750)
    que_vida_se2 = models.CharField(max_length=750)
    se2_res = models.TextField()
    se1_imagen = models.CharField(max_length=750)
    se2_imagen = models.CharField(max_length=750)
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'arte_cultura'

class Canciones(models.Model):
    usuario = models.BigIntegerField()
    archivo = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'canciones'

class ChicaportadaChicas(models.Model):
    nombre = models.CharField(max_length=750)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=750)
    email = models.CharField(max_length=750)
    status = models.IntegerField()
    total = models.IntegerField()
    punto1 = models.IntegerField()
    punto2 = models.IntegerField()
    punto3 = models.IntegerField()
    punto4 = models.IntegerField()
    punto5 = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'chicaportada_chicas'

class ChicaportadaVotos(models.Model):
    total = models.IntegerField()
    punto_1 = models.IntegerField()
    punto_2 = models.IntegerField()
    punto_3 = models.IntegerField()
    punto_4 = models.IntegerField()
    punto_5 = models.IntegerField()
    chica = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'chicaportada_votos'

class ClickDominos(models.Model):
    fecha = models.IntegerField()
    ip = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'click_dominos'

class Comentarios(models.Model):
    tabla = models.CharField(max_length=750)
    id_tabla = models.CharField(max_length=750)
    usuario = models.CharField(max_length=750)
    dia = models.CharField(max_length=750)
    mes = models.CharField(max_length=750)
    ano = models.CharField(max_length=750)
    hora = models.CharField(max_length=750)
    minuto = models.CharField(max_length=750)
    texto = models.TextField()
    ip = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'comentarios'

class Coments(models.Model):
    id = models.IntegerField(primary_key=True)
    postid = models.IntegerField()
    memid = models.IntegerField()
    coment = models.TextField()
    com_date = models.DateField()
    approved = models.IntegerField()
    profileid = models.IntegerField()
    class Meta:
        db_table = u'coments'

class Comunidad(models.Model):
    id = models.IntegerField(primary_key=True)
    nick = models.TextField()
    tipo = models.TextField()
    class Meta:
        db_table = u'comunidad'

class ComunidadAlbum(models.Model):
    id = models.IntegerField(unique=True)
    nick = models.CharField(max_length=300, blank=True)
    nombre = models.TextField(blank=True)
    locacion = models.TextField()
    fecha = models.DateTimeField()
    class Meta:
        db_table = u'comunidad_album'

class ComunidadAmigos(models.Model):
    id = models.IntegerField(primary_key=True)
    nick = models.TextField()
    amigo = models.TextField()
    status = models.CharField(max_length=9)
    class Meta:
        db_table = u'comunidad_amigos'

class ComunidadBloqueados(models.Model):
    nick = models.TextField()
    bloquea = models.TextField()
    class Meta:
        db_table = u'comunidad_bloqueados'

class ComunidadBuscando(models.Model):
    nick = models.CharField(max_length=300, primary_key=True)
    hombres = models.CharField(max_length=6, blank=True)
    mujeres = models.CharField(max_length=6, blank=True)
    amigos = models.CharField(max_length=6, blank=True)
    parejas = models.CharField(max_length=6, blank=True)
    trabajo = models.CharField(max_length=6, blank=True)
    class Meta:
        db_table = u'comunidad_buscando'

class ComunidadCalendariorumbas(models.Model):
    id = models.IntegerField()
    inicio = models.DateField()
    fin = models.DateField()
    nick = models.CharField(max_length=150)
    class Meta:
        db_table = u'comunidad_calendariorumbas'

class ComunidadCanciones(models.Model):
    nick = models.TextField()
    archivo = models.TextField()
    nombre = models.TextField()
    autor = models.TextField()
    comentarios = models.TextField()
    fecha = models.DateTimeField()
    class Meta:
        db_table = u'comunidad_canciones'

class ComunidadDatos(models.Model):
    id = models.IntegerField(primary_key=True)
    nick = models.CharField(max_length=300)
    nombre = models.TextField()
    apellido = models.TextField()
    sexo = models.CharField(max_length=6)
    cumple = models.DateField()
    ciudad = models.TextField()
    pais = models.TextField()
    email = models.TextField()
    telefono = models.TextField()
    celular = models.TextField()
    direccion = models.TextField()
    web = models.TextField()
    estatus = models.CharField(max_length=6)
    universidad = models.TextField()
    universidadano = models.CharField(max_length=15)
    bachillerato = models.TextField()
    bachilleratoano = models.CharField(max_length=15)
    empresa = models.TextField()
    cargo = models.TextField()
    class Meta:
        db_table = u'comunidad_datos'

class ComunidadEventos(models.Model):
    id = models.IntegerField(primary_key=True)
    nick = models.TextField()
    nombre = models.TextField()
    fecha = models.DateField()
    locacion = models.TextField()
    ciudad = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = u'comunidad_eventos'

class ComunidadFotos(models.Model):
    album = models.IntegerField(null=True, blank=True)
    archivo = models.TextField(blank=True)
    nombre = models.TextField(blank=True)
    id = models.IntegerField(primary_key=True)
    nick = models.TextField()
    class Meta:
        db_table = u'comunidad_fotos'

class ComunidadInbox(models.Model):
    id = models.IntegerField(primary_key=True)
    para = models.TextField(blank=True)
    de = models.TextField(blank=True)
    titulo = models.TextField()
    mensaje = models.TextField(blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    tipo = models.CharField(max_length=6)
    leido = models.CharField(max_length=6)
    class Meta:
        db_table = u'comunidad_inbox'

class ComunidadIntereses(models.Model):
    nick = models.CharField(max_length=300)
    item = models.TextField(blank=True)
    valor = models.TextField(blank=True)
    class Meta:
        db_table = u'comunidad_intereses'

class ComunidadInvitaciones(models.Model):
    id = models.IntegerField(primary_key=True)
    invita = models.TextField()
    nick = models.TextField()
    link = models.TextField()
    titulo = models.TextField()
    class Meta:
        db_table = u'comunidad_invitaciones'

class ComunidadMensajes(models.Model):
    id = models.IntegerField(primary_key=True)
    para = models.CharField(max_length=300, blank=True)
    de = models.CharField(max_length=300, blank=True)
    mensaje = models.TextField(blank=True)
    fecha = models.DateTimeField()
    class Meta:
        db_table = u'comunidad_mensajes'

class ComunidadVideos(models.Model):
    nick = models.TextField()
    link = models.TextField()
    nombre = models.TextField()
    comentarios = models.TextField()
    fecha = models.DateTimeField()
    class Meta:
        db_table = u'comunidad_videos'

class Comunidadb(models.Model):
    nick = models.CharField(max_length=300)
    nombre = models.TextField()
    integrantes = models.TextField()
    cumple = models.DateField()
    ocultarcumple = models.CharField(max_length=6)
    ciudad = models.TextField()
    pais = models.TextField()
    email = models.TextField()
    ocultaremail = models.CharField(max_length=6)
    genero = models.TextField()
    influencias = models.TextField()
    biografia = models.TextField()
    web = models.TextField()
    discografia = models.TextField()
    contrataciones = models.TextField()
    tipo = models.CharField(max_length=6)
    privado = models.CharField(max_length=6)
    class Meta:
        db_table = u'comunidadb'

class Comunidadd(models.Model):
    nick = models.CharField(max_length=300)
    nombre = models.TextField()
    apellido = models.TextField()
    sobrenombre = models.TextField()
    sexo = models.CharField(max_length=6)
    cumple = models.DateField()
    ocultarcumple = models.CharField(max_length=6)
    ciudad = models.TextField()
    pais = models.TextField()
    email = models.TextField()
    ocultaremail = models.CharField(max_length=6)
    telefono = models.TextField()
    celular = models.TextField()
    direccion = models.TextField()
    web = models.TextField()
    tiempocomodj = models.TextField()
    genero = models.TextField()
    influencias = models.TextField()
    bio = models.TextField()
    contrataciones = models.TextField()
    tipo = models.CharField(max_length=6)
    privado = models.CharField(max_length=6)
    class Meta:
        db_table = u'comunidadd'

class Comunidadr(models.Model):
    nick = models.CharField(max_length=300)
    nombre = models.TextField()
    apellido = models.TextField()
    sobrenombrea = models.CharField(max_length=6)
    sobrenombre = models.TextField()
    sexo = models.CharField(max_length=6)
    cumple = models.DateField()
    ocultarcumple = models.CharField(max_length=6)
    ciudad = models.TextField()
    pais = models.TextField()
    email = models.TextField()
    ocultaremail = models.CharField(max_length=6)
    telefono = models.TextField()
    celular = models.TextField()
    direccion = models.TextField()
    web = models.TextField()
    estatus = models.CharField(max_length=6)
    universidad = models.TextField()
    universidadano = models.CharField(max_length=15)
    bachillerato = models.TextField()
    bachilleratoano = models.CharField(max_length=15)
    empresa = models.TextField()
    cargo = models.TextField()
    tipo = models.CharField(max_length=6)
    privado = models.CharField(max_length=6)
    class Meta:
        db_table = u'comunidadr'

class Conciertos(models.Model):
    titulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    pr_link = models.CharField(max_length=750)
    rumba_news_pr = models.CharField(max_length=750)
    music_news_pr = models.CharField(max_length=750)
    entrevista_pr = models.CharField(max_length=750)
    especial_pr = models.CharField(max_length=750)
    dj_mix_pr = models.CharField(max_length=750)
    dj_school_pr = models.CharField(max_length=750)
    que_vida_pr = models.CharField(max_length=750)
    local_pr = models.CharField(max_length=750)
    evento_pr = models.CharField(max_length=750)
    local_se1 = models.CharField(max_length=750)
    evento_se1 = models.CharField(max_length=750)
    local_se2 = models.CharField(max_length=750)
    evento_se2 = models.CharField(max_length=750)
    encuesta = models.CharField(max_length=750)
    evento_fotos = models.CharField(max_length=750)
    imagen_evento = models.CharField(max_length=750)
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    se1_link = models.CharField(max_length=750)
    rumba_news_se1 = models.CharField(max_length=750)
    music_news_se1 = models.CharField(max_length=750)
    entrevista_se1 = models.CharField(max_length=750)
    especial_se1 = models.CharField(max_length=750)
    dj_mix_se1 = models.CharField(max_length=750)
    dj_school_se1 = models.CharField(max_length=750)
    que_vida_se1 = models.CharField(max_length=750)
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField(max_length=750)
    rumba_news_se2 = models.CharField(max_length=750)
    music_news_se2 = models.CharField(max_length=750)
    entrevista_se2 = models.CharField(max_length=750)
    especial_se2 = models.CharField(max_length=750)
    dj_mix_se2 = models.CharField(max_length=750)
    dj_school_se2 = models.CharField(max_length=750)
    que_vida_se2 = models.CharField(max_length=750)
    se2_res = models.TextField()
    se1_imagen = models.CharField(max_length=750)
    se2_imagen = models.CharField(max_length=750)
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'conciertos'

class Contenido(models.Model):
    tipo = models.BigIntegerField()
    titulo = models.CharField(max_length=750)
    fecha = models.DateField()
    imagen_listado = models.CharField(max_length=750)
    imagen_contenido = models.CharField(max_length=750)
    imagen_feature = models.CharField(max_length=750)
    url = models.CharField(max_length=750)
    contenido = models.TextField()
    posted = models.DateField()
    updated = models.DateField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'contenido'

class CuadernoEdiciones(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765)
    image = models.CharField(max_length=300)
    date_time = models.DateTimeField()
    class Meta:
        db_table = u'cuaderno_ediciones'

class Cyzone(models.Model):
    time = models.IntegerField()
    ip = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'cyzone'

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

class DjSchool(models.Model):
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
    class Meta:
        db_table = u'dj_school'

class ERumba(models.Model):
    vendedor = models.CharField(max_length=750)
    cliente = models.CharField(max_length=750)
    comentario = models.TextField()
    vinculo = models.CharField(max_length=750)
    posicion = models.CharField(max_length=750)
    fecha = models.DateField()
    archivo = models.TextField()
    n_archivo = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'e-rumba'

class EdicionesImpresas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=765)
    article1 = models.CharField(max_length=765, blank=True)
    article2 = models.CharField(max_length=765, blank=True)
    article3 = models.CharField(max_length=765, blank=True)
    article4 = models.CharField(max_length=765, blank=True)
    article5 = models.CharField(max_length=765, blank=True)
    article6 = models.CharField(max_length=765, blank=True)
    article7 = models.CharField(max_length=765, blank=True)
    article8 = models.CharField(max_length=765, blank=True)
    article9 = models.CharField(max_length=765, blank=True)
    article10 = models.CharField(max_length=765, blank=True)
    issuu_id = models.CharField(max_length=750)
    image = models.CharField(max_length=300)
    date_time = models.DateTimeField()
    ano = models.CharField(max_length=15, blank=True)
    class Meta:
        db_table = u'ediciones_impresas'

class Electronica(models.Model):
    titulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    pr_link = models.CharField(max_length=750)
    rumba_news_pr = models.CharField(max_length=750)
    music_news_pr = models.CharField(max_length=750)
    entrevista_pr = models.CharField(max_length=750)
    especial_pr = models.CharField(max_length=750)
    dj_mix_pr = models.CharField(max_length=750)
    dj_school_pr = models.CharField(max_length=750)
    que_vida_pr = models.CharField(max_length=750)
    local_pr = models.CharField(max_length=750)
    evento_pr = models.CharField(max_length=750)
    local_se1 = models.CharField(max_length=750)
    evento_se1 = models.CharField(max_length=750)
    local_se2 = models.CharField(max_length=750)
    evento_se2 = models.CharField(max_length=750)
    encuesta = models.CharField(max_length=750)
    evento_fotos = models.CharField(max_length=750)
    imagen_evento = models.CharField(max_length=750)
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    se1_link = models.CharField(max_length=750)
    rumba_news_se1 = models.CharField(max_length=750)
    music_news_se1 = models.CharField(max_length=750)
    entrevista_se1 = models.CharField(max_length=750)
    especial_se1 = models.CharField(max_length=750)
    dj_mix_se1 = models.CharField(max_length=750)
    dj_school_se1 = models.CharField(max_length=750)
    que_vida_se1 = models.CharField(max_length=750)
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField(max_length=750)
    rumba_news_se2 = models.CharField(max_length=750)
    music_news_se2 = models.CharField(max_length=750)
    entrevista_se2 = models.CharField(max_length=750)
    especial_se2 = models.CharField(max_length=750)
    dj_mix_se2 = models.CharField(max_length=750)
    dj_school_se2 = models.CharField(max_length=750)
    que_vida_se2 = models.CharField(max_length=750)
    se2_res = models.TextField()
    se1_imagen = models.CharField(max_length=750)
    se2_imagen = models.CharField(max_length=750)
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'electronica'

class Elpoint(models.Model):
    email = models.CharField(max_length=750)
    nombre = models.CharField(max_length=750)
    apellido = models.CharField(max_length=750)
    ocupacion = models.CharField(max_length=300)
    edad = models.CharField(max_length=750)
    sexo = models.CharField(max_length=750)
    telefono = models.CharField(max_length=750)
    residencia = models.CharField(max_length=750)
    universidad = models.CharField(max_length=750)
    ip = models.CharField(max_length=750)
    fecha = models.DateField()
    movilnet = models.IntegerField(null=True, blank=True)
    rcc = models.IntegerField(null=True, blank=True)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'elpoint'

class Emails(models.Model):
    email = models.CharField(unique=True, max_length=450)
    active = models.IntegerField()
    unsuscribed = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        db_table = u'emails'

class EmailsBlack(models.Model):
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    compania = models.CharField(max_length=300)
    sexo = models.IntegerField(null=True, blank=True)
    cumpleanos = models.DateField()
    pais = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=300)
    email = models.CharField(unique=True, max_length=450)
    status = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        db_table = u'emails_Black'

class EmailsMaracaibo(models.Model):
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    compania = models.CharField(max_length=300)
    sexo = models.IntegerField(null=True, blank=True)
    cumpleanos = models.DateField()
    pais = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=300)
    email = models.CharField(unique=True, max_length=450)
    status = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        db_table = u'emails_Maracaibo'

class EmailsRumbabogota(models.Model):
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    compania = models.CharField(max_length=300)
    sexo = models.IntegerField(null=True, blank=True)
    cumpleanos = models.DateField()
    pais = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=300)
    email = models.CharField(unique=True, max_length=450)
    status = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        db_table = u'emails_RumbaBogota'

class EmailsCacique(models.Model):
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    compania = models.CharField(max_length=300)
    sexo = models.IntegerField(null=True, blank=True)
    cumpleanos = models.DateField()
    pais = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=300)
    email = models.CharField(unique=True, max_length=450)
    status = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        db_table = u'emails_cacique'

class EmailsOriginales(models.Model):
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    compania = models.CharField(max_length=300)
    sexo = models.IntegerField(null=True, blank=True)
    cumpleanos = models.DateField()
    pais = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=300)
    lastbounced = models.IntegerField()
    bounced = models.IntegerField()
    email = models.CharField(unique=True, max_length=450)
    status = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        db_table = u'emails_originales'

class EncuestaElpoint(models.Model):
    opcion = models.CharField(max_length=120)
    ip = models.CharField(max_length=300)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'encuesta_elpoint'

class Encuestas(models.Model):
    pregunta = models.CharField(max_length=750)
    opcion1 = models.CharField(max_length=750)
    opcion2 = models.CharField(max_length=750)
    opcion3 = models.CharField(max_length=750)
    opcion4 = models.CharField(max_length=750)
    opcion5 = models.CharField(max_length=750)
    opcion6 = models.CharField(max_length=750)
    opcion7 = models.CharField(max_length=750)
    opcion8 = models.CharField(max_length=750)
    opcion9 = models.CharField(max_length=750)
    opcion10 = models.CharField(max_length=750)
    r1 = models.CharField(max_length=750)
    r2 = models.CharField(max_length=750)
    r3 = models.CharField(max_length=750)
    r4 = models.CharField(max_length=750)
    r5 = models.CharField(max_length=750)
    r6 = models.CharField(max_length=750)
    r7 = models.CharField(max_length=750)
    r8 = models.CharField(max_length=750)
    r9 = models.CharField(max_length=750)
    r10 = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'encuestas'

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

class Erumba(models.Model):
    asunto = models.CharField(max_length=240)
    e_envia = models.CharField(max_length=120)
    nombre = models.CharField(max_length=120)
    tipo = models.IntegerField()
    html = models.TextField()
    imagen1 = models.CharField(max_length=750)
    imagen2 = models.CharField(max_length=750)
    url1 = models.CharField(max_length=750)
    url2 = models.CharField(max_length=750)
    imagen_ext = models.CharField(max_length=750)
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    dia1 = models.IntegerField()
    mes1 = models.IntegerField()
    ano1 = models.IntegerField()
    dia2 = models.IntegerField()
    mes2 = models.IntegerField()
    ano2 = models.IntegerField()
    begin = models.CharField(max_length=750)
    end = models.CharField(max_length=750)
    status = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    imagen3 = models.CharField(max_length=750, blank=True)
    url3 = models.CharField(max_length=750, blank=True)
    class Meta:
        db_table = u'erumba'

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

class EventosBackup(models.Model):
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
    class Meta:
        db_table = u'eventos_backup'

class EventosCategorias(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=750, blank=True)
    class Meta:
        db_table = u'eventos_categorias'

class EventosCompartidos(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    nick = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'eventos_compartidos'

class EventosMas(models.Model):
    titulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    pr_link = models.CharField(max_length=750)
    rumba_news_pr = models.CharField(max_length=750)
    music_news_pr = models.CharField(max_length=750)
    entrevista_pr = models.CharField(max_length=750)
    especial_pr = models.CharField(max_length=750)
    dj_mix_pr = models.CharField(max_length=750)
    dj_school_pr = models.CharField(max_length=750)
    que_vida_pr = models.CharField(max_length=750)
    local_pr = models.CharField(max_length=750)
    evento_pr = models.CharField(max_length=750)
    local_se1 = models.CharField(max_length=750)
    evento_se1 = models.CharField(max_length=750)
    local_se2 = models.CharField(max_length=750)
    evento_se2 = models.CharField(max_length=750)
    encuesta = models.CharField(max_length=750)
    evento_fotos = models.CharField(max_length=750)
    imagen_evento = models.CharField(max_length=750)
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    se1_link = models.CharField(max_length=750)
    rumba_news_se1 = models.CharField(max_length=750)
    music_news_se1 = models.CharField(max_length=750)
    entrevista_se1 = models.CharField(max_length=750)
    especial_se1 = models.CharField(max_length=750)
    dj_mix_se1 = models.CharField(max_length=750)
    dj_school_se1 = models.CharField(max_length=750)
    que_vida_se1 = models.CharField(max_length=750)
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField(max_length=750)
    rumba_news_se2 = models.CharField(max_length=750)
    music_news_se2 = models.CharField(max_length=750)
    entrevista_se2 = models.CharField(max_length=750)
    especial_se2 = models.CharField(max_length=750)
    dj_mix_se2 = models.CharField(max_length=750)
    dj_school_se2 = models.CharField(max_length=750)
    que_vida_se2 = models.CharField(max_length=750)
    se2_res = models.TextField()
    se1_imagen = models.CharField(max_length=750)
    se2_imagen = models.CharField(max_length=750)
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'eventos_mas'

class EventosMensajes(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    nick = models.CharField(max_length=300, blank=True)
    mensaje = models.TextField(blank=True)
    fecha = models.DateTimeField()
    class Meta:
        db_table = u'eventos_mensajes'

class EventosPor(models.Model):
    titulo = models.CharField(max_length=750)
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=18)
    dia2 = models.CharField(max_length=6)
    mes2 = models.CharField(max_length=6)
    ano2 = models.CharField(max_length=18)
    dias = models.CharField(max_length=750)
    categoria = models.CharField(max_length=750)
    imagen = models.CharField(max_length=750, blank=True)
    vestuario = models.CharField(max_length=750)
    entrada = models.CharField(max_length=750)
    direccion = models.CharField(max_length=750)
    local = models.CharField(max_length=750)
    url = models.CharField(max_length=750)
    email = models.CharField(max_length=750)
    jerarquia = models.CharField(max_length=6, blank=True)
    descripcion = models.TextField(blank=True)
    hora = models.CharField(max_length=6, blank=True)
    da = models.IntegerField(null=True, blank=True)
    ma = models.IntegerField(null=True, blank=True)
    aa = models.IntegerField(null=True, blank=True)
    du = models.IntegerField(null=True, blank=True)
    mu = models.IntegerField(null=True, blank=True)
    au = models.IntegerField(null=True, blank=True)
    localn = models.CharField(max_length=750, blank=True)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'eventos_por'

class EventosRecordar(models.Model):
    fecha = models.DateField()
    id = models.IntegerField()
    email = models.TextField()
    class Meta:
        db_table = u'eventos_recordar'

class EventosVotacion(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    si = models.IntegerField(null=True, blank=True)
    quiza = models.IntegerField(null=True, blank=True)
    no = models.IntegerField(null=True, blank=True)
    nick = models.TextField(blank=True)
    class Meta:
        db_table = u'eventos_votacion'

class FnAnnotationRows(models.Model):
    id = models.IntegerField(primary_key=True)
    file = models.CharField(max_length=750, blank=True)
    image_id = models.CharField(max_length=750, blank=True)
    user_id = models.CharField(max_length=135, blank=True)
    username = models.CharField(max_length=135, blank=True)
    added = models.CharField(max_length=135, blank=True)
    modified = models.CharField(max_length=135, blank=True)
    annotation = models.CharField(max_length=135, blank=True)
    annotation_id = models.CharField(max_length=135, blank=True)
    annotation_title = models.CharField(max_length=135, blank=True)
    annotation_author = models.CharField(max_length=135, blank=True)
    annotation_boundingbox = models.CharField(max_length=135, blank=True)
    annotation_content = models.CharField(max_length=750, blank=True)
    class Meta:
        db_table = u'fn_annotation_rows'

class Fotografos(models.Model):
    nombre = models.CharField(max_length=750)
    email = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'fotografos'

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
    directorio = models.CharField(unique=True, max_length=750)
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

class FotosCompartidos(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    nick = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'fotos_compartidos'

class FotosMensajes(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    nick = models.CharField(max_length=300, blank=True)
    mensaje = models.TextField(blank=True)
    fecha = models.DateTimeField()
    class Meta:
        db_table = u'fotos_mensajes'

class FotosVotacion(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    si = models.IntegerField(null=True, blank=True)
    no = models.IntegerField(null=True, blank=True)
    nick = models.TextField()
    class Meta:
        db_table = u'fotos_votacion'

class Friends(models.Model):
    id = models.IntegerField(primary_key=True)
    friendid = models.IntegerField()
    userid = models.IntegerField()
    class Meta:
        db_table = u'friends'

class Fumanchu(models.Model):
    mes = models.IntegerField()
    ano = models.IntegerField()
    aries = models.TextField()
    tauro = models.TextField()
    geminis = models.TextField()
    cancer = models.TextField()
    leo = models.TextField()
    virgo = models.TextField()
    libra = models.TextField()
    escorpio = models.TextField()
    sagitario = models.TextField()
    capricornio = models.TextField()
    acuario = models.TextField()
    piscis = models.TextField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'fumanchu'

class Home(models.Model):
    id = models.IntegerField(primary_key=True)
    home_title = models.CharField(max_length=300)
    home_text = models.TextField()
    class Meta:
        db_table = u'home'

class Invites(models.Model):
    id = models.IntegerField(primary_key=True)
    post_date = models.DateField()
    postid = models.IntegerField()
    memid = models.IntegerField()
    approved = models.IntegerField()
    class Meta:
        db_table = u'invites'

class Leidas(models.Model):
    id = models.IntegerField()
    catalogo = models.CharField(max_length=60)
    lecturas = models.IntegerField()
    class Meta:
        db_table = u'leidas'

class Links(models.Model):
    id = models.IntegerField(primary_key=True)
    regid = models.IntegerField()
    link_title = models.CharField(max_length=300)
    link_url = models.CharField(max_length=300)
    class Meta:
        db_table = u'links'

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

class LocalesCompartidos(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    nick = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'locales_compartidos'

class LocalesMensajes(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    nick = models.CharField(max_length=300, blank=True)
    mensaje = models.TextField(blank=True)
    fecha = models.DateTimeField()
    class Meta:
        db_table = u'locales_mensajes'

class LocalesVotacion(models.Model):
    id = models.IntegerField()
    votacion = models.IntegerField()
    nick = models.TextField()
    class Meta:
        db_table = u'locales_votacion'

class LogsBouncedMails(models.Model):
    mail_id = models.BigIntegerField()
    user = models.CharField(max_length=750)
    time = models.IntegerField()
    id = models.BigIntegerField()
    class Meta:
        db_table = u'logs_bounced_mails'

class LogsOpenedMails(models.Model):
    mail_id = models.BigIntegerField()
    user = models.CharField(max_length=750)
    time = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        db_table = u'logs_opened_mails'

class LogsUrlClick(models.Model):
    mail_id = models.BigIntegerField()
    user = models.CharField(max_length=750)
    url = models.CharField(max_length=750)
    time = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        db_table = u'logs_url_click'

class MagazinePics(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mag_id = models.BigIntegerField()
    page = models.IntegerField()
    picture = models.CharField(max_length=300)
    class Meta:
        db_table = u'magazine_pics'

class Mail(models.Model):
    email = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'mail'

class Mailing(models.Model):
    email = models.TextField()
    class Meta:
        db_table = u'mailing'

class MailingFacebook(models.Model):
    email = models.TextField()
    class Meta:
        db_table = u'mailing_facebook'

class MailingLanzamiento(models.Model):
    email = models.TextField()
    class Meta:
        db_table = u'mailing_lanzamiento'

class MailingPrestable(models.Model):
    email = models.TextField()
    class Meta:
        db_table = u'mailing_prestable'

class MailingPruebarufi(models.Model):
    email = models.TextField()
    class Meta:
        db_table = u'mailing_pruebarufi'

class MamiPapi(models.Model):
    nombre = models.CharField(max_length=750)
    ocupacion = models.CharField(max_length=750)
    edad = models.CharField(max_length=750)
    genero = models.CharField(max_length=750)
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    directorio = models.CharField(max_length=750)
    imagen = models.CharField(max_length=750)
    imagen2 = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'mami_papi'

class MamiPapi2(models.Model):
    nombre = models.CharField(max_length=750)
    ocupacion = models.CharField(max_length=750)
    edad = models.CharField(max_length=750)
    genero = models.CharField(max_length=750)
    dia = models.CharField(max_length=750)
    mes = models.CharField(max_length=750)
    ano = models.CharField(max_length=750)
    directorio = models.CharField(max_length=750)
    imagen = models.CharField(max_length=750)
    imagen2 = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'mami_papi2'

class MamiVista(models.Model):
    vista = models.BigIntegerField()
    ranking = models.CharField(max_length=750)
    mami_papi = models.CharField(max_length=750)
    tiempo = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'mami_vista'

class Minisites(models.Model):
    id = models.IntegerField(primary_key=True)
    sitio = models.TextField()
    plantilla = models.TextField()
    articulo = models.IntegerField()
    class Meta:
        db_table = u'minisites'

class MotoEventos(models.Model):
    nombre = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'moto_eventos'

class MotoVotos(models.Model):
    email = models.CharField(max_length=750)
    foto = models.IntegerField()
    evento = models.IntegerField()
    puntos = models.IntegerField()
    foto_id = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'moto_votos'

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

class Newsletters(models.Model):
    db = models.CharField(max_length=300)
    subject = models.CharField(max_length=750)
    body = models.TextField()
    fixed_body = models.TextField()
    time = models.IntegerField()
    sent_start = models.IntegerField()
    sent_finish = models.IntegerField()
    total = models.IntegerField()
    sent = models.IntegerField()
    fail = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        db_table = u'newsletters'

class NewslettersBounced(models.Model):
    email = models.CharField(unique=True, max_length=150)
    lbounced = models.IntegerField()
    n_id = models.IntegerField()
    tries = models.IntegerField()
    class Meta:
        db_table = u'newsletters_bounced'

class NewslettersUnsuscribeds(models.Model):
    email = models.CharField(unique=True, max_length=180)
    time = models.IntegerField()
    class Meta:
        db_table = u'newsletters_unsuscribeds'

class NokiaFoto(models.Model):
    email = models.CharField(max_length=750)
    historia = models.TextField()
    file = models.CharField(max_length=750)
    time = models.IntegerField()
    status = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'nokia_foto'

class NokiaReg(models.Model):
    nombre = models.CharField(max_length=750)
    fnacimiento = models.DateField()
    email = models.CharField(max_length=750)
    optin = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'nokia_reg'

class NoticiasCompartidos(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    cat = models.CharField(max_length=90, blank=True)
    nick = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'noticias_compartidos'

class NoticiasMensajes(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    nick = models.CharField(max_length=300, blank=True)
    mensaje = models.TextField(blank=True)
    fecha = models.DateTimeField()
    cat = models.TextField(blank=True)
    class Meta:
        db_table = u'noticias_mensajes'

class Otros(models.Model):
    email = models.CharField(max_length=750)
    stats = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'otros'

class Pautas(models.Model):
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    evento = models.CharField(max_length=750)
    fotografos = models.CharField(max_length=750)
    comentario = models.TextField()
    hora = models.IntegerField()
    hora_r = models.CharField(max_length=6)
    direccion = models.CharField(max_length=750)
    time = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'pautas'

class Photocoments(models.Model):
    id = models.IntegerField(primary_key=True)
    photoid = models.IntegerField()
    postid = models.IntegerField()
    coment = models.TextField()
    com_date = models.DateField()
    approved = models.IntegerField()
    class Meta:
        db_table = u'photocoments'

class Photos(models.Model):
    id = models.IntegerField(primary_key=True)
    regid = models.IntegerField()
    pathtophoto = models.CharField(max_length=300)
    leyenda = models.CharField(max_length=750)
    view = models.BigIntegerField()
    class Meta:
        db_table = u'photos'

class Principal(models.Model):
    dia = models.CharField(max_length=750)
    mes = models.CharField(max_length=750)
    ano = models.CharField(max_length=750)
    local_dia = models.CharField(max_length=750)
    local_link = models.CharField(max_length=750)
    evento_local = models.CharField(max_length=750)
    local_des = models.TextField()
    ev_titulo = models.CharField(max_length=750)
    ev_evento = models.CharField(max_length=750)
    pr_titulo = models.CharField(max_length=750)
    pr_des = models.TextField()
    se1_titulo = models.CharField(max_length=750)
    se1_des = models.TextField()
    se2_titulo = models.CharField(max_length=750)
    se2_des = models.TextField()
    se3_titulo = models.CharField(max_length=750)
    se3_des = models.TextField()
    se4_titulo = models.CharField(max_length=750)
    se4_des = models.TextField()
    imagen_pr = models.CharField(max_length=750)
    imagen_se1 = models.CharField(max_length=750)
    imagen_se2 = models.CharField(max_length=750)
    imagen_se3 = models.CharField(max_length=750)
    imagen_se4 = models.CharField(max_length=750)
    imagen_ev1 = models.CharField(max_length=750)
    imagen_ev2 = models.CharField(max_length=750)
    imagen_ev3 = models.CharField(max_length=750)
    pr_link = models.CharField(max_length=750)
    rumba_news_pr = models.CharField(max_length=750)
    music_news_pr = models.CharField(max_length=750)
    entrevista_pr = models.CharField(max_length=750)
    especial_pr = models.CharField(max_length=750)
    dj_mix_pr = models.CharField(max_length=750)
    dj_school_pr = models.CharField(max_length=750)
    que_vida_pr = models.CharField(max_length=750)
    local_pr = models.CharField(max_length=750)
    evento_pr = models.CharField(max_length=750)
    se1_link = models.CharField(max_length=750)
    rumba_news_se1 = models.CharField(max_length=750)
    music_news_se1 = models.CharField(max_length=750)
    entrevista_se1 = models.CharField(max_length=750)
    especial_se1 = models.CharField(max_length=750)
    dj_mix_se1 = models.CharField(max_length=750)
    dj_school_se1 = models.CharField(max_length=750)
    que_vida_se1 = models.CharField(max_length=750)
    local_se1 = models.CharField(max_length=750)
    evento_se1 = models.CharField(max_length=750)
    se2_link = models.CharField(max_length=750)
    rumba_news_se2 = models.CharField(max_length=750)
    music_news_se2 = models.CharField(max_length=750)
    entrevista_se2 = models.CharField(max_length=750)
    especial_se2 = models.CharField(max_length=750)
    dj_mix_se2 = models.CharField(max_length=750)
    dj_school_se2 = models.CharField(max_length=750)
    que_vida_se2 = models.CharField(max_length=750)
    local_se2 = models.CharField(max_length=750)
    evento_se2 = models.CharField(max_length=750)
    se3_link = models.CharField(max_length=750)
    rumba_news_se3 = models.CharField(max_length=750)
    music_news_se3 = models.CharField(max_length=750)
    entrevista_se3 = models.CharField(max_length=750)
    especial_se3 = models.CharField(max_length=750)
    dj_mix_se3 = models.CharField(max_length=750)
    dj_school_se3 = models.CharField(max_length=750)
    que_vida_se3 = models.CharField(max_length=750)
    local_se3 = models.CharField(max_length=750)
    evento_se3 = models.CharField(max_length=750)
    se4_link = models.CharField(max_length=750)
    rumba_news_se4 = models.CharField(max_length=750)
    music_news_se4 = models.CharField(max_length=750)
    entrevista_se4 = models.CharField(max_length=750)
    especial_se4 = models.CharField(max_length=750)
    dj_mix_se4 = models.CharField(max_length=750)
    dj_school_se4 = models.CharField(max_length=750)
    que_vida_se4 = models.CharField(max_length=750)
    local_se4 = models.CharField(max_length=750)
    evento_se4 = models.CharField(max_length=750)
    fotosv_pr = models.CharField(max_length=750)
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    fotosv_se3 = models.BigIntegerField()
    fotosv_se4 = models.BigIntegerField()
    fotos_pr = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'principal'

class QueVida(models.Model):
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
    class Meta:
        db_table = u'que_vida'

class Rate(models.Model):
    id = models.IntegerField(primary_key=True)
    photoid = models.IntegerField()
    memid = models.IntegerField()
    rate = models.IntegerField()
    class Meta:
        db_table = u'rate'

class RateLocales(models.Model):
    db = models.IntegerField()
    local = models.BigIntegerField()
    user = models.BigIntegerField()
    class Meta:
        db_table = u'rate_locales'

class RateRumbas(models.Model):
    db = models.IntegerField()
    rumba = models.BigIntegerField()
    user = models.BigIntegerField()
    class Meta:
        db_table = u'rate_rumbas'

class RegControl(models.Model):
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'reg_control'

class Registration(models.Model):
    id = models.IntegerField(primary_key=True)
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
    stars = models.IntegerField()
    imagen_principal = models.TextField()
    imagen_original = models.TextField()
    rumba1 = models.BigIntegerField()
    rumba2 = models.BigIntegerField()
    rumba3 = models.BigIntegerField()
    local1 = models.BigIntegerField()
    local2 = models.BigIntegerField()
    local3 = models.BigIntegerField()
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
    class Meta:
        db_table = u'registration'

class ResMoto(models.Model):
    foto = models.BigIntegerField()
    votos = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'res_moto'

class ResMotoUser(models.Model):
    email = models.CharField(max_length=750)
    votos = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'res_moto_user'

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

class Rumbas(models.Model):
    titulo = models.CharField(max_length=750)
    imagen1 = models.CharField(max_length=750)
    pr_link = models.CharField(max_length=750)
    rumba_news_pr = models.CharField(max_length=750)
    music_news_pr = models.CharField(max_length=750)
    entrevista_pr = models.CharField(max_length=750)
    especial_pr = models.CharField(max_length=750)
    dj_mix_pr = models.CharField(max_length=750)
    dj_school_pr = models.CharField(max_length=750)
    que_vida_pr = models.CharField(max_length=750)
    local_pr = models.CharField(max_length=750)
    evento_pr = models.CharField(max_length=750)
    local_se1 = models.CharField(max_length=750)
    evento_se1 = models.CharField(max_length=750)
    local_se2 = models.CharField(max_length=750)
    evento_se2 = models.CharField(max_length=750)
    encuesta = models.CharField(max_length=750)
    evento_fotos = models.CharField(max_length=750)
    imagen_evento = models.CharField(max_length=750)
    dia = models.CharField(max_length=6)
    mes = models.CharField(max_length=6)
    ano = models.CharField(max_length=12)
    se1_link = models.CharField(max_length=750)
    rumba_news_se1 = models.CharField(max_length=750)
    music_news_se1 = models.CharField(max_length=750)
    entrevista_se1 = models.CharField(max_length=750)
    especial_se1 = models.CharField(max_length=750)
    dj_mix_se1 = models.CharField(max_length=750)
    dj_school_se1 = models.CharField(max_length=750)
    que_vida_se1 = models.CharField(max_length=750)
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField(max_length=750)
    rumba_news_se2 = models.CharField(max_length=750)
    music_news_se2 = models.CharField(max_length=750)
    entrevista_se2 = models.CharField(max_length=750)
    especial_se2 = models.CharField(max_length=750)
    dj_mix_se2 = models.CharField(max_length=750)
    dj_school_se2 = models.CharField(max_length=750)
    que_vida_se2 = models.CharField(max_length=750)
    se2_res = models.TextField()
    se1_imagen = models.CharField(max_length=750)
    se2_imagen = models.CharField(max_length=750)
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'rumbas'

class Secciones(models.Model):
    imagen = models.CharField(max_length=750)
    titulo = models.CharField(max_length=750)
    descripcion = models.TextField()
    vinculo = models.CharField(max_length=750)
    vinculo_externo = models.CharField(max_length=750)
    vinculo_externo_tipo = models.CharField(max_length=750)
    vinculo_externo_target = models.CharField(max_length=750)
    vinculo_local = models.CharField(max_length=750)
    vinculo_seccion = models.CharField(max_length=750)
    vinculo_evento = models.CharField(max_length=750)
    pagina = models.CharField(max_length=750)
    numero = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'secciones'

class Ss2011(models.Model):
    articulo = models.IntegerField()
    id = models.IntegerField()
    plantilla = models.TextField()
    sitio = models.TextField()
    pagina = models.CharField(max_length=12)
    class Meta:
        db_table = u'ss2011'

class Tbladmins(models.Model):
    adminid = models.IntegerField(primary_key=True, db_column='adminId') # Field name made lowercase.
    username = models.CharField(max_length=75, blank=True)
    password = models.CharField(max_length=105, blank=True)
    name = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tblAdmins'

class Tbltasks(models.Model):
    taskid = models.BigIntegerField(primary_key=True, db_column='taskId') # Field name made lowercase.
    userid = models.IntegerField(null=True, db_column='userId', blank=True) # Field name made lowercase.
    task = models.CharField(max_length=765, blank=True)
    description = models.TextField(blank=True)
    priority = models.BigIntegerField(null=True, blank=True)
    dateposted = models.DateField(null=True, db_column='datePosted', blank=True) # Field name made lowercase.
    datetobecompleted = models.DateField(null=True, db_column='dateToBeCompleted', blank=True) # Field name made lowercase.
    datecompleted = models.DateField(null=True, db_column='dateCompleted', blank=True) # Field name made lowercase.
    completed = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = u'tblTasks'

class Tblusers(models.Model):
    userid = models.IntegerField(primary_key=True, db_column='userId') # Field name made lowercase.
    name = models.CharField(max_length=300, blank=True)
    tabname = models.CharField(max_length=150, db_column='tabName', blank=True) # Field name made lowercase.
    email = models.CharField(unique=True, max_length=300, blank=True)
    password = models.CharField(max_length=105, blank=True)
    class Meta:
        db_table = u'tblUsers'

class TmpLocal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=750)
    tipo = models.CharField(max_length=750)
    restaurant = models.TextField()
    direccion = models.CharField(max_length=750)
    ciudad = models.CharField(max_length=750)
    telefono = models.CharField(max_length=750)
    telefono2 = models.CharField(max_length=750)
    fax = models.CharField(max_length=750)
    url = models.CharField(max_length=750)
    email = models.CharField(max_length=750)
    horario = models.CharField(max_length=750)
    ambiente = models.CharField(max_length=750)
    musica = models.CharField(max_length=750)
    dj = models.CharField(max_length=750)
    vestuario = models.CharField(max_length=750)
    capacidad = models.CharField(max_length=750)
    imagen = models.CharField(max_length=750)
    descripcion = models.TextField()
    gerente = models.CharField(max_length=750)
    contacto = models.CharField(max_length=750)
    actualizaciones = models.CharField(max_length=750)
    telefonosc = models.CharField(max_length=750)
    emailc = models.CharField(max_length=750)
    day = models.DateField()
    class Meta:
        db_table = u'tmp_local'

class TmpNews(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=750)
    img_thumb = models.CharField(max_length=750)
    img_enlarged = models.CharField(max_length=750)
    img_title = models.CharField(max_length=750)
    info = models.CharField(max_length=750)
    details = models.TextField(blank=True)
    day = models.DateField(null=True, blank=True)
    section = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'tmp_news'

class Topdjsreg(models.Model):
    nombre = models.CharField(max_length=750)
    apellido = models.CharField(max_length=750)
    email = models.CharField(max_length=750)
    telefono = models.IntegerField()
    email_md5 = models.CharField(max_length=750)
    v1 = models.BigIntegerField()
    v2 = models.BigIntegerField()
    v3 = models.BigIntegerField()
    v4 = models.BigIntegerField()
    v5 = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'topdjsreg'

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

class TusfotosMensajes(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    nick = models.CharField(max_length=300, blank=True)
    mensaje = models.TextField(blank=True)
    fecha = models.DateTimeField()
    class Meta:
        db_table = u'tusfotos_mensajes'

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

class TusfotosVotacion(models.Model):
    id = models.IntegerField()
    votacion = models.IntegerField()
    nick = models.TextField()
    fecha = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'tusfotos_votacion'

class UserAnun(models.Model):
    user = models.CharField(unique=True, max_length=750)
    pass_field = models.CharField(max_length=750, db_column='pass') # Field renamed because it was a Python reserved word.
    email = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'user_anun'

class UserMoto(models.Model):
    nombre = models.CharField(max_length=750)
    apellido = models.CharField(max_length=750)
    ci = models.CharField(max_length=750)
    email = models.CharField(unique=True, max_length=750)
    telefono = models.CharField(max_length=750)
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'user_moto'

class Users(models.Model):
    email = models.CharField(max_length=750)
    status = models.IntegerField()
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'users'

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

class Usuarios2(models.Model):
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
    stars = models.IntegerField()
    imagen_principal = models.TextField()
    imagen_original = models.TextField()
    rumba1 = models.BigIntegerField()
    rumba2 = models.BigIntegerField()
    rumba3 = models.BigIntegerField()
    local1 = models.BigIntegerField()
    local2 = models.BigIntegerField()
    local3 = models.BigIntegerField()
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
    class Meta:
        db_table = u'usuarios2'

class VideosMensajes(models.Model):
    id = models.BigIntegerField(null=True, blank=True)
    nick = models.CharField(max_length=300, blank=True)
    mensaje = models.TextField(blank=True)
    fecha = models.DateTimeField()
    class Meta:
        db_table = u'videos_mensajes'

class VideosVotacion(models.Model):
    id = models.IntegerField()
    votacion = models.IntegerField()
    nick = models.TextField()
    fecha = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'videos_votacion'

