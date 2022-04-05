from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ClearableFileInput
from pymysql import NULL

from colegio.models import Alumno, Asistente, Guia, Noticia, Evento, Profesor


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    mensaje = forms.CharField(widget=forms.Textarea, max_length=2000)


class FormNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "subtitulo","lead","texto","redactor", "tituloDestacado","destacado", "galeria"]

class ImagesFormNoticia(FormNoticia): #extending form
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(FormNoticia.Meta):
        fields = FormNoticia.Meta.fields + ['images',]


class FormProfesor(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profesor
        fields = ["nombre", "apellido","profesion", "ciclo", "foto", "correo", "universidad", 'password']
        

class FormAsistente(forms.ModelForm):
    class Meta:
        model = Asistente
        fields = ["nombre", "apellido", "profesion", "ciclo", "foto", "correo", "universidad"]


class FormAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'curso', 'alergico', 'fono', 'direccion']


class FormEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ["fecha", "titulo", "texto"]

class FormGuia(forms.ModelForm):
    class Meta:
        model = Guia
        fields = ["profesor", "fecha", "documento",'cantidad', "curso",]
    


        