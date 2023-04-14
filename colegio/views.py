from email import message
from itertools import chain
import json
import mimetypes
from operator import attrgetter
import os
import random
from django.core import serializers
from django.views.generic import TemplateView, ListView
from django.db.models import Q # new

import re
from django.utils.dateparse import parse_date 
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from urllib.request import Request
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, FormBoletin, FormTenista,Curso,FormEvaluacion,FormInscripcion, FormAlumno, FormAmigo, FormApoderado, FormLibro, FormMadre, FormNoticia, FormEvento, FormPadre, FormProfesor, FormGuia, FormComunicado, FormTutor, UserRegisterForm
from datetime import datetime
from json import dumps
from django.contrib import messages #import messages
from django.http import JsonResponse
from .models import Amigo,Tenista, Apoderado, Evaluacion, Book, Alumno, ArchivosComunicado, Guia, ImagesNoticia, Madre, Noticia, Evento, Padre, Profesor, Curso, Comunicado, Tutor, Taller, Inscripcion


#funciones relacionadas con los archivos estaticos como reglamento
def archReligion(request):
    filepath = os.path.join('static', 'CircularReligion.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def fichaMatricula(request):
    filepath = os.path.join('static', 'fichaMatricula.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


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

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def galeria(request):

    noticias = Noticia.objects.all()
    noticias_ordenadas = noticias.order_by('-date')
    noticias_galeria = []

    for n in noticias_ordenadas:
        n.date = dame_formato(n.date)  # actualizo su formato de fecha
        if n.galeria == True:
            noticias_galeria.append(n)

    fotos = ImagesNoticia.objects.all()
    
    return render(request, 'fotos.html', {'noticias':noticias_galeria, 'fotos':fotos})    



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

def destroyAlumnoTaller(request, id):

    return redirect("/talleres")

def estado_guia(request, id):
    guia = Guia.objects.get(id=id)
    guia.estado = "Ok"
    guia.save()
    
    return redirect("/pedidos")

def download_guia(request, id):
    guia = Guia.objects.get(id=id)
    filepath = os.path.join(settings.MEDIA_ROOT, guia.documento.name)
    return FileResponse(open(filepath, 'rb'), content_type='application/force-download')

def descargarListaMateriales(request, curso):
    msg = 'materials'
    msg += str(curso)
    msg += '.pdf'
    filepath = os.path.join('static', msg)


    if os.path.isfile(filepath):
        print("existe")
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    else:
        print('no existe')
        return redirect("index")

def descargarCalendario(request, id):

    guia = Evaluacion.objects.get(id=id)
    filepath = os.path.join(settings.MEDIA_ROOT, guia.archivo.name)
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


def talleres(request):
    talleres = Taller.objects.all()#traigo todos los talleres
    inscripcion = True

    if request.method == 'POST':
        form = FormInscripcion(request.POST)
        if form.is_valid():
            form.save()
            inscripcion = False
        else:
            print('formulario no valido')
    else:
        print('hola')

    context = {"talleres": talleres, "inscripcion": inscripcion}

    return render(request, 'talleres.html', context )

def comunicados(request):
    archivos = ArchivosComunicado.objects.all()
    comunicados = Comunicado.objects.order_by('id').all().reverse()

    
    return render(request, 'comunicados.html', {'comunicados':comunicados, 'archivos':archivos})

def valores(request):
    return render(request, 'valores.html')

def pie(request):
    return render(request, 'pie.html')


def evaluaciones(request):
    evaluaciones = Evaluacion.objects.all()

    context = {"evaluaciones": evaluaciones}
    
    return render(request, "evaluaciones.html", context)

def addEvaluacion(request):
    if request.method == 'POST':
        form = FormEvaluacion(request.POST, request.FILES)
        archivos = request.FILES.getlist('file')

        if form.is_valid():
            form.save()

    return render(request, 'form-evaluacion.html')



def inscripciones(request):

    return render(request, 'inscripciones.html')


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


def addBoletin(request):
    if request.method == 'POST':

        form = FormBoletin(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    return render(request, 'boletin.html')


def add_comunicado(request):
    if request.method == 'POST':
        form_noticia = FormComunicado(request.POST, request.FILES)
        archivos = request.FILES.getlist('files')
        

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

@login_required
def inicio(request):
    current_user = request.user
    respuesta = 'no'
    alumnos = None
    
    if Apoderado.objects.filter(user_id=current_user).exists():
        apoderado = Apoderado.objects.get(user_id=current_user)
        # resto de acciones cuando el pedido existe
        respuesta = 'si'

        print(apoderado.id)

        if Alumno.objects.filter(apoderado_id=apoderado).exists():
            print(Alumno.objects.filter(apoderado_id=3).__sizeof__)
            alumnos = Alumno.objects.filter(apoderado_id=apoderado)
            print(alumnos.count)
            if len(alumnos) > 1 :
                alumnos = Alumno.objects.filter(apoderado_id=apoderado)

                # resto de acciones cuando el pedido existe
            else:
                print('ke')
                print(Alumno.objects.filter(apoderado_id=3).exists())
                alumnos = Alumno.objects.get(apoderado_id=apoderado)
        else:
            #no hay alumnos
            print('hola')
            pass
        
    else:
        # acciones cuando el pedido no existe, redireccionas, envias un mensaje o cualquier opcion que consideres necesario para tratar este caso
        pass
    
    
    return render(request, 'inicio.html', {'username': current_user, 'apoderado': respuesta, 'alumnos': alumnos})

@csrf_exempt 
def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        nombreUsuario = request.POST.get('username')
        passw = request.POST.get('password')


        if form.is_valid():
            user = form.save()

            user = authenticate(username=nombreUsuario, password=passw)

            #message.success(request,'se ha creado exitosamente')
            return redirect('inicio')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registro.html', context)


def apoderado(request):
    current_user = request.user

    if request.method == "POST":
        form = FormApoderado(request.POST)

        if form.is_valid():

            your_object = form.save(commit=False)
            your_object.user = current_user
            your_object.save()

            return redirect("inicio")

        else:
            print(form.errors)


    return render(request, 'apoderado.html')

def savealumno(request):
    #usuario logeado
    current_user = request.user
    apoderado = Apoderado.objects.get(user_id=current_user.id)


    # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        form = FormAlumno(request.POST)
        idCurso = request.POST.get("curso")
        curso = Curso.objects.get(id=idCurso)
        
        if form.is_valid():
            your_object = form.save(commit=False)
            your_object.curso = curso
            your_object.apoderado = apoderado
            alumno = your_object.save()

            # save the data and after fetch the object in instance
            

            return redirect('inicio')

        else:
            print('error ingresando datos')
            print(form.errors) 

    cursos = Curso.objects.all
    return render(request, 'alumno.html',{'cursos': cursos})


def encuesta(request):
    return render(request, 'encuesta.html')


def selectTutor(request, idTutor, idAlumno):
    alumno = Alumno.objects.get(id = idAlumno)
    print(alumno.nombre)
    tutor = Tutor.objects.get(id=idTutor)
    alumno.tutor = tutor
    alumno.save()

    return redirect('inicio')




def resultadoTalleres(request, id):
    alumnos = Inscripcion.objects.filter(talleres = id)
    taller = Taller.objects.get(id = id)
    
    total  = len(alumnos)


    print(taller)
    print(alumnos)

    context = {'alumnos': alumnos, 'taller': taller, 'total':total}

    return render(request, 'resultados-taller.html', context)


def tutor(request, id):
    current_user = request.user
    alumno = Alumno.objects.get(id = id)

    if request.method == 'POST':
        
        form = FormTutor(request.POST)
        if form.is_valid():
            idAlumno = request.POST.get("idAlumno")

            alumno = Alumno.objects.get(id = idAlumno)


            tutor = form.save()
            alumno.tutor = tutor
            alumno.save()
            return redirect('inicio')
    
    return render(request, 'tutor.html', {'idAlumno': id})

#aqui llegamos despues de registrar al alumno, con su id

def selectPadre(request, idPadre, idAlumno):
    alumno = Alumno.objects.get(id = idAlumno)
    print(alumno.nombre)
    padre = Padre.objects.get(id=idPadre)
    alumno.padre = padre
    alumno.save()

    return redirect('inicio')

def padre(request, id):
    current_user = request.user
    alumno = Alumno.objects.get(id = id)

    if request.method == 'POST':
        
        form = FormPadre(request.POST)
        if form.is_valid():
            idAlumno = request.POST.get("idAlumno")
            alumno = Alumno.objects.get(id = idAlumno)
            padre = form.save()
            alumno.padre = padre
            alumno.save()
            return redirect('inicio')
    
    return render(request, 'padre.html', {'idAlumno': id})

def selectMadre(request, idMadre, idAlumno):
    alumno = Alumno.objects.get(id = idAlumno)
    print(alumno.nombre)
    madre = Madre.objects.get(id=idMadre)
    alumno.madre = madre
    alumno.save()
    print('hooa')

    return redirect('inicio')

def madre(request, id):
    current_user = request.user
    alumno = Alumno.objects.get(id = id)

    if request.method == 'POST':
        
        form = FormMadre(request.POST)
        if form.is_valid():
            idAlumno = request.POST.get("idAlumno")
            alumno = Alumno.objects.get(id = idAlumno)
            madre = form.save()
            alumno.madre = madre
            alumno.save()
            return redirect('inicio')
        else:
            print(form.errors)
    
    return render(request, 'madre.html', {'idAlumno': id})




def cursos(request):
    return render(request, 'cursos.html')

def ranking(request):
    hola = Tenista.objects.all()


    #ordenar a los jugadores segun puntaje
    jugadores = sorted(hola, key=attrgetter('puntaje'), reverse=True)
    i=1
    for jugador in jugadores:
        jugador.ranking = i
        jugador.save()
        i=i+1

    context = {'jugadores':jugadores}


    return render(request, 'ranking.html', context)


def addTenista(request):
    if request.method == 'POST':

        form = FormTenista(request.POST)

        if form.is_valid():
            form.save()
            
        

    return render(request, 'form-tenista.html')


def torneos(request):

    return render(request, 'torneos.html')



def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        send_mail("mensaje de la web", mensaje, email, ['altascumbressanclemente@gmail.com'])

        return HttpResponse("Gracias por contactarnos")

    return render(request, 'contacto.html')



def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})


def infoAlumnos(request, id):
    print('id curso')
    print(id)
    alumnos = Alumno.objects.filter(curso_id = id)

    return render(request, 'info-alumnos.html', {'alumnos': alumnos})

def info(request, id):
    alumno = Alumno.objects.get(id = id)

    return render(request, 'alumno-info.html', {'alumno': alumno})





def amigoSecreto(request):
    
    if request.method == 'POST':
        form = FormAmigo(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "registrado exitosamente"
        else:
            mensaje = 'hubo un error, porfavor intertarlo nuevamente!!'
        
        return render(request, 'amigo.html',{
            "mensaje": mensaje
        })
            
    else:
        return render(request, 'amigo.html')

class SearchResultsView(ListView):
    model = Amigo
    template_name = "resultados-amigo.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        ipActual = verIp(self.request, query)
        object_list = Amigo.objects.filter(
            Q(nombre__icontains=query) 
        )

        if object_list.get().ip:

            if Amigo.objects.filter(ip=ipActual):
            
                if object_list.get().ip == Amigo.objects.filter(ip=ipActual).get().ip:
                    print('puede ver los datos 1')
                    
                else:
                    print('no puede ver los datos 1')
                    object_list = None
            else:
                print(' no puedes ver esos datos')
                

        else:#no tiene ip

            #veo si mi ip no ha consultado antes en la base de datos
            if Amigo.objects.filter(ip=ipActual):

                if object_list.get().nombre == Amigo.objects.filter(ip=ipActual).get().nombre:
                    print('puede ver los datos 2')
                    Amigo.objects.filter(nombre=query).update(visto=True)
                    Amigo.objects.filter(nombre=query).update(ip=ipActual)

                else:
                    print('no puede ver los datos 2')
                    object_list = None
                    
            else:

                print ('registrando')
                Amigo.objects.filter(nombre=query).update(visto=True)
                Amigo.objects.filter(nombre=query).update(ip=ipActual)


        return object_list


def verIp(request, nombre):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    
    
    return ip
    

    


def amigoResultado(request):

    return render(request, 'resultados-amigo.html')

def realizarSorteo():
    amigos = Amigo.objects.all()#traigo a todos los participantes
    friends = []

    for amigo in amigos:
        if amigo.nombreAmigo is None:
            friends.append(amigo)

    cantidad = int(len(amigos))#cantidad de participantes

    if cantidad % 2 == 0:
        for i in range(cantidad):
            primerSeleccionado = amigos[i]
            #si seleccionado no tiene amigo secreto



            if(primerSeleccionado.nombreAmigo is None):

                segundoSeleccionado = random.choice(friends)

                
                while primerSeleccionado == segundoSeleccionado:
                    segundoSeleccionado = random.choice(friends)

                
                friends.remove(segundoSeleccionado)

                amigos.filter(nombre=primerSeleccionado.nombre).update(nombreAmigo=segundoSeleccionado.nombre+' '+segundoSeleccionado.apellido)

    else:
        print('falta un participante para el juego de amigo secreto')



   