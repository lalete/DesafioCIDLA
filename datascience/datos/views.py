from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from .forms import UploadDocumentForm

from mongoengine import connect
from datos.models import City


from django.conf import settings
from django.core.files.storage import FileSystemStorage


#Funcion que redirecciona al html inicio 
def home(request):
    return render(request, 'home.html')
 
def pie_chart(request):
    labels = []
    data = []
 
    queryset = City.objects.order_by('-population')[:9]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)
 
    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })

# Luego de entrar a la pagina de inicio y seleccionar estandar nos llevara 
# al html index.
def Estandar (resquest): 
    fechaup= datetime.datetime.now()
    return render (resquest, 'index.html', {'damefecha':fechaup})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'ig.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'ig.html')