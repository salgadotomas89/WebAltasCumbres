import mimetypes
import os
from django.utils.dateparse import parse_date 
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from urllib.request import Request
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, Curso, FormAlumno, FormLibro, FormNoticia, FormEvento, FormProfesor, FormGuia, FormComunicado
from datetime import datetime
from json import dumps
from django.contrib import messages #import messages
from django.http import JsonResponse
from .models import Book, Alumno, ArchivosComunicado, Guia, ImagesNoticia, Noticia, Evento, Profesor, Curso, Comunicado


#funciones relacionadas con los archivos estaticos como reglamento
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

def reglamentos(request):
    return render(request, 'reglamentos.html')

def proyecto(request):
    return render(request, 'proyecto.html')


#pagina de inicio del sitio
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


#cambia el formato de la fecha date
def dame_formato(date):
    formato = "%d %b %Y"
    return date.strftime(formato)

def boletin(request):
    return render(request, 'boletin.html')

def salaBiblioteca(request):
    return render(request, 'sala-biblioteca.html')

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


#Guias para imprimir
def pedidos(request):
    lista_guias = Guia.objects.all()  # traigo todas las guias

    for l in lista_guias:
        l.fecha_subida = dame_formato(l.fecha_subida)


    return render(request, 'pedidos.html', {'guias':lista_guias})

def imprimir(request):
    profesores = Profesor.objects.all()
    if request.method == 'POST':
        guia = FormGuia(request.POST, request.FILES)
        if guia.is_valid():
            guia.save()
            messages.success(request, 'Archivo enviado exitosamente.')
            return render(request, 'imprimir.html')
        else:
            messages.error(request, 'Hubo un error, intente nuevamente.')
            return render(request, 'imprimir.html')
        
    return render(request, 'imprimir.html', {"profesores":profesores})

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


def directiva(request):
    return render(request, 'directiva.html')


def mision(request):
    return render(request, 'mision.html')


def vision(request):
    return render(request, 'vision.html')

def libros(request):
    libros = Book.objects.all
    return render(request, 'libros.html', {'libros': libros})


def profesor(request):
    if request.method == 'POST':
        form = FormProfesor(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        else:
            print("error al ingresar profesor")

    return render(request, 'profesor.html')

def libro(request):
    if request.method == 'POST':
        form = FormLibro(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Archivo enviado exitosamente.')
        else:
            messages.error(request, 'Error al ingresar archivo.'+form.add_error)
    return render(request, 'form-libro.html')


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

def get_segundo_elemento(tupla):
    return tupla[0]

def panel(request):
    context = {'cursos' : Curso.objects.all()}
    return render(request, 'panel.html', context)
    
def alumnos(request, idCurso):
    #traigo todos los alumnos del curso seleccionado ordenado por el nombre a-z
    alumnos =  Alumno.objects.filter(curso_id = idCurso).order_by("nombre")
    cursos = Curso.objects.all    
    #metodo request GET es para cuando seleccionamos alumno del curso correspondiente
    if request.method == 'GET' :
        if 'post_id' in request.GET:
            #id del alumno pasado por ajax 
            post_id = request.GET['post_id']
            elegido = Alumno.objects.get(id = post_id)
            elegido.edad = calcularEdad(elegido)
            fecha  = elegido.fechaNacimiento.strftime("%m/%d/%Y")
            diccionario = {
                'nombre' : elegido.nombre,
                'apellido' : elegido.apellido,
                'nacionalidad' : elegido.nacionalidad,
                'edad': elegido.edad,
                'fechaNac': fecha,
                'direccion': elegido.direccion,
                'fono': elegido.fono
            }
            dataJSON = dumps(diccionario)

            #data = serializers.serialize('json', elegido)
            return HttpResponse(dataJSON)

            #return render(request, 'alumnos.html', {'data': dataJSON})
        else :    
            print('hello')
            return render(request, 'alumnos.html', {'alumnos':alumnos, 'cursos': cursos,'idCurso': idCurso})
    
def prueba(request):
    if request.is_ajax():
        alumnos =  Alumno.objects.filter(curso_id = 1).order_by("nombre")
        html = render_to_string('prueba.html', {'alumnos': alumnos})
    return HttpResponse(html)


#funciones relacionadas con el perfil de los usuarios
def perfil(request, id):
    alumno =  Alumno.objects.get(id = id)
    

    context = {
        'alumno' : alumno
    }

    return render(request, 'perfil.html', context)


def noticias(request):
    context = {"noticias": Noticia.objects.all()}
    return render(request, 'noticias.html', context)

def comunicados(request):
    archivos = ArchivosComunicado.objects.all()
    comunicados = Comunicado.objects.all()
    return render(request, 'comunicados.html', {'comunicados':comunicados, 'archivos':archivos})

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


def add_comunicado(request):
    if request.method == 'POST':
        form_noticia = FormComunicado(request.POST, request.FILES)
        archivos = request.FILES.getlist('files')
        print('hello')
        print(archivos)

        if form_noticia.is_valid():
            noticia = form_noticia.save(commit=False)
            noticia.save()

            for f in archivos:
                foto = ArchivosComunicado(comunicado=noticia, archivo=f)
                foto.save()

        else:
            messages.error(request, form_noticia.errors)
            return render(request, 'comunicado.html')

    return render(request, 'comunicado.html')


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

def destroy_comunicado(request, id):
    news = Comunicado.objects.get(id=id)
    news.delete()
    return redirect("/comunicados")


def destroy_profesor(request, id):
    profe = Profesor.objects.get(id=id)
    profe.delete()
    return redirect("/profesores")

def destroy_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect("/alumnos")




def add_alumno(request):
    cursos = Curso.objects.all

    return render(request, 'alumno.html',{'cursos': cursos} )




def calcularEdad(alumno):
        #fecha de hoy
        edad = 0
        currentDateTime = datetime.now()
        date = currentDateTime.date()
        #extraigo el año
        añoActual = date.strftime("%Y")
        #extraigo el mes
        mesActual = date.strftime("%M")
        diaActual = date.strftime("%D")
        #fecha nacimiento del alumno
        fechaNac = alumno.fechaNacimiento
        #extraigo su año de nacimiento
        añoNacimiento = fechaNac.strftime("%Y")
        mesNacimiento = fechaNac.strftime("%M")
        diaNacimiento = fechaNac.strftime("%D")


        if fechaNac.month >=  date.month:
            if fechaNac.day >= date.day:
                edad = int(añoActual) - int(añoNacimiento)
            else:
                edad = int(añoActual) - int(añoNacimiento) -1       
        else:
            edad = int(añoActual) - int(añoNacimiento) -1
            

        return edad

def savealumno(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = FormAlumno(request.POST)
        idCurso = request.POST.get('curso')
        curso = Curso.objects.get(id=idCurso)
        form.curso = curso
        if form.is_valid():
            # save the data and after fetch the object in instance
            alumno = form.save()
            response = {
                'msg':'Datos guardados exitosamente' # response message
            }
            return JsonResponse(response)
        else:
            print(form.errors)   
        
    return render(request, 'alumno.html')


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
