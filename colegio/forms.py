from dataclasses import fields
from django import forms
from pymysql import NULL

from colegio.models import Alumno, Asistente, Comunicado, Guia,Book, Noticia, Evento, Profesor


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    mensaje = forms.CharField(widget=forms.Textarea, max_length=2000)

class FormProfesor(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profesor
        fields = ["nombre", "apellido","profesion", "ciclo", "foto", "correo", "universidad", 'password']

class FormLibro(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        

class FormAsistente(forms.ModelForm):
    class Meta:
        model = Asistente
        fields = ["nombre", "apellido", "profesion", "ciclo", "foto", "correo", "universidad"]


class FormEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ["fecha", "titulo", "texto"]

class FormGuia(forms.ModelForm):
    class Meta:
        model = Guia
        fields = ["profesor", "fecha", "documento",'cantidad', "curso",]

class Curso(forms.ModelForm):
    class Meta:
        model = Guia
        fields = '__all__'

class FormAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class FormNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "subtitulo","texto","redactor", "tituloDestacado","destacado", "galeria"]

class ImagesFormNoticia(FormNoticia): #extending form
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(FormNoticia.Meta):
        fields = FormNoticia.Meta.fields + ['images',]

class FormComunicado(forms.ModelForm):
    class Meta:
        model = Comunicado
        fields = ["titulo", "texto", "autor"]

class ArchivosFormComunicado(FormComunicado): #extending form
    archivos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(FormComunicado.Meta):
        fields = FormComunicado.Meta.fields + ['archivos',]


    


        