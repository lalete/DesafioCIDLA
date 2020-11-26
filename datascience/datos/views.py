from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from datos.models import datociencia
import json
from django.conf import settings
import os



#Funcion que redirecciona al html inicio 
def home(request):
    return render(request, 'home.html')
 
# Luego de entrar a la pagina de inicio y seleccionar estandar nos llevara al html index.
def Estandar (resquest): 
    fechaup= datetime.datetime.now()
    return render (resquest, 'index.html', {'damefecha':fechaup})

def mostrar(request):
    docs=[]
    for e in datociencia.objects.all():
        docs.append(e)
        
   return render(request, 'ig.html',{'damefecha':docs})


def subir(request):

    b=datociencia(name='prueba',dato=my_file,date='')
    b.save()
    print(b)
    return render(request, 'prueba.html')

base_dir =settings.MEDIA_ROOT    
my_file = os.path.join(base_dir, str(object='clinicos.json'))

