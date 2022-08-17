from django.contrib import admin

from colegio.models import Alumno, Apoderado, Book, Evento, Guia, ImagesNoticia, Madre, Noticia, Padre, Profesor
from colegio.views import madre

# Register your models here.

admin.site.register(Noticia)
admin.site.register(Evento)
admin.site.register(ImagesNoticia)
admin.site.register(Guia)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Apoderado)
admin.site.register(Book)
admin.site.register(Madre)
admin.site.register(Padre)

