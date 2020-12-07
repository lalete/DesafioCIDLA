from .models import Sciencia
from rest_framework import serializers

class ScienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sciencia
        fields = '__all__'