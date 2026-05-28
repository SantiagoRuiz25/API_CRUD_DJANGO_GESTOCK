from django.urls import path
from . import views  # Importamos las vistas desde api_inventario/views.py

urlpatterns = [
    # ---- CATEGORÍAS DE PRODUCTOS ----
    path('categorias/', views.CategoriaProductoListCreateView.as_view(), name='categorias-list'),
    path('categorias/<int:pk>/', views.CategoriaProductoDetailView.as_view(), name='categoria-detail'),

    # ---- PRODUCTOS ----
    path('productos/', views.ProductoListCreateView.as_view(), name='productos-list'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),
    
    # ---- INVENTARIOS (BODEGAS) ----
    path('inventarios/', views.InventarioListCreateView.as_view(), name='inventarios-list'),
    path('inventarios/<int:pk>/', views.InventarioDetailView.as_view(), name='inventario-detail'),
    
    # ---- INVENTARIO PRODUCTOS (STOCK EN BODEGAS) ----
    path('inventario-productos/', views.InventarioProductosListCreateView.as_view(), name='inventario-productos-list'),
    path('inventario-productos/<int:pk>/', views.InventarioProductosDetailView.as_view(), name='inventario-producto-detail'),

    # ---- TIPOS DE MOVIMIENTO ----
    path('tipos-movimiento/', views.TipoMovimientoListCreateView.as_view(), name='tipos-movimiento-list'),
    path('tipos-movimiento/<int:pk>/', views.TipoMovimientoDetailView.as_view(), name='tipo-movimiento-detail'),

    # ---- MOVIMIENTOS ----
    path('movimientos/', views.MovimientoListCreateView.as_view(), name='movimientos-list'),
    path('movimientos/<int:pk>/', views.MovimientoDetailView.as_view(), name='movimiento-detail'),
    
    # ---- AJUSTES DE STOCK ----
    path('ajustes/', views.AjusteListCreateView.as_view(), name='ajustes-list'),
    path('ajustes/<int:pk>/', views.AjusteDetailView.as_view(), name='ajuste-detail'),

    # ---- TRANSFERENCIAS ----
    path('transferencias/', views.TransferenciaListCreateView.as_view(), name='transferencias-list'),
    path('transferencias/<int:pk>/', views.TransferenciaDetailView.as_view(), name='transferencia-detail'),
]