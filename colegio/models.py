from email.policy import default
from operator import mod
from pyexpat import model
from django.db import models
from django.conf import settings
from django.utils import timezone
import os


#noticia que tiene sus componentes correspondientes. galeria significa que esta noticia pasa
#a estar en la galeria de fotos, cuando la noticia tenga varias fotos.
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200,blank=True, null=True, default=" ")
    lead = models.CharField(max_length=1000,blank=True, null=True, default=" ")
    texto = models.CharField(max_length=1000, default='SOME')
    date = models.DateTimeField(default=timezone.now)
    redactor = models.CharField(max_length=200,blank=True, null=True, default='Tomás Salgado')
    tituloDestacado = models.CharField(max_length=100, blank=True, null=True, default=" ")
    destacado = models.CharField(max_length=1000, blank=True, null=True , default=" ")
    galeria = models.BooleanField(default=False)

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


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, null=False, default='sin dirección')
    fono = models.CharField(max_length=20,blank=False, null=False, default='0')
    curso = models.CharField(max_length=100,blank=False, null=False, default='0')
    alergico = models.CharField(max_length=100,blank=True, null=True, default='no es alergico')

    def __str__(self):
        return self.nombre
    
    


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



    
