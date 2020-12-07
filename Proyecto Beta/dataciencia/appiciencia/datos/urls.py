from rest_framework import routers

from .viewsets import ScienciaViewSet

router = routers.SimpleRouter()
router.register('datos',ScienciaViewSet)

urlpatterns = router.urls