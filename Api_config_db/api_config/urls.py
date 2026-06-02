from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    sistemaViewSet,
    backupViewSet,
    seguridadViewSet,
    notificacionViewSet,
)

router = DefaultRouter()

router.register(r'sistema', sistemaViewSet)
router.register(r'backup', backupViewSet)
router.register(r'seguridad', seguridadViewSet)
router.register(r'notificacion', notificacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]