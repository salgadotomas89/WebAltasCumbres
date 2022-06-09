from django.conf.urls import url, include # Add include to the imports here
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('colegio.urls')) # tell django to read urls.py in example app
] 
