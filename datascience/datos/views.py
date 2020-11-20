from django.shortcuts import render, redirect

# Create your views here.

from datos.models import City
 
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