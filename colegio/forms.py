from django import forms
from django.forms import ClearableFileInput

from colegio.models import Noticia, Evento, Profesor


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    mensaje = forms.CharField(widget=forms.Textarea, max_length=2000)


class FormNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "subtitulo","lead","texto", "documento","redactor", "tituloDestacado","destacado"]
        widgets = {
         'documento': ClearableFileInput(attrs={'multiple': True}),
        }


class FormProfesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ["nombre", "apellido", "profesion", "ciclo", "foto", "correo", "universidad"]


class FormEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ["fecha", "titulo", "texto"]

