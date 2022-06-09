from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from colegio import views
from djangoProject import settings



urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:idnotice>', views.blog, name='blog'),
    path('directiva', views.directiva, name="directiva"),
    path('boletin', views.boletin, name="boletin"),
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
    path('evaluacion', views.show_eva, name='evaluacion'),
    path('eventos', views.eventos, name='eventos'),
    path('add/alumno', views.add_alumno),
    path('add/libro', views.libro),
    path('savealumno', views.savealumno, name='savealumno'),
    path('delete/evento/<int:id>', views.destroy),
    path('delete/alumno/<int:id>', views.destroy_alumno),
    path('delete/noticia/<int:id>', views.destroy_noticia),
    path('delete/comunicado/<int:id>', views.destroy_comunicado),
    path('delete/guia/<int:id>', views.destroy_guia),
    path('download/guia/<int:id>', views.download_guia),
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
    path('panel', views.panel)
] 

handler404 = views.page_not_found_view


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

