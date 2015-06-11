# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Admin( models.Model ):
    id = models.IntegerField( primary_key = True )
    username = models.CharField( max_length = 300 )
    password = models.CharField( max_length = 300 )
    class Meta:
        db_table = u'admin'

class Administrador( models.Model ):
    nombre = models.CharField( max_length = 750 )
    apellido = models.CharField( max_length = 750 )
    user = models.CharField( max_length = 750 )
    pass_field = models.CharField( max_length = 750, db_column = 'pass' ) # Field renamed because it was a Python reserved word.
    status = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'administrador'

class AdultoContemporaneo( models.Model ):
    titulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    pr_link = models.CharField( max_length = 750 )
    rumba_news_pr = models.CharField( max_length = 750 )
    music_news_pr = models.CharField( max_length = 750 )
    entrevista_pr = models.CharField( max_length = 750 )
    especial_pr = models.CharField( max_length = 750 )
    dj_mix_pr = models.CharField( max_length = 750 )
    dj_school_pr = models.CharField( max_length = 750 )
    que_vida_pr = models.CharField( max_length = 750 )
    local_pr = models.CharField( max_length = 750 )
    evento_pr = models.CharField( max_length = 750 )
    local_se1 = models.CharField( max_length = 750 )
    evento_se1 = models.CharField( max_length = 750 )
    local_se2 = models.CharField( max_length = 750 )
    evento_se2 = models.CharField( max_length = 750 )
    encuesta = models.CharField( max_length = 750 )
    evento_fotos = models.CharField( max_length = 750 )
    imagen_evento = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    se1_link = models.CharField( max_length = 750 )
    rumba_news_se1 = models.CharField( max_length = 750 )
    music_news_se1 = models.CharField( max_length = 750 )
    entrevista_se1 = models.CharField( max_length = 750 )
    especial_se1 = models.CharField( max_length = 750 )
    dj_mix_se1 = models.CharField( max_length = 750 )
    dj_school_se1 = models.CharField( max_length = 750 )
    que_vida_se1 = models.CharField( max_length = 750 )
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField( max_length = 750 )
    rumba_news_se2 = models.CharField( max_length = 750 )
    music_news_se2 = models.CharField( max_length = 750 )
    entrevista_se2 = models.CharField( max_length = 750 )
    especial_se2 = models.CharField( max_length = 750 )
    dj_mix_se2 = models.CharField( max_length = 750 )
    dj_school_se2 = models.CharField( max_length = 750 )
    que_vida_se2 = models.CharField( max_length = 750 )
    se2_res = models.TextField()
    se1_imagen = models.CharField( max_length = 750 )
    se2_imagen = models.CharField( max_length = 750 )
    fotosv_pr = models.CharField( max_length = 750 )
    fotosv_se1 = models.CharField( max_length = 750 )
    fotosv_se2 = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'adulto_contemporaneo'

class Ambiente( models.Model ):
    titulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    pr_link = models.CharField( max_length = 750 )
    rumba_news_pr = models.CharField( max_length = 750 )
    music_news_pr = models.CharField( max_length = 750 )
    entrevista_pr = models.CharField( max_length = 750 )
    especial_pr = models.CharField( max_length = 750 )
    dj_mix_pr = models.CharField( max_length = 750 )
    dj_school_pr = models.CharField( max_length = 750 )
    que_vida_pr = models.CharField( max_length = 750 )
    local_pr = models.CharField( max_length = 750 )
    evento_pr = models.CharField( max_length = 750 )
    local_se1 = models.CharField( max_length = 750 )
    evento_se1 = models.CharField( max_length = 750 )
    local_se2 = models.CharField( max_length = 750 )
    evento_se2 = models.CharField( max_length = 750 )
    encuesta = models.CharField( max_length = 750 )
    evento_fotos = models.CharField( max_length = 750 )
    imagen_evento = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    se1_link = models.CharField( max_length = 750 )
    rumba_news_se1 = models.CharField( max_length = 750 )
    music_news_se1 = models.CharField( max_length = 750 )
    entrevista_se1 = models.CharField( max_length = 750 )
    especial_se1 = models.CharField( max_length = 750 )
    dj_mix_se1 = models.CharField( max_length = 750 )
    dj_school_se1 = models.CharField( max_length = 750 )
    que_vida_se1 = models.CharField( max_length = 750 )
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField( max_length = 750 )
    rumba_news_se2 = models.CharField( max_length = 750 )
    music_news_se2 = models.CharField( max_length = 750 )
    entrevista_se2 = models.CharField( max_length = 750 )
    especial_se2 = models.CharField( max_length = 750 )
    dj_mix_se2 = models.CharField( max_length = 750 )
    dj_school_se2 = models.CharField( max_length = 750 )
    que_vida_se2 = models.CharField( max_length = 750 )
    se2_res = models.TextField()
    se1_imagen = models.CharField( max_length = 750 )
    se2_imagen = models.CharField( max_length = 750 )
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'ambiente'

class Amorciego( models.Model ):
    tu_sexo = models.CharField( max_length = 750 )
    edad = models.CharField( max_length = 750 )
    sexo_te_gusta = models.CharField( max_length = 750 )
    color_ojos = models.CharField( max_length = 750 )
    color_pelo = models.CharField( max_length = 750 )
    color_piel = models.CharField( max_length = 750 )
    estatura = models.CharField( max_length = 750 )
    contextura = models.CharField( max_length = 750 )
    gancho = models.CharField( max_length = 750 )
    enloquecer = models.TextField()
    producto = models.TextField()
    estudias = models.CharField( max_length = 750 )
    donde_estudias = models.CharField( max_length = 750 )
    que_haces = models.CharField( max_length = 750 )
    donde_haces = models.CharField( max_length = 750 )
    nombre = models.CharField( max_length = 750 )
    telefono = models.CharField( max_length = 750 )
    celular = models.CharField( max_length = 750 )
    email = models.CharField( max_length = 750 )
    puntuacion = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'amorciego'

class Anunciantes( models.Model ):
    usuario = models.CharField( max_length = 750 )
    nombre = models.CharField( max_length = 750 )
    dia1 = models.CharField( max_length = 6 )
    dia2 = models.CharField( max_length = 6 )
    mes1 = models.CharField( max_length = 6 )
    mes2 = models.CharField( max_length = 6 )
    ano1 = models.CharField( max_length = 12 )
    ano2 = models.CharField( max_length = 12 )
    impresiones = models.CharField( max_length = 750 )
    tipo = models.CharField( max_length = 750 )
    url = models.CharField( max_length = 750 )
    imagen = models.CharField( max_length = 750 )
    beg = models.BigIntegerField()
    end = models.BigIntegerField()
    dias = models.BigIntegerField()
    clicks = models.BigIntegerField()
    total_imp = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'anunciantes'

