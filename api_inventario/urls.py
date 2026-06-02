from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

# 1. Creamos el router
router = DefaultRouter()

# 2. Registramos TODOS tus endpoints en singular
router.register(r'categoria_producto', views.CategoriaProductoViewSet, basename='categoria_producto')
router.register(r'inventario', views.InventarioViewSet, basename='inventario')
router.register(r'producto', views.ProductoViewSet, basename='producto')
router.register(r'inventario_producto', views.InventarioProductosViewSet, basename='inventario_producto')
router.register(r'tipo_movimiento', views.TipoMovimientoViewSet, basename='tipo_movimiento')
router.register(r'movimiento', views.MovimientoViewSet, basename='movimiento')
router.register(r'ajuste', views.AjusteViewSet, basename='ajuste')
router.register(r'transferencia', views.TransferenciaViewSet, basename='transferencia')

# 3. Cargamos las URLs al proyecto
urlpatterns = [
    path('', include(router.urls)),
]