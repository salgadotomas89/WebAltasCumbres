from re import template
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from colegio import views
from djangoProject import settings
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('torneos', views.torneos),
    path('ranking', views.ranking, name='ranking'),
    path('info/alumno/<int:id>', views.info),
    path('info/<int:id>', views.infoAlumnos),
    path('madre/<int:id>/', views.madre),
    path('padre/<int:id>/', views.padre),
    path('amigo', views.amigoSecreto, name='amigo'),
    path('amigo/resultado', views.amigoResultado, name='resultadoAmigo'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path('inscripciones', views.inscripciones, name='inscripciones'),
    path('tutor/<int:id>/', views.tutor, name='tutor'),
    path('select/madre/<int:idMadre>/<int:idAlumno>', views.selectMadre),
    path('select/padre/<int:idPadre>/<int:idAlumno>', views.selectPadre),
    path('select/tutor/<int:idTutor>/<int:idAlumno>', views.selectTutor),
    path('cursos', views.cursos, name='cursos'),
    path('inicio', views.inicio, name='inicio'),
    path('registro', views.registro, name='register'),
    path('blog/<int:idnotice>', views.blog, name='blog'),
    path('directiva', views.directiva, name="directiva"),
    path('boletin', views.boletin, name="boletin"),
    path('evaluaciones', views.evaluaciones, name="evaluaciones"),
    path('add/calendario', views.addEvaluacion, name="calendarioevaluaciones"),
    path('mision', views.mision, name="mision"),
    path('vision', views.vision, name="vision"),
    path('contacto', views.contacto, name="contacto"),
    path('noticia', views.noticia, name="noticia"),
    path('evento', views.evento, name="evento"),
    path('noticias', views.noticias, name="noticias"),
    path('admision', views.admision, name="admision"),
    path('colegio', views.colegio, name="colegio"),
    path('profesores', views.profesores, name="profesores"),
    path('profesor', views.profesor, name='profesor'),
    path('direccion', views.direccion, name='direccion'),
    path('valores', views.valores, name='valores'),
    path('pie', views.pie, name='pie'),
    path('covid', views.covid, name='covid'),
    path('reglamentos', views.reglamentos, name='reglamentos'),
    path('proyecto', views.show_pdf, name='proyecto'),
    path('documentos', views.proyecto, name='documentos'),
    path('convivencia', views.show_rc, name='convivencia'),
    path('reglamentointerno', views.show_rice, name='reglamentointerno'),
    path('archReligion', views.archReligion, name='archReligion'),


    path('fichaMatricula', views.fichaMatricula, name='fichaMatricula'),
    path('evaluacion', views.show_eva, name='evaluacion'),
    path('eventos', views.eventos, name='eventos'),
    path('encuesta', views.encuesta, name='encuesta'),
    path('add/libro', views.libro),
    path('alumno', views.savealumno, name='alumno'),
    path('apoderado', views.apoderado, name='apoderado'),
    path('delete/evento/<int:id>', views.destroy),
    path('delete/alumno/<int:id>', views.destroy_alumno),
    path('delete/noticia/<int:id>', views.destroy_noticia),
    path('delete/comunicado/<int:id>', views.destroy_comunicado),
    path('delete/guia/<int:id>', views.destroy_guia),
    path('download/guia/<int:id>', views.download_guia),
    path('download/calendario/<int:id>', views.descargarCalendario),
    path('add/boletin', views.addBoletin, "add-boletin"),

    path('estado/guia/<int:id>', views.estado_guia),
    path('delete/profesor/<int:id>', views.destroy_profesor),
    path('delete/alumno/<int:id>', views.destroy_alumno),
    path('cursos', views.cursos),
    path('add/comunicado', views.add_comunicado, name="comunicado"),
    path('galeria', views.galeria, name='galeria'),
    path('guias', views.imprimir, name="guias"),
    path('pedidos', views.pedidos),
    path('libros', views.libros, name='libros'),
    path('alumnos/<int:idCurso>/', views.alumnos, name='alumnos'),
    path('alumnos/perfil/<int:id>', views.perfil, name='perfil'),
    path('prueba', views.prueba),
    path('comunicados', views.comunicados, name="comunicados"),
    path('sala-biblioteca', views.salaBiblioteca,name="sala-biblioteca" ),
    path('panel', views.panel),
    path('talleres', views.talleres, name="talleres"),
    path('resultado/taller/<int:id>', views.resultadoTalleres),
    path('add/tenista', views.addTenista)
] 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