class ArteCultura( models.Model ):
    titulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    pr_link = models.CharField( max_length = 750 )
    rumba_news_pr = models.CharField( max_length = 750 )
    music_news_pr = models.CharField( max_length = 750 )
    entrevista_pr = models.CharField( max_length = 750 )
    especial_pr = models.CharField( max_length = 750 )
    dj_mix_pr = models.CharField( max_length = 750 )
    dj_school_pr = models.CharField( max_length = 750 )
    que_vida_pr = models.CharField( max_length = 750 )
    local_pr = models.CharField( max_length = 750 )
    evento_pr = models.CharField( max_length = 750 )
    local_se1 = models.CharField( max_length = 750 )
    evento_se1 = models.CharField( max_length = 750 )
    local_se2 = models.CharField( max_length = 750 )
    evento_se2 = models.CharField( max_length = 750 )
    encuesta = models.CharField( max_length = 750 )
    evento_fotos = models.CharField( max_length = 750 )
    imagen_evento = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    se1_link = models.CharField( max_length = 750 )
    rumba_news_se1 = models.CharField( max_length = 750 )
    music_news_se1 = models.CharField( max_length = 750 )
    entrevista_se1 = models.CharField( max_length = 750 )
    especial_se1 = models.CharField( max_length = 750 )
    dj_mix_se1 = models.CharField( max_length = 750 )
    dj_school_se1 = models.CharField( max_length = 750 )
    que_vida_se1 = models.CharField( max_length = 750 )
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField( max_length = 750 )
    rumba_news_se2 = models.CharField( max_length = 750 )
    music_news_se2 = models.CharField( max_length = 750 )
    entrevista_se2 = models.CharField( max_length = 750 )
    especial_se2 = models.CharField( max_length = 750 )
    dj_mix_se2 = models.CharField( max_length = 750 )
    dj_school_se2 = models.CharField( max_length = 750 )
    que_vida_se2 = models.CharField( max_length = 750 )
    se2_res = models.TextField()
    se1_imagen = models.CharField( max_length = 750 )
    se2_imagen = models.CharField( max_length = 750 )
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'arte_cultura'

class Canciones( models.Model ):
    usuario = models.BigIntegerField()
    archivo = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'canciones'

class ChicaportadaChicas( models.Model ):
    nombre = models.CharField( max_length = 750 )
    edad = models.IntegerField()
    telefono = models.CharField( max_length = 750 )
    email = models.CharField( max_length = 750 )
    status = models.IntegerField()
    total = models.IntegerField()
    punto1 = models.IntegerField()
    punto2 = models.IntegerField()
    punto3 = models.IntegerField()
    punto4 = models.IntegerField()
    punto5 = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'chicaportada_chicas'

class ChicaportadaFotos( models.Model ):
    big = models.TextField()
    small = models.TextField()
    chica = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'chicaportada_fotos'

class ChicaportadaVotos( models.Model ):
    total = models.IntegerField()
    punto_1 = models.IntegerField()
    punto_2 = models.IntegerField()
    punto_3 = models.IntegerField()
    punto_4 = models.IntegerField()
    punto_5 = models.IntegerField()
    chica = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'chicaportada_votos'

class ClickDominos( models.Model ):
    fecha = models.IntegerField()
    ip = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'click_dominos'

class Comentarios( models.Model ):
    tabla = models.CharField( max_length = 750 )
    id_tabla = models.CharField( max_length = 750 )
    usuario = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 750 )
    mes = models.CharField( max_length = 750 )
    ano = models.CharField( max_length = 750 )
    hora = models.CharField( max_length = 750 )
    minuto = models.CharField( max_length = 750 )
    texto = models.TextField()
    ip = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'comentarios'

class Coments( models.Model ):
    id = models.IntegerField( primary_key = True )
    postid = models.IntegerField()
    memid = models.IntegerField()
    coment = models.TextField()
    com_date = models.DateField()
    approved = models.IntegerField()
    profileid = models.IntegerField()
    class Meta:
        db_table = u'coments'

class Conciertos( models.Model ):
    titulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    pr_link = models.CharField( max_length = 750 )
    rumba_news_pr = models.CharField( max_length = 750 )
    music_news_pr = models.CharField( max_length = 750 )
    entrevista_pr = models.CharField( max_length = 750 )
    especial_pr = models.CharField( max_length = 750 )
    dj_mix_pr = models.CharField( max_length = 750 )
    dj_school_pr = models.CharField( max_length = 750 )
    que_vida_pr = models.CharField( max_length = 750 )
    local_pr = models.CharField( max_length = 750 )
    evento_pr = models.CharField( max_length = 750 )
    local_se1 = models.CharField( max_length = 750 )
    evento_se1 = models.CharField( max_length = 750 )
    local_se2 = models.CharField( max_length = 750 )
    evento_se2 = models.CharField( max_length = 750 )
    encuesta = models.CharField( max_length = 750 )
    evento_fotos = models.CharField( max_length = 750 )
    imagen_evento = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    se1_link = models.CharField( max_length = 750 )
    rumba_news_se1 = models.CharField( max_length = 750 )
    music_news_se1 = models.CharField( max_length = 750 )
    entrevista_se1 = models.CharField( max_length = 750 )
    especial_se1 = models.CharField( max_length = 750 )
    dj_mix_se1 = models.CharField( max_length = 750 )
    dj_school_se1 = models.CharField( max_length = 750 )
    que_vida_se1 = models.CharField( max_length = 750 )
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField( max_length = 750 )
    rumba_news_se2 = models.CharField( max_length = 750 )
    music_news_se2 = models.CharField( max_length = 750 )
    entrevista_se2 = models.CharField( max_length = 750 )
    especial_se2 = models.CharField( max_length = 750 )
    dj_mix_se2 = models.CharField( max_length = 750 )
    dj_school_se2 = models.CharField( max_length = 750 )
    que_vida_se2 = models.CharField( max_length = 750 )
    se2_res = models.TextField()
    se1_imagen = models.CharField( max_length = 750 )
    se2_imagen = models.CharField( max_length = 750 )
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'conciertos'

