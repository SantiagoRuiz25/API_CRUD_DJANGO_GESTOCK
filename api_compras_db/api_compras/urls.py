from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import (
    proveedorViewSet,
    proveedor_productosViewSet,
    guias_entradaViewSet,
)

router = DefaultRouter()
router.register(r'proveedor', proveedorViewSet)
router.register(r'proveedor_productos', proveedor_productosViewSet)
router.register(r'guias_entrada', guias_entradaViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]