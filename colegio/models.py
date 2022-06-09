from distutils.command.upload import upload
from email.policy import default
from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
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


class Alumno(models.Model):
    #antecedentes personales
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    puebloOriginario = models.BooleanField(default='no', blank=True)
    edad = models.IntegerField(default=0, blank=True)
    fechaNacimiento = models.DateTimeField(default=timezone.now)
    sexo = models.CharField(max_length=100)
    alergico = models.CharField(max_length=100, default='no', blank=True)
    direccion = models.CharField(max_length=100)
    fono = models.CharField(max_length=20)
    #antecedentes escolares
    procedencia = models.CharField(max_length=100)
    reprobado = models.CharField(max_length=100)
    fechaIncorporacion = models.DateTimeField(default=timezone.now)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default='1', blank=True)
    
    
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



