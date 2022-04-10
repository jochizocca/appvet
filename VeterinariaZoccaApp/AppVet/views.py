from django.http import HttpResponse
from django.shortcuts import render
from .models import Clientes
from .models import Animales
from .models import turno
from .models import Productos


def clientes(request,nombre, apellido,dni):

    mis_clientes= Clientes(nombre=nombre,apellido= apellido,dni=dni)
    mis_clientes.save()
    
    return HttpResponse (f'Se genero el Cliente: {mis_clientes.nombre} {mis_clientes.apellido} dni = {mis_clientes.dni}')



def turno(request,dia,hora,email):

    mis_turnos= turno(dia=dia,hora=hora,email=email)
    mis_turnos.save()
    
    return HttpResponse (f'Su turno es : {mis_turnos.dia} {mis_turnos.hora} se envia email a: {mis_turnos.email}')

def producto(request,n_producto,sku):

    mis_productos= Productos(n_producto=n_producto,sku=sku)
    mis_productos.save()
    
    return HttpResponse (f'{n_producto} sku= {sku}')
    
def animales(request,nombre_animal, raza):

    mis_animales= Animales(nombre_animal=nombre_animal,raza=raza)
    mis_animales.save()
    
    return HttpResponse (f'Se agrego el Animal: {mis_animales.nombre_animal} raza: {mis_animales.raza} ')