class Contenido( models.Model ):
    tipo = models.BigIntegerField()
    titulo = models.CharField( max_length = 750 )
    fecha = models.DateField()
    imagen_listado = models.CharField( max_length = 750 )
    imagen_contenido = models.CharField( max_length = 750 )
    imagen_feature = models.CharField( max_length = 750 )
    url = models.CharField( max_length = 750 )
    contenido = models.TextField()
    posted = models.DateField()
    updated = models.DateField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'contenido'

class Cyzone( models.Model ):
    time = models.IntegerField()
    ip = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'cyzone'

class Dj( models.Model ):
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    titulo = models.CharField( max_length = 750 )
    subtitulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    titcon = models.CharField( max_length = 750 )
    contenido = models.TextField()
    info = models.CharField( max_length = 750 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    int = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'dj'

class DjSchool( models.Model ):
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    titulo = models.CharField( max_length = 750 )
    subtitulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    titcon = models.CharField( max_length = 750 )
    contenido = models.TextField()
    info = models.CharField( max_length = 750 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'dj_school'

class ERumba( models.Model ):
    vendedor = models.CharField( max_length = 750 )
    cliente = models.CharField( max_length = 750 )
    comentario = models.TextField()
    vinculo = models.CharField( max_length = 750 )
    posicion = models.CharField( max_length = 750 )
    fecha = models.DateField()
    archivo = models.TextField()
    n_archivo = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'e-rumba'

class Electronica( models.Model ):
    titulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    pr_link = models.CharField( max_length = 750 )
    rumba_news_pr = models.CharField( max_length = 750 )
    music_news_pr = models.CharField( max_length = 750 )
    entrevista_pr = models.CharField( max_length = 750 )
    especial_pr = models.CharField( max_length = 750 )
    dj_mix_pr = models.CharField( max_length = 750 )
    dj_school_pr = models.CharField( max_length = 750 )
    que_vida_pr = models.CharField( max_length = 750 )
    local_pr = models.CharField( max_length = 750 )
    evento_pr = models.CharField( max_length = 750 )
    local_se1 = models.CharField( max_length = 750 )
    evento_se1 = models.CharField( max_length = 750 )
    local_se2 = models.CharField( max_length = 750 )
    evento_se2 = models.CharField( max_length = 750 )
    encuesta = models.CharField( max_length = 750 )
    evento_fotos = models.CharField( max_length = 750 )
    imagen_evento = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    se1_link = models.CharField( max_length = 750 )
    rumba_news_se1 = models.CharField( max_length = 750 )
    music_news_se1 = models.CharField( max_length = 750 )
    entrevista_se1 = models.CharField( max_length = 750 )
    especial_se1 = models.CharField( max_length = 750 )
    dj_mix_se1 = models.CharField( max_length = 750 )
    dj_school_se1 = models.CharField( max_length = 750 )
    que_vida_se1 = models.CharField( max_length = 750 )
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField( max_length = 750 )
    rumba_news_se2 = models.CharField( max_length = 750 )
    music_news_se2 = models.CharField( max_length = 750 )
    entrevista_se2 = models.CharField( max_length = 750 )
    especial_se2 = models.CharField( max_length = 750 )
    dj_mix_se2 = models.CharField( max_length = 750 )
    dj_school_se2 = models.CharField( max_length = 750 )
    que_vida_se2 = models.CharField( max_length = 750 )
    se2_res = models.TextField()
    se1_imagen = models.CharField( max_length = 750 )
    se2_imagen = models.CharField( max_length = 750 )
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'electronica'

class Elpoint( models.Model ):
    email = models.CharField( max_length = 750 )
    nombre = models.CharField( max_length = 750 )
    apellido = models.CharField( max_length = 750 )
    ocupacion = models.CharField( max_length = 300 )
    edad = models.CharField( max_length = 750 )
    sexo = models.CharField( max_length = 750 )
    telefono = models.CharField( max_length = 750 )
    residencia = models.CharField( max_length = 750 )
    universidad = models.CharField( max_length = 750 )
    ip = models.CharField( max_length = 750 )
    fecha = models.DateField()
    movilnet = models.IntegerField( null = True, blank = True )
    rcc = models.IntegerField( null = True, blank = True )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'elpoint'

class Emails( models.Model ):
    email = models.CharField( max_length = 450 )
    active = models.IntegerField()
    unsuscribed = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True )
    class Meta:
        db_table = u'emails'

class EmailsNegros( models.Model ):
    nombre = models.CharField( max_length = 750 )
    email = models.CharField( max_length = 750 )
    status = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'emails_negros'

class EmailsPrueba( models.Model ):
    nombre = models.CharField( max_length = 300 )
    apellido = models.CharField( max_length = 300 )
    compania = models.CharField( max_length = 300 )
    sexo = models.IntegerField( null = True, blank = True )
    cumpleanos = models.DateField()
    pais = models.CharField( max_length = 300 )
    ciudad = models.CharField( max_length = 300 )
    email = models.CharField( max_length = 450 )
    status = models.IntegerField()
    id = models.BigIntegerField( primary_key = True )
    class Meta:
        db_table = u'emails_prueba'

class EmailsRumbabogota( models.Model ):
    nombre = models.CharField( max_length = 300 )
    apellido = models.CharField( max_length = 300 )
    compania = models.CharField( max_length = 300 )
    sexo = models.IntegerField()
    cumpleanos = models.DateField()
    pais = models.CharField( max_length = 300 )
    ciudad = models.CharField( max_length = 300 )
    lastbounced = models.IntegerField()
    bounced = models.IntegerField()
    email = models.CharField( max_length = 450 )
    status = models.IntegerField()
    unsuscribed = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True )
    class Meta:
        db_table = u'emails_rumbabogota'

