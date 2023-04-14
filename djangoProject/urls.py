from django.urls import path, include 
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from colegio import views

urlpatterns = [
    path('admin/', admin.site.urls),
        path('', views.index, name='index'),

    path('', include('colegio.urls')),

] 
handler404 = views.page_not_found_view
