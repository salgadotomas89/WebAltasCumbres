from email.policy import default
from operator import mod
from pyexpat import model
from django.db import models
from django.conf import settings
from django.utils import timezone
import os


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, default=" ")
    lead = models.CharField(max_length=1000, default=" ")
    texto = models.CharField(max_length=1000, default='SOME ')
    date = models.DateTimeField(default=timezone.now)
    redactor = models.CharField(max_length=200, default='Tomás Salgado')
    tituloDestacado = models.CharField(max_length=100, default=" ")
    destacado = models.CharField(max_length=1000, default="")
    galeria = models.BooleanField(default=False)


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

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    alergico = models.CharField(max_length=100, default='no es alergico')


class Guia(models.Model):
    profesor = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100, default= '10')
    fecha_subida = models.DateTimeField(default=timezone.now)
    documento = models.FileField(upload_to='guias')
    curso = models.CharField(max_length=100, default="sin curso")

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.documento.name))
        super(Guia,self).delete(*args,**kwargs)



    
