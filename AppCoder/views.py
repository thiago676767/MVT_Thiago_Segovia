from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from AppCoder.models import Familia


def template(self):
    
    # familiares = Familia.objects.all()
    # contexto = {"familiares": familiares}


    diccionario = {
        "nombre":"Carlos","parentesco":"Padre", "fecha":"1971-11-23", "edad":"50",
        "nombre1":"Liliana","parentesco1":"Madre", "fecha1":"1969-12-25", "edad1":"52",
        "nombre2":"Maria","parentesco2":"Abuela", "fecha2":"1943-03-18", "edad2":"79",
        }

    miHtml = open("C:/Users/User/Desktop/coder/django/ProyectoMVT/AppCoder/plantillas/template.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)


# def index(request):
#     familiares = Familia.objects.all()
#     contexto = {"familiares": familiares} 
#     return render(request, "template.html", contexto)

# def familia(self):

#     familiar1 = Familia(nombre = "Carlos", parentesco = "Padre", fecha = "1971-11-23", edad = "50")
#     familiar1.save()

#      familiar2 = Familia(nombre = "Liliana", parentesco = "Madre", fecha = "1969-12-25", edad = "52")
#      familiar2.save()

#      familiar3 = Familia(nombre = "Maria", parentesco = "Abuela", fecha = "1943-03-18", edad = "79")
#      familiar3.save()

#     documento = f"El {familiar1.parentesco} se llama {familiar1.nombre}, nacio el {familiar1.fecha} y su edad es {familiar1.edad}"

#     return HttpResponse(documento)