"""datascience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
#from datascience.views import Estandar, inicio
from datos import views 
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#rutas para ingresar al navegador
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('index/', inicio),
    path('index/', views.Estandar, name= 'Estandar'),
    path('prueba/', views.subir, name= 'subir'),
    path('ig/', views.mostrar, name= 'mostrar'),
    path('', views.home, name='home'),
    #path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    
]
urlpatterns += staticfiles_urlpatterns()

#<int:edad>/<int:agno>