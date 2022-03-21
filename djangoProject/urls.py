"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path

from colegio import views
from djangoProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/<int:idnotice>', views.blog, name='blog'),
    path('directiva', views.directiva, name="directiva"),
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
    path('delete/evento/<int:id>', views.destroy),
    path('delete/noticia/<int:id>', views.destroy_noticia),
    path('delete/profesor/<int:id>', views.destroy_profesor),

    path('galeria', views.galeria, name='galeria')


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

