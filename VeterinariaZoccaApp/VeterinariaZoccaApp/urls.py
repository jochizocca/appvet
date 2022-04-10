"""VeterinariaZoccaApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from AppVet.views import clientes
from AppVet.views import turno
from AppVet.views import producto
from AppVet.views import animales

from .views import bienvenida
from .views import inicio



urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('inicio/', inicio),
    path('agrega.cliente/<nombre>/<apellido>/<dni>/', clientes),
    path('agrega.turno/<dia>/<hora>/<email>/', turno),
    path('agrega.producto/<n_producto>/<sku>/', producto),
    path('agrega.animal/<nombre_animal>,<raza>/',animales)

    ]
