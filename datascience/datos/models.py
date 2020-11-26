from django.db import models

# Create your models here.
class datociencia(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    dato=models.TextField(blank=True)
    date=models.DateField(auto_now_add=True)
    
  