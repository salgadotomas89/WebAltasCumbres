from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ClearableFileInput

from colegio.models import ImagesNoticia, Noticia, Evento, Profesor


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    mensaje = forms.CharField(widget=forms.Textarea, max_length=2000)


class FormNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "subtitulo","lead","texto","redactor", "tituloDestacado","destacado"]

class ImagesFormNoticia(FormNoticia): #extending form
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(FormNoticia.Meta):
        fields = FormNoticia.Meta.fields + ['images',]


class FormProfesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ["nombre", "apellido", "profesion", "ciclo", "foto", "correo", "universidad"]


class FormEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ["fecha", "titulo", "texto"]

        