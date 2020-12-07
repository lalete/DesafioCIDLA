from django.shortcuts import render,redirect
from rest_framework.response import Response
from django.template import Template, Context
from rest_framework.decorators import api_view

from django.db import models
from datos.models import Sciencia
import json



# Create your views here.
"""def subir(request):

    with open('C:/dataciencia/appiciencia/datos/media/clinicos.json') as json_data:
        d = json.load(json_data)

    b=Sciencia(name='prueba',dato=d)
    b.save()
    print(b)
    return render(request, 'prueba.html')
"""
api_view(['GET','POST','DELETE'])
def consultas(request,dato):
    queryset=Sciencia.objects.filter(id=dato)
    return 

