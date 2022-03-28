import mimetypes
import os
from django.conf import settings

from urllib.request import Request

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, FormAlumno, FormNoticia, FormEvento, FormProfesor, FormGuia
from datetime import datetime

# Create your views here.
from .models import Guia, ImagesNoticia, Noticia, Evento, Profesor


def show_pdf(request):
    filepath = os.path.join('static', 'PEI.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def show_rc(request):
    filepath = os.path.join('static', 'RC.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def show_rice(request):
    filepath = os.path.join('static', 'RICE.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def show_eva(request):
    filepath = os.path.join('static', 'EVA.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def index(request):
    context = {}
    noticias = Noticia.objects.all()  # traigo todas las noticias
    for news in noticias:  # recorro cada noticia
        news.date = dame_formato(news.date)  # actualizo su formato de fecha
    # add the dictionary during initialization

    lista_profesores = Profesor.objects.all()



    context["profesores"] = lista_profesores
    context["noticias"] = noticias
    context["eventos"] = Evento.objects.all()

    if len(lista_profesores) >= 4:
        ultimos_profesores = [lista_profesores[len(lista_profesores) -1], lista_profesores[len(lista_profesores) -2],
                              lista_profesores[len(lista_profesores) -3]]
        context["profesores"] = ultimos_profesores

    if len(noticias) >= 5:
        ultimas_noticias = [noticias[len(noticias) - 1], noticias[len(noticias) - 2], noticias[len(noticias) - 3],
                            noticias[len(noticias) - 4]]
        context["noticias"] = ultimas_noticias

    return render(request, "index.html", context)


def dame_formato(date):
    formato = "%d %b %Y"
    return date.strftime(formato)


def reglamentos(request):
    return render(request, 'reglamentos.html')

def perfil(request):

    return(request, 'perfil.html')


def pedidos(request):
    context = {}

    cursos = {'primero' : 29, 'segundo' : 31, 'tercero' : 35, 'cuarto' : 26, 'quinto':31, 'sexto': 25, 'septimo' : 18}

    lista_guias = Guia.objects.all()  # traigo todas las guias


    return render(request, 'pedidos.html', {'guias':lista_guias, 'cursos':cursos})


def proyecto(request):
    return render(request, 'proyecto.html')


def directiva(request):
    return render(request, 'directiva.html')


def mision(request):
    return render(request, 'mision.html')


def vision(request):
    return render(request, 'vision.html')


def profesor(request):
    if request.method == 'POST':
        form = FormProfesor(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save()
        else:
            print("error al ingresar profesor")

    return render(request, 'profesor.html')


def imprimir(request):

    if request.method == 'POST':
        guia = FormGuia(request.POST, request.FILES)
        

        if guia.is_valid():
            guia.save()
            print("hola")
        else:
            print(guia.errors)
        
    return render(request, 'imprimir.html')


def direccion(request):
    return render(request, 'direccion.html')


def covid(request):
    return render(request, 'covid.html')


def admision(request):
    return render(request, 'admision.html')


def colegio(request):
    return render(request, 'colegio.html')


def profesores(request):
    context = {"profesores": Profesor.objects.all()}
    return render(request, 'profesores.html', context)


def noticias(request):
    context = {"noticias": Noticia.objects.all()}

    return render(request, 'noticias.html', context)


def valores(request):
    return render(request, 'valores.html')


def pie(request):
    return render(request, 'pie.html')


def blog(request, idnotice):

    noticia = Noticia.objects.get(id=idnotice)
    noticia.date = dame_formato(noticia.date)

    fotos = ImagesNoticia.objects.all().filter(noticia_id=idnotice)
    foto = ImagesNoticia
    for f in fotos:
        if f.noticia.titulo == noticia.titulo:
            foto = f
            break

    return render(request, 'blog.html', {'noticia':noticia, 'foto':foto})    


def noticia(request):
    if request.method == 'POST':

        form_noticia = FormNoticia(request.POST, request.FILES)
        fotos = request.FILES.getlist('imagenes')

        if form_noticia.is_valid():
            noticia = form_noticia.save(commit=False)
            noticia.save()
            for f in fotos:
                foto = ImagesNoticia(noticia=noticia, image=f)
                foto.save()

        else:
            print(form_noticia.errors)

    return render(request, 'noticia.html')


def evento(request):
    if request.method == 'POST':
        form = FormEvento(request.POST)
        if form.is_valid():
            new_evento = form.save()
    return render(request, 'evento.html')


def eventos(request):
    context = {"eventos": Evento.objects.all()}
    return render(request, 'eventos.html', context)


def destroy(request, id):
    employee = Evento.objects.get(id=id)
    employee.delete()
    return redirect("/eventos")

def destroy_guia(request, id):
    guia = Guia.objects.get(id=id)
    guia.delete()
    
    return redirect("/pedidos")

def estado_guia(request, id):
    guia = Guia.objects.get(id=id)
    guia.estado = "Ok"
    guia.save()
    
    return redirect("/pedidos")

def download_guia(request, id):
    guia = Guia.objects.get(id=id)

    
    filepath = os.path.join(settings.MEDIA_ROOT, guia.documento.name)

    return FileResponse(open(filepath, 'rb'), content_type='application/force-download')

def destroy_noticia(request, id):
    news = Noticia.objects.get(id=id)
    news.delete()
    return redirect("/noticias")


def destroy_profesor(request, id):
    profe = Profesor.objects.get(id=id)
    profe.delete()
    return redirect("/profesores")


def add_alumno(request):
    if request.method == 'POST':
        form = FormAlumno(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('hello')
        else:
            print('error al ingresar alumno')    

    return render(request, 'form_alumno.html')


def cursos(request):
    return render(request, 'cursos.html')


def galeria(request):

    noticias = Noticia.objects.all()

    noticias_galeria = []

    for n in noticias:
        if n.galeria == True:
            noticias_galeria.append(n)

    fotos = ImagesNoticia.objects.all()
    
    return render(request, 'galeria.html', {'noticias':noticias_galeria, 'fotos':fotos})    


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        send_mail("mensaje de la web", mensaje, email, ['altascumbressanclemente@gmail.com'])

        return HttpResponse("Gracias por contactarnos")

    return render(request, 'contacto.html')
