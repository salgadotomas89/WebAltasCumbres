from distutils.command.upload import upload
from email.policy import default
from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.forms import BooleanField, CharField
from django.utils import timezone
import os

#noticia que tiene sus componentes correspondientes. galeria significa que esta noticia pasa
#a estar en la galeria de fotos, cuando la noticia tenga varias fotos.
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200,blank=True, null=True, default=" ")
    texto = models.CharField(max_length=1000,blank=True, null=True, default=' ')
    date = models.DateTimeField(default=timezone.now)
    redactor = models.CharField(max_length=200,blank=True, null=True, default='Tomás Salgado')
    tituloDestacado = models.CharField(max_length=100, blank=True, null=True, default=" ")
    destacado = models.CharField(max_length=1000, blank=True, null=True , default=" ")
    galeria = models.BooleanField(default=False)
    noticia = models.BooleanField(default=True)


#modelo que contiene una foto relacionada a una noticia con clave foranea
class ImagesNoticia(models.Model):
    noticia = models.ForeignKey(Noticia,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='noticias',null=True,blank=True)


class Evento(models.Model):
    fecha = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    texto = models.CharField(max_length=600)


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100, default='profesor')
    ciclo = models.IntegerField(default=3)
    universidad = models.CharField(max_length=100, default='-')
    correo = models.CharField(max_length=200, default='sin correo')
    foto = models.ImageField(upload_to='profesores')
    password = models.CharField(max_length=100, default='altascumbres')

    def __str__(self):
        return f"{self.nombre}"


class Book(models.Model):
    nombre = models.TextField()
    tema = models.TextField(default='')
    autor = models.TextField()
    isbn = models.TextField()
    editorial = models.TextField()
    resumen = models.TextField(blank=True)
    foto = models.ImageField(upload_to='libros', blank=True)
    cantidad = models.IntegerField(default=1, blank=True, null=True)


#este modelo llamado asistente, engloba a todos los trabajadores que no son profesores en el establecimiento o que son profesores
#pero desempeñan otro trabajo
class Asistente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100, default='asistente de la educación')
    ciclo = models.IntegerField(default=4)
    universidad = models.CharField(max_length=100, default='-')
    correo = models.CharField(max_length=200, default='sin correo')
    foto = models.ImageField(upload_to='asistentes')

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    profesorJefe = models.OneToOneField(Profesor, on_delete=models.CASCADE, null=True, blank=True)

class Padre(models.Model):
    participacion = BooleanField()
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    estadoCivil = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=100)
    lugarTrabajo = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    fechaNacimiento = models.DateTimeField(default=timezone.now)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Madre(models.Model):
    participacion = BooleanField()
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    estadoCivil = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=100)
    lugarTrabajo = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    fechaNacimiento = models.DateTimeField(default=timezone.now)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Tutor(models.Model):
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    trabajo = models.CharField(max_length=200)

class Apoderado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=200, default='padre')
    direccion = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

class Alumno(models.Model):
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE, null=True, blank=True)
    #antecedentes estudiante
    nombre = models.CharField(max_length=100)
    paterno = models.CharField(max_length=100, null=True)
    materno = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100, blank=True, default='chilena')
    puebloOriginario = models.BooleanField(default='no', blank=True)
    edad = models.IntegerField(default=0, blank=True)
    fechaNacimiento = models.DateTimeField(default=timezone.now)
    sexo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    #antecedentes academicos
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    procedencia = models.CharField(max_length=200, blank=True)
    fechaIncorporacion = models.DateTimeField(default=timezone.now)
    religion = models.CharField(max_length=200, blank='True')
    reprobado = models.CharField(max_length=200, blank='True', default='No')
    hermanos = models.CharField(max_length=200,blank=True, default='No')
    #antecedentes sociales y del aprendizaje
    socioeconomica = models.TextField(max_length=200, null=True)
    beca = models.CharField(max_length=200, blank=True, default='no posee')
    pie = models.CharField(max_length=200, blank=True, default='no pertenece')
    #antecedentes de salud
    enfermedades = models.CharField(max_length=100, default='no', blank=True)
    alergico = models.CharField(max_length=100, default='no', blank=True)
    vision = models.CharField(max_length=100, default='normal', blank=True)
    lentes = models.CharField(max_length=100, default='no', blank=True)
    audicion = models.CharField(max_length=100, default='no', blank=True)
    audifonos = models.CharField(max_length=100, default='no', blank=True)
    sanguineo = models.CharField(max_length=100,  blank=True)
    salud = models.CharField(max_length=100, default='AFP', blank=True)
    peso = models.CharField(max_length=100, blank=True)
    talla = models.CharField(max_length=100, blank=True)
    problema = models.CharField(max_length=100, default='no', blank=True)
    emergencia = models.CharField(max_length=100, blank=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True)
    padre = models.ForeignKey(Padre, on_delete=models.CASCADE, null=True, blank=True)
    madre = models.ForeignKey(Madre, on_delete=models.CASCADE, null=True, blank=True)


    
#guia es el documento que envian los profesores o asistentes a imprimir
class Guia(models.Model):
    profesor = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100,blank=True, null=True, default= '10')
    fecha_subida = models.DateTimeField(default=timezone.now)
    documento = models.FileField(upload_to='guias')
    curso = models.CharField(max_length=100, default="sin curso")
    estado = models.CharField(max_length=100, default="por imprimir" )

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.documento.name))
        super(Guia,self).delete(*args,**kwargs)


class Reserva(models.Model):
    dia = models.CharField(max_length=100)
    bloque = models.IntegerField(default=0)

class Comunicado(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100, default='Mauricio Orellana', null=True, blank=True)
    texto = models.TextField(max_length=1000)

class ArchivosComunicado(models.Model):
    comunicado = models.ForeignKey(Comunicado,on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='comunicados',null=True,blank=True)



