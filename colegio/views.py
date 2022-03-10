import mimetypes
import os

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, FormNoticia, FormEvento, FormProfesor
from datetime import datetime

# Create your views here.
from .models import Noticia, Evento, Profesor


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

    if len(lista_profesores) >= 5:
        ultimos_profesores = [lista_profesores[len(lista_profesores) -1], lista_profesores[len(lista_profesores) -2],
                              lista_profesores[len(lista_profesores) -3], lista_profesores[len(lista_profesores) -4]]
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


def blog(request, idnotice):
    noticia = Noticia.objects.get(id=idnotice)

    noticia.date = dame_formato(noticia.date)

    context = {"noticia": noticia}

    return render(request, 'blog.html', context)


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


def noticia(request):
    if request.method == 'POST':

        form = FormNoticia(request.POST, request.FILES)
        files = request.FILES.getlist('documento')

        if form.is_valid():
            form.save()

        else:
            print("error")

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


def destroy_noticia(request, id):
    news = Noticia.objects.get(id=id)
    news.delete()
    return redirect("/noticias")


def galeria(request):
    return render(request, 'galeria.html')


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        send_mail("mensaje de la web", mensaje, email, ['altascumbressanclemente@gmail.com'])

        return HttpResponse("Gracias por contactarnos")

    return render(request, 'contacto.html')
