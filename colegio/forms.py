from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pymysql import NULL
from colegio import models
from colegio.models import Alumno , Boletin, Evaluacion, Amigo, Apoderado, Asistente, Comunicado, Guia,Book, Noticia, Madre ,Evento, Padre, Profesor, Taller, Inscripcion, Tenista


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    mensaje = forms.CharField(widget=forms.Textarea, max_length=2000)


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }

    
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

class FormApoderado(forms.ModelForm):
    class Meta:
        model = Apoderado
        fields = '__all__'

class FormAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class FormPadre(forms.ModelForm):
    class Meta:
        model = Padre
        fields = '__all__'

class FormTutor(forms.ModelForm):
    class Meta:
        model = models.Tutor
        fields = '__all__'

class FormMadre(forms.ModelForm):
    class Meta:
        model = Madre
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


class FormAmigo(forms.ModelForm):
    class Meta:
        model = Amigo
        fields = '__all__'

class FormTaller(forms.ModelForm):
    class Meta:
        model = Taller
        fields = '__all__'

class FormInscripcion(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'

class FormEvaluacion(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = '__all__'
        

class FormTenista(forms.ModelForm):
    class Meta:
        model = Tenista
        fields = ["nombre", "curso"]


class FormBoletin(forms.ModelForm):
    class Meta:
        model = Boletin
        fields = ["fecha", "archivo", "autor"]
