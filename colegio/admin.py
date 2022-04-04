from django.contrib import admin

from colegio.models import Evento, Guia, ImagesNoticia, Noticia, Profesor

# Register your models here.

admin.site.register(Noticia)
admin.site.register(Evento)
admin.site.register(ImagesNoticia)
admin.site.register(Guia)
admin.site.register(Profesor)