class EncuestaElpoint( models.Model ):
    opcion = models.CharField( max_length = 120 )
    ip = models.CharField( max_length = 300 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'encuesta_elpoint'

class Encuestas( models.Model ):
    pregunta = models.CharField( max_length = 750 )
    opcion1 = models.CharField( max_length = 750 )
    opcion2 = models.CharField( max_length = 750 )
    opcion3 = models.CharField( max_length = 750 )
    opcion4 = models.CharField( max_length = 750 )
    opcion5 = models.CharField( max_length = 750 )
    opcion6 = models.CharField( max_length = 750 )
    opcion7 = models.CharField( max_length = 750 )
    opcion8 = models.CharField( max_length = 750 )
    opcion9 = models.CharField( max_length = 750 )
    opcion10 = models.CharField( max_length = 750 )
    r1 = models.CharField( max_length = 750 )
    r2 = models.CharField( max_length = 750 )
    r3 = models.CharField( max_length = 750 )
    r4 = models.CharField( max_length = 750 )
    r5 = models.CharField( max_length = 750 )
    r6 = models.CharField( max_length = 750 )
    r7 = models.CharField( max_length = 750 )
    r8 = models.CharField( max_length = 750 )
    r9 = models.CharField( max_length = 750 )
    r10 = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'encuestas'

class Entrevista( models.Model ):
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    titulo = models.CharField( max_length = 750 )
    subtitulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    titcon = models.CharField( max_length = 750 )
    contenido = models.TextField()
    info = models.CharField( max_length = 750 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'entrevista'

class Erumba( models.Model ):
    asunto = models.CharField( max_length = 240 )
    e_envia = models.CharField( max_length = 120 )
    nombre = models.CharField( max_length = 120 )
    tipo = models.IntegerField()
    html = models.TextField()
    imagen1 = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    url1 = models.CharField( max_length = 750 )
    url2 = models.CharField( max_length = 750 )
    imagen_ext = models.CharField( max_length = 750 )
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    dia1 = models.IntegerField()
    mes1 = models.IntegerField()
    ano1 = models.IntegerField()
    dia2 = models.IntegerField()
    mes2 = models.IntegerField()
    ano2 = models.IntegerField()
    begin = models.CharField( max_length = 750 )
    end = models.CharField( max_length = 750 )
    status = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    imagen3 = models.CharField( max_length = 750, blank = True )
    url3 = models.CharField( max_length = 750, blank = True )
    class Meta:
        db_table = u'erumba'

class Especial( models.Model ):
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    titulo = models.CharField( max_length = 750 )
    subtitulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    titcon = models.CharField( max_length = 750 )
    contenido = models.TextField()
    info = models.CharField( max_length = 750 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'especial'

class Eventos( models.Model ):
    titulo = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 18 )
    dia2 = models.CharField( max_length = 6 )
    mes2 = models.CharField( max_length = 6 )
    ano2 = models.CharField( max_length = 18 )
    dias = models.CharField( max_length = 750 )
    categoria = models.CharField( max_length = 750 )
    imagen = models.CharField( max_length = 750 )
    vestuario = models.CharField( max_length = 750 )
    entrada = models.CharField( max_length = 750 )
    direccion = models.CharField( max_length = 750 )
    local = models.CharField( max_length = 750 )
    url = models.CharField( max_length = 750 )
    email = models.CharField( max_length = 750 )
    jerarquia = models.IntegerField()
    descripcion = models.TextField()
    hora = models.CharField( max_length = 6 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    localn = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    usuario = models.CharField( max_length = 150, blank = True )
    class Meta:
        db_table = u'eventos'

class EventosCategorias( models.Model ):
    id = models.IntegerField( primary_key = True )
    nombre = models.CharField( max_length = 750, blank = True )
    class Meta:
        db_table = u'eventos_categorias'

class EventosMas( models.Model ):
    titulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    pr_link = models.CharField( max_length = 750 )
    rumba_news_pr = models.CharField( max_length = 750 )
    music_news_pr = models.CharField( max_length = 750 )
    entrevista_pr = models.CharField( max_length = 750 )
    especial_pr = models.CharField( max_length = 750 )
    dj_mix_pr = models.CharField( max_length = 750 )
    dj_school_pr = models.CharField( max_length = 750 )
    que_vida_pr = models.CharField( max_length = 750 )
    local_pr = models.CharField( max_length = 750 )
    evento_pr = models.CharField( max_length = 750 )
    local_se1 = models.CharField( max_length = 750 )
    evento_se1 = models.CharField( max_length = 750 )
    local_se2 = models.CharField( max_length = 750 )
    evento_se2 = models.CharField( max_length = 750 )
    encuesta = models.CharField( max_length = 750 )
    evento_fotos = models.CharField( max_length = 750 )
    imagen_evento = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    se1_link = models.CharField( max_length = 750 )
    rumba_news_se1 = models.CharField( max_length = 750 )
    music_news_se1 = models.CharField( max_length = 750 )
    entrevista_se1 = models.CharField( max_length = 750 )
    especial_se1 = models.CharField( max_length = 750 )
    dj_mix_se1 = models.CharField( max_length = 750 )
    dj_school_se1 = models.CharField( max_length = 750 )
    que_vida_se1 = models.CharField( max_length = 750 )
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField( max_length = 750 )
    rumba_news_se2 = models.CharField( max_length = 750 )
    music_news_se2 = models.CharField( max_length = 750 )
    entrevista_se2 = models.CharField( max_length = 750 )
    especial_se2 = models.CharField( max_length = 750 )
    dj_mix_se2 = models.CharField( max_length = 750 )
    dj_school_se2 = models.CharField( max_length = 750 )
    que_vida_se2 = models.CharField( max_length = 750 )
    se2_res = models.TextField()
    se1_imagen = models.CharField( max_length = 750 )
    se2_imagen = models.CharField( max_length = 750 )
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'eventos_mas'

class EventosPor( models.Model ):
    titulo = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 18 )
    dia2 = models.CharField( max_length = 6 )
    mes2 = models.CharField( max_length = 6 )
    ano2 = models.CharField( max_length = 18 )
    dias = models.CharField( max_length = 750 )
    categoria = models.CharField( max_length = 750 )
    imagen = models.CharField( max_length = 750 )
    vestuario = models.CharField( max_length = 750 )
    entrada = models.CharField( max_length = 750 )
    direccion = models.CharField( max_length = 750 )
    local = models.CharField( max_length = 750 )
    url = models.CharField( max_length = 750 )
    email = models.CharField( max_length = 750 )
    jerarquia = models.CharField( max_length = 6 )
    descripcion = models.TextField()
    hora = models.CharField( max_length = 6 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    localn = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'eventos_por'

class Fotografos( models.Model ):
    nombre = models.CharField( max_length = 750 )
    email = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'fotografos'

class Fotos( models.Model ):
    titulo = models.CharField( max_length = 750 )
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    ciudad = models.CharField( max_length = 750 )
    categoria = models.CharField( max_length = 750 )
    lugar = models.CharField( max_length = 750 )
    reportero = models.CharField( max_length = 750 )
    email = models.CharField( max_length = 750 )
    resena = models.TextField()
    directorio = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    imagen_principal = models.CharField( max_length = 750 )
    s_picts = models.CharField( max_length = 750 )
    u_picts = models.CharField( max_length = 750 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'fotos'

class Friends( models.Model ):
    id = models.IntegerField( primary_key = True )
    friendid = models.IntegerField()
    userid = models.IntegerField()
    class Meta:
        db_table = u'friends'

class Fumanchu( models.Model ):
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
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'fumanchu'

class Home( models.Model ):
    id = models.IntegerField( primary_key = True )
    home_title = models.CharField( max_length = 300 )
    home_text = models.TextField()
    class Meta:
        db_table = u'home'

class Invites( models.Model ):
    id = models.IntegerField( primary_key = True )
    post_date = models.DateField()
    postid = models.IntegerField()
    memid = models.IntegerField()
    approved = models.IntegerField()
    class Meta:
        db_table = u'invites'

class Links( models.Model ):
    id = models.IntegerField( primary_key = True )
    regid = models.IntegerField()
    link_title = models.CharField( max_length = 300 )
    link_url = models.CharField( max_length = 300 )
    class Meta:
        db_table = u'links'

class Local( models.Model ):
    nombre = models.CharField( max_length = 750 )
    tipo = models.CharField( max_length = 750 )
    restaurant = models.TextField()
    direccion = models.CharField( max_length = 750 )
    ciudad = models.CharField( max_length = 750 )
    telefono = models.CharField( max_length = 750 )
    fax = models.CharField( max_length = 750 )
    url = models.CharField( max_length = 750 )
    email = models.CharField( max_length = 750 )
    horario = models.CharField( max_length = 750 )
    ambiente = models.CharField( max_length = 750 )
    musica = models.CharField( max_length = 750 )
    dj = models.CharField( max_length = 750 )
    vestuario = models.CharField( max_length = 750 )
    capacidad = models.CharField( max_length = 750 )
    descripcion = models.TextField()
    cerveza_nacional = models.CharField( max_length = 750 )
    cerveza_importada = models.CharField( max_length = 750 )
    trago_nacional = models.CharField( max_length = 750 )
    trago_importado = models.CharField( max_length = 750 )
    whisky_nacional = models.CharField( max_length = 750 )
    whisky_importado = models.CharField( max_length = 750 )
    otros_tragos = models.CharField( max_length = 750 )
    prom_lun_vie = models.CharField( max_length = 750 )
    prom_lun = models.CharField( max_length = 750 )
    prom_mar = models.CharField( max_length = 750 )
    prom_mie = models.CharField( max_length = 750 )
    prom_jue = models.CharField( max_length = 750 )
    prom_vie = models.CharField( max_length = 750 )
    prom_sab = models.CharField( max_length = 750 )
    prom_dom = models.CharField( max_length = 750 )
    prom_info = models.CharField( max_length = 750 )
    prog_lun_vie = models.CharField( max_length = 750 )
    prog_lun = models.CharField( max_length = 750 )
    prog_mar = models.CharField( max_length = 750 )
    prog_mie = models.CharField( max_length = 750 )
    prog_jue = models.CharField( max_length = 750 )
    prog_vie = models.CharField( max_length = 750 )
    prog_sab = models.CharField( max_length = 750 )
    prog_dom = models.CharField( max_length = 750 )
    prog_info = models.CharField( max_length = 750 )
    especialidades = models.CharField( max_length = 750 )
    platos = models.CharField( max_length = 750 )
    comentarios = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 750 )
    mes = models.CharField( max_length = 750 )
    ano = models.CharField( max_length = 750 )
    imagen = models.CharField( max_length = 750 )
    gerente = models.CharField( max_length = 750 )
    contacto = models.CharField( max_length = 750 )
    actualizaciones = models.CharField( max_length = 750 )
    telefonosc = models.CharField( max_length = 750 )
    emailc = models.CharField( max_length = 750 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    user = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'local'

class LogsBouncedMails( models.Model ):
    mail_id = models.BigIntegerField()
    user = models.CharField( max_length = 750 )
    time = models.IntegerField()
    id = models.BigIntegerField( primary_key = True )
    class Meta:
        db_table = u'logs_bounced_mails'

class LogsOpenedMails( models.Model ):
    mail_id = models.BigIntegerField()
    user = models.CharField( max_length = 750 )
    time = models.IntegerField()
    id = models.BigIntegerField( primary_key = True )
    class Meta:
        db_table = u'logs_opened_mails'

class LogsUrlClick( models.Model ):
    mail_id = models.BigIntegerField()
    user = models.CharField( max_length = 750 )
    url = models.CharField( max_length = 750 )
    time = models.IntegerField()
    id = models.BigIntegerField( primary_key = True )
    class Meta:
        db_table = u'logs_url_click'

class Mail( models.Model ):
    email = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'mail'

class Mailing( models.Model ):
    email = models.TextField()
    class Meta:
        db_table = u'mailing'

class MamiPapi( models.Model ):
    nombre = models.CharField( max_length = 750 )
    ocupacion = models.CharField( max_length = 750 )
    edad = models.CharField( max_length = 750 )
    genero = models.CharField( max_length = 750 )
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    directorio = models.CharField( max_length = 750 )
    imagen = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'mami_papi'

class MamiPapi2( models.Model ):
    nombre = models.CharField( max_length = 750 )
    ocupacion = models.CharField( max_length = 750 )
    edad = models.CharField( max_length = 750 )
    genero = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 750 )
    mes = models.CharField( max_length = 750 )
    ano = models.CharField( max_length = 750 )
    directorio = models.CharField( max_length = 750 )
    imagen = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'mami_papi2'

class MamiVista( models.Model ):
    vista = models.BigIntegerField()
    ranking = models.CharField( max_length = 750 )
    mami_papi = models.CharField( max_length = 750 )
    tiempo = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'mami_vista'

class Minisites( models.Model ):
    id = models.IntegerField( primary_key = True )
    sitio = models.TextField()
    plantilla = models.TextField()
    articulo = models.IntegerField()
    class Meta:
        db_table = u'minisites'

class MotoEventos( models.Model ):
    nombre = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'moto_eventos'

class MotoFotos( models.Model ):
    foto = models.TextField()
    numero = models.IntegerField()
    evento = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'moto_fotos'

class MotoVotos( models.Model ):
    email = models.CharField( max_length = 750 )
    foto = models.IntegerField()
    evento = models.IntegerField()
    puntos = models.IntegerField()
    foto_id = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'moto_votos'

class MusicNews( models.Model ):
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    titulo = models.CharField( max_length = 750 )
    subtitulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    titcon = models.CharField( max_length = 750 )
    contenido = models.TextField()
    info = models.CharField( max_length = 750 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'music_news'

class Newsletters( models.Model ):
    db = models.CharField( max_length = 900, blank = True )
    subject = models.CharField( max_length = 2250, blank = True )
    body = models.TextField( blank = True )
    fixed_body = models.TextField( blank = True )
    time = models.IntegerField( null = True, blank = True )
    sent_start = models.IntegerField()
    sent_finish = models.IntegerField()
    total = models.IntegerField()
    sent = models.IntegerField()
    fail = models.IntegerField()
    id = models.IntegerField( primary_key = True )
    class Meta:
        db_table = u'newsletters'

class NewslettersBounced( models.Model ):
    email = models.CharField( max_length = 450, blank = True )
    lbounced = models.IntegerField( null = True, blank = True )
    n_id = models.IntegerField( null = True, blank = True )
    tries = models.IntegerField( null = True, blank = True )
    class Meta:
        db_table = u'newsletters_bounced'

class NewslettersUnsuscribeds( models.Model ):
    email = models.CharField( max_length = 540, blank = True )
    time = models.IntegerField( null = True, blank = True )
    class Meta:
        db_table = u'newsletters_unsuscribeds'

class NokiaFoto( models.Model ):
    email = models.CharField( max_length = 750 )
    historia = models.TextField()
    file = models.CharField( max_length = 750 )
    time = models.IntegerField()
    status = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'nokia_foto'

class NokiaReg( models.Model ):
    nombre = models.CharField( max_length = 750 )
    fnacimiento = models.DateField()
    email = models.CharField( max_length = 750 )
    optin = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'nokia_reg'

class Otros( models.Model ):
    email = models.CharField( max_length = 750 )
    stats = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'otros'

class PapiVisto( models.Model ):
    vista = models.CharField( max_length = 750 )
    ranking = models.CharField( max_length = 750 )
    mami_papi = models.CharField( max_length = 750 )
    tiempo = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'papi_visto'

class Pautas( models.Model ):
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    evento = models.CharField( max_length = 750 )
    fotografos = models.CharField( max_length = 750 )
    comentario = models.TextField()
    hora = models.IntegerField()
    hora_r = models.CharField( max_length = 6 )
    direccion = models.CharField( max_length = 750 )
    time = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'pautas'

class Photocoments( models.Model ):
    id = models.IntegerField( primary_key = True )
    photoid = models.IntegerField()
    postid = models.IntegerField()
    coment = models.TextField()
    com_date = models.DateField()
    approved = models.IntegerField()
    class Meta:
        db_table = u'photocoments'

class Photos( models.Model ):
    id = models.IntegerField( primary_key = True )
    regid = models.IntegerField()
    pathtophoto = models.CharField( max_length = 300 )
    leyenda = models.CharField( max_length = 750 )
    view = models.BigIntegerField()
    class Meta:
        db_table = u'photos'

class Principal( models.Model ):
    dia = models.CharField( max_length = 750 )
    mes = models.CharField( max_length = 750 )
    ano = models.CharField( max_length = 750 )
    local_dia = models.CharField( max_length = 750 )
    local_link = models.CharField( max_length = 750 )
    evento_local = models.CharField( max_length = 750 )
    local_des = models.TextField()
    ev_titulo = models.CharField( max_length = 750 )
    ev_evento = models.CharField( max_length = 750 )
    pr_titulo = models.CharField( max_length = 750 )
    pr_des = models.TextField()
    se1_titulo = models.CharField( max_length = 750 )
    se1_des = models.TextField()
    se2_titulo = models.CharField( max_length = 750 )
    se2_des = models.TextField()
    se3_titulo = models.CharField( max_length = 750 )
    se3_des = models.TextField()
    se4_titulo = models.CharField( max_length = 750 )
    se4_des = models.TextField()
    imagen_pr = models.CharField( max_length = 750 )
    imagen_se1 = models.CharField( max_length = 750 )
    imagen_se2 = models.CharField( max_length = 750 )
    imagen_se3 = models.CharField( max_length = 750 )
    imagen_se4 = models.CharField( max_length = 750 )
    imagen_ev1 = models.CharField( max_length = 750 )
    imagen_ev2 = models.CharField( max_length = 750 )
    imagen_ev3 = models.CharField( max_length = 750 )
    pr_link = models.CharField( max_length = 750 )
    rumba_news_pr = models.CharField( max_length = 750 )
    music_news_pr = models.CharField( max_length = 750 )
    entrevista_pr = models.CharField( max_length = 750 )
    especial_pr = models.CharField( max_length = 750 )
    dj_mix_pr = models.CharField( max_length = 750 )
    dj_school_pr = models.CharField( max_length = 750 )
    que_vida_pr = models.CharField( max_length = 750 )
    local_pr = models.CharField( max_length = 750 )
    evento_pr = models.CharField( max_length = 750 )
    se1_link = models.CharField( max_length = 750 )
    rumba_news_se1 = models.CharField( max_length = 750 )
    music_news_se1 = models.CharField( max_length = 750 )
    entrevista_se1 = models.CharField( max_length = 750 )
    especial_se1 = models.CharField( max_length = 750 )
    dj_mix_se1 = models.CharField( max_length = 750 )
    dj_school_se1 = models.CharField( max_length = 750 )
    que_vida_se1 = models.CharField( max_length = 750 )
    local_se1 = models.CharField( max_length = 750 )
    evento_se1 = models.CharField( max_length = 750 )
    se2_link = models.CharField( max_length = 750 )
    rumba_news_se2 = models.CharField( max_length = 750 )
    music_news_se2 = models.CharField( max_length = 750 )
    entrevista_se2 = models.CharField( max_length = 750 )
    especial_se2 = models.CharField( max_length = 750 )
    dj_mix_se2 = models.CharField( max_length = 750 )
    dj_school_se2 = models.CharField( max_length = 750 )
    que_vida_se2 = models.CharField( max_length = 750 )
    local_se2 = models.CharField( max_length = 750 )
    evento_se2 = models.CharField( max_length = 750 )
    se3_link = models.CharField( max_length = 750 )
    rumba_news_se3 = models.CharField( max_length = 750 )
    music_news_se3 = models.CharField( max_length = 750 )
    entrevista_se3 = models.CharField( max_length = 750 )
    especial_se3 = models.CharField( max_length = 750 )
    dj_mix_se3 = models.CharField( max_length = 750 )
    dj_school_se3 = models.CharField( max_length = 750 )
    que_vida_se3 = models.CharField( max_length = 750 )
    local_se3 = models.CharField( max_length = 750 )
    evento_se3 = models.CharField( max_length = 750 )
    se4_link = models.CharField( max_length = 750 )
    rumba_news_se4 = models.CharField( max_length = 750 )
    music_news_se4 = models.CharField( max_length = 750 )
    entrevista_se4 = models.CharField( max_length = 750 )
    especial_se4 = models.CharField( max_length = 750 )
    dj_mix_se4 = models.CharField( max_length = 750 )
    dj_school_se4 = models.CharField( max_length = 750 )
    que_vida_se4 = models.CharField( max_length = 750 )
    local_se4 = models.CharField( max_length = 750 )
    evento_se4 = models.CharField( max_length = 750 )
    fotosv_pr = models.CharField( max_length = 750 )
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    fotosv_se3 = models.BigIntegerField()
    fotosv_se4 = models.BigIntegerField()
    fotos_pr = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'principal'

class PrintDominos( models.Model ):
    fecha = models.IntegerField()
    ip = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'print_dominos'

class QueVida( models.Model ):
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    titulo = models.CharField( max_length = 750 )
    subtitulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    titcon = models.CharField( max_length = 750 )
    contenido = models.TextField()
    info = models.CharField( max_length = 750 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'que_vida'

class Ranking( models.Model ):
    tabla = models.CharField( max_length = 750 )
    id_tabla = models.BigIntegerField()
    ip = models.CharField( max_length = 750, db_column = 'IP' ) # Field name made lowercase.
    user = models.BigIntegerField()
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    voto = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'ranking'

class Rate( models.Model ):
    id = models.IntegerField( primary_key = True )
    photoid = models.IntegerField()
    memid = models.IntegerField()
    rate = models.IntegerField()
    class Meta:
        db_table = u'rate'

class RateLocales( models.Model ):
    db = models.IntegerField()
    local = models.BigIntegerField()
    user = models.BigIntegerField()
    class Meta:
        db_table = u'rate_locales'

class RateRumbas( models.Model ):
    db = models.IntegerField()
    rumba = models.BigIntegerField()
    user = models.BigIntegerField()
    class Meta:
        db_table = u'rate_rumbas'

class RegControl( models.Model ):
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'reg_control'

class Registration( models.Model ):
    id = models.IntegerField( primary_key = True )
    nombre = models.CharField( max_length = 300 )
    apellido = models.CharField( max_length = 300 )
    telefono_contacto = models.CharField( max_length = 300 )
    email = models.CharField( max_length = 300 )
    direccion = models.TextField()
    estado = models.CharField( max_length = 300 )
    codigo_postal = models.CharField( max_length = 300 )
    dia = models.CharField( max_length = 300 )
    mes = models.CharField( max_length = 300 )
    ano = models.CharField( max_length = 300 )
    sexo = models.CharField( max_length = 300 )
    pais = models.CharField( max_length = 300 )
    codigo = models.CharField( max_length = 300 )
    celular = models.CharField( max_length = 300 )
    user = models.CharField( max_length = 300 )
    pass_field = models.CharField( max_length = 300, db_column = 'pass' ) # Field renamed because it was a Python reserved word.
    directorio = models.CharField( max_length = 300 )
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
    nick = models.CharField( max_length = 300 )
    me_gusta = models.TextField()
    edad = models.CharField( max_length = 300 )
    cumpleanos = models.CharField( max_length = 300 )
    estatus = models.TextField()
    estoy_buscando = models.TextField()
    me_encuentro_en = models.TextField()
    sobre_mi = models.TextField()
    quisiera_conocer = models.TextField()
    intereses = models.TextField()
    musica_favorita = models.TextField()
    artistas = models.TextField()
    peliculas_favoritas = models.TextField()
    avatar = models.CharField( max_length = 300 )
    feat = models.IntegerField()
    class Meta:
        db_table = u'registration'

class ResMoto( models.Model ):
    foto = models.BigIntegerField()
    votos = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'res_moto'

class ResMotoUser( models.Model ):
    email = models.CharField( max_length = 750 )
    votos = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'res_moto_user'

class RumbaNews( models.Model ):
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    titulo = models.CharField( max_length = 750 )
    subtitulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    imagen2 = models.CharField( max_length = 750 )
    titcon = models.CharField( max_length = 750 )
    contenido = models.TextField()
    info = models.CharField( max_length = 750 )
    da = models.IntegerField()
    ma = models.IntegerField()
    aa = models.IntegerField()
    du = models.IntegerField()
    mu = models.IntegerField()
    au = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'rumba_news'

class Rumbas( models.Model ):
    titulo = models.CharField( max_length = 750 )
    imagen1 = models.CharField( max_length = 750 )
    pr_link = models.CharField( max_length = 750 )
    rumba_news_pr = models.CharField( max_length = 750 )
    music_news_pr = models.CharField( max_length = 750 )
    entrevista_pr = models.CharField( max_length = 750 )
    especial_pr = models.CharField( max_length = 750 )
    dj_mix_pr = models.CharField( max_length = 750 )
    dj_school_pr = models.CharField( max_length = 750 )
    que_vida_pr = models.CharField( max_length = 750 )
    local_pr = models.CharField( max_length = 750 )
    evento_pr = models.CharField( max_length = 750 )
    local_se1 = models.CharField( max_length = 750 )
    evento_se1 = models.CharField( max_length = 750 )
    local_se2 = models.CharField( max_length = 750 )
    evento_se2 = models.CharField( max_length = 750 )
    encuesta = models.CharField( max_length = 750 )
    evento_fotos = models.CharField( max_length = 750 )
    imagen_evento = models.CharField( max_length = 750 )
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    se1_link = models.CharField( max_length = 750 )
    rumba_news_se1 = models.CharField( max_length = 750 )
    music_news_se1 = models.CharField( max_length = 750 )
    entrevista_se1 = models.CharField( max_length = 750 )
    especial_se1 = models.CharField( max_length = 750 )
    dj_mix_se1 = models.CharField( max_length = 750 )
    dj_school_se1 = models.CharField( max_length = 750 )
    que_vida_se1 = models.CharField( max_length = 750 )
    se1_res = models.TextField()
    contenido = models.TextField()
    se2_link = models.CharField( max_length = 750 )
    rumba_news_se2 = models.CharField( max_length = 750 )
    music_news_se2 = models.CharField( max_length = 750 )
    entrevista_se2 = models.CharField( max_length = 750 )
    especial_se2 = models.CharField( max_length = 750 )
    dj_mix_se2 = models.CharField( max_length = 750 )
    dj_school_se2 = models.CharField( max_length = 750 )
    que_vida_se2 = models.CharField( max_length = 750 )
    se2_res = models.TextField()
    se1_imagen = models.CharField( max_length = 750 )
    se2_imagen = models.CharField( max_length = 750 )
    fotosv_pr = models.BigIntegerField()
    fotosv_se1 = models.BigIntegerField()
    fotosv_se2 = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'rumbas'

class Secciones( models.Model ):
    imagen = models.CharField( max_length = 750 )
    titulo = models.CharField( max_length = 750 )
    descripcion = models.TextField()
    vinculo = models.CharField( max_length = 750 )
    vinculo_externo = models.CharField( max_length = 750 )
    vinculo_externo_tipo = models.CharField( max_length = 750 )
    vinculo_externo_target = models.CharField( max_length = 750 )
    vinculo_local = models.CharField( max_length = 750 )
    vinculo_seccion = models.CharField( max_length = 750 )
    vinculo_evento = models.CharField( max_length = 750 )
    pagina = models.CharField( max_length = 750 )
    numero = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'secciones'

class Topdjsreg( models.Model ):
    nombre = models.CharField( max_length = 750 )
    apellido = models.CharField( max_length = 750 )
    email = models.CharField( max_length = 750 )
    telefono = models.IntegerField()
    email_md5 = models.CharField( max_length = 750 )
    v1 = models.BigIntegerField()
    v2 = models.BigIntegerField()
    v3 = models.BigIntegerField()
    v4 = models.BigIntegerField()
    v5 = models.BigIntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'topdjsreg'

class Tusfotos( models.Model ):
    dia = models.CharField( max_length = 6 )
    mes = models.CharField( max_length = 6 )
    ano = models.CharField( max_length = 12 )
    archivo = models.CharField( max_length = 750 )
    usuario = models.CharField( max_length = 750 )
    leyenda = models.CharField( max_length = 750 )
    visitas = models.BigIntegerField()
    status = models.IntegerField()
    user_id = models.BigIntegerField()
    user_name = models.CharField( max_length = 750 )
    thumbnail = models.TextField()
    day = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'tusfotos'

class UserAnun( models.Model ):
    user = models.CharField( max_length = 750 )
    pass_field = models.CharField( max_length = 750, db_column = 'pass' ) # Field renamed because it was a Python reserved word.
    email = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'user_anun'

class UserMoto( models.Model ):
    nombre = models.CharField( max_length = 750 )
    apellido = models.CharField( max_length = 750 )
    ci = models.CharField( max_length = 750 )
    email = models.CharField( max_length = 750 )
    telefono = models.CharField( max_length = 750 )
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'user_moto'

class Users( models.Model ):
    email = models.CharField( max_length = 750 )
    status = models.IntegerField()
    id = models.IntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'users'

class Usuarios( models.Model ):
    nombre = models.CharField( max_length = 300 )
    apellido = models.CharField( max_length = 300 )
    telefono_contacto = models.CharField( max_length = 300 )
    email = models.CharField( max_length = 300 )
    direccion = models.TextField()
    estado = models.CharField( max_length = 300 )
    codigo_postal = models.CharField( max_length = 300 )
    dia = models.CharField( max_length = 300 )
    mes = models.CharField( max_length = 300 )
    ano = models.CharField( max_length = 300 )
    sexo = models.CharField( max_length = 300 )
    pais = models.CharField( max_length = 300 )
    ciudad = models.CharField( max_length = 300 )
    codigo = models.CharField( max_length = 300 )
    celular = models.CharField( max_length = 300 )
    user = models.CharField( max_length = 300 )
    pass_field = models.CharField( max_length = 300, db_column = 'pass' ) # Field renamed because it was a Python reserved word.
    directorio = models.CharField( max_length = 300 )
    status = models.IntegerField()
    dia2 = models.IntegerField()
    mes2 = models.IntegerField()
    ano2 = models.IntegerField()
    comentario = models.TextField()
    youtube = models.TextField()
    stars = models.IntegerField()
    imagen_principal = models.TextField()
    imagen_original = models.TextField()
    nick = models.CharField( max_length = 300 )
    me_gusta = models.TextField()
    edad = models.CharField( max_length = 300 )
    cumpleanos = models.CharField( max_length = 300 )
    estatus = models.TextField()
    estoy_buscando = models.TextField()
    me_encuentro_en = models.TextField()
    sobre_mi = models.TextField()
    quisiera_conocer = models.TextField()
    intereses = models.TextField()
    musica_favorita = models.TextField()
    artistas = models.TextField()
    peliculas_favoritas = models.TextField()
    avatar = models.CharField( max_length = 300 )
    feat = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    fumas = models.CharField( max_length = 6 )
    bebes = models.CharField( max_length = 6 )
    class Meta:
        db_table = u'usuarios'

class Usuarios2( models.Model ):
    nombre = models.CharField( max_length = 300 )
    apellido = models.CharField( max_length = 300 )
    telefono_contacto = models.CharField( max_length = 300 )
    email = models.CharField( max_length = 300 )
    direccion = models.TextField()
    estado = models.CharField( max_length = 300 )
    codigo_postal = models.CharField( max_length = 300 )
    dia = models.CharField( max_length = 300 )
    mes = models.CharField( max_length = 300 )
    ano = models.CharField( max_length = 300 )
    sexo = models.CharField( max_length = 300 )
    pais = models.CharField( max_length = 300 )
    ciudad = models.CharField( max_length = 300 )
    codigo = models.CharField( max_length = 300 )
    celular = models.CharField( max_length = 300 )
    user = models.CharField( max_length = 300 )
    pass_field = models.CharField( max_length = 300, db_column = 'pass' ) # Field renamed because it was a Python reserved word.
    directorio = models.CharField( max_length = 300 )
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
    nick = models.CharField( max_length = 300 )
    me_gusta = models.TextField()
    edad = models.CharField( max_length = 300 )
    cumpleanos = models.CharField( max_length = 300 )
    estatus = models.TextField()
    estoy_buscando = models.TextField()
    me_encuentro_en = models.TextField()
    sobre_mi = models.TextField()
    quisiera_conocer = models.TextField()
    intereses = models.TextField()
    musica_favorita = models.TextField()
    artistas = models.TextField()
    peliculas_favoritas = models.TextField()
    avatar = models.CharField( max_length = 300 )
    feat = models.IntegerField()
    id = models.BigIntegerField( primary_key = True, db_column = 'ID' ) # Field name made lowercase.
    class Meta:
        db_table = u'usuarios2'

