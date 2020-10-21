from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

#def interestandar (request): #edad,agno #V ista interfaz usuario estandar v1
    #fechaup= datetime.datetime.now()
    #edad= 23
    #periodo=agno-2020
    #edadfu=edad+periodo

    #doc_ext= open("C:/ProyectoTI3/datascience/datascience/plantillas/estandar.html")
    #plt=Template(doc_ext.read())
    #doc_ext.close()

    #CARGA PLANTILLA v1
    #doc_ext=get_template('estandar.html')
    #ctx=Context()
    #plantilla=doc_ext.render()
    
    #CARGA PLANTILLA V2
    #return render(request,'estandar.html' ) # resquest,plantilla,diccionario

def inicio (request): 
    fechaup= datetime.datetime.now()
    return render(request, 'inicio.html' , {'damefecha':fechaup} ) 
def Estandar (resquest): 
    fechaup= datetime.datetime.now()
    return render (resquest, 'userEstandar.html', {'damefecha':fechaup})
