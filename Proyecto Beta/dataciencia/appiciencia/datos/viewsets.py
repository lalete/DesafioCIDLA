from rest_framework import viewsets
from .models import Sciencia
from .serializer import ScienciaSerializer

class ScienciaViewSet (viewsets.ModelViewSet):
    queryset=Sciencia.objects.all()
    serializer_class= ScienciaSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(
                Prefetch('cities')
            )
        return queryset
    