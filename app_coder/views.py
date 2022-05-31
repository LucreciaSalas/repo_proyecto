from django.shortcuts import render
from django.http import HttpResponse
import datetime
from app_coder.models import Pacientes, Prestadores, Proveedores
from django.template import loader  # agregado en clase 18 #

# Create your views here.

#def inicio(request): #
  #  return render(request, "index.html") #

"""
def lista_pacientes(request):
    pacientes= Pacientes.objects.all()
    datos= {"datos" : pacientes }

    return render (request, "lista_pacientes.html", datos) #sin configurar html#
"""

def lista_pacientes(request):                   #función configurada en clase 18 HORA 1:48#
    pacientes= Pacientes.objects.all()
    datos= {"datos" : pacientes }
    plantilla = loader.get.template("plantillas.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)


def lista_prestadores(request):
    prestadores= Prestadores.objects.all()
    datos= {"datos" : prestadores }

    return render (request, "lista_prestadores.html", datos) 

def lista_proveedores(request):
    proveedores= Proveedores.objects.all()
    datos= {"datos" : proveedores }

    return render (request, "lista_proveedores.html", datos) 

   #  FALTA CONFIGURAR INGRESO POR FORMULARIO #
def alta_pacientes (request):
    paciente= Pacientes(nombre="María Laura Perez", edad=30, dni=38555678,  patología="diabetes", talla=170, peso=70, contorno=80)
    paciente.save()
    paciente= Pacientes(nombre="Pedro Gutierrez", edad=67, dni=8577087,  patología="diabetes", talla=180, peso=110, contorno=140)
    paciente.save()
    
    return HttpResponse("Se ha cargado lista de pacientes")


"""
def alta_pacientes(request, nombre, edad, dni, patologia, talla, peso, contorno)
    paciente= Pacientes(nombre=nombre, edad=edad, dni=dni, patología=patología, talla=talla, peso=peso, contorno=contorno)
    paciente.save()
    texto= f"Se cargó correctamente paciente en BD Pacientes"
    return HttpResponse(texto)

"""