from rest_framework import viewsets
from .models import (
    CategoriaProducto, Inventario, Producto, 
    InventarioProductos, TipoMovimiento, Movimiento, 
    Ajuste, Transferencia
)
from .serializers import (
    CategoriaProductoSerializer, 
    InventarioSerializer, 
    ProductoSerializer, ProductoReadSerializer,
    InventarioProductosSerializer, InventarioProductosReadSerializer,
    TipoMovimientoSerializer, 
    MovimientoSerializer, MovimientoReadSerializer,
    AjusteSerializer, AjusteReadSerializer,
    TransferenciaSerializer, TransferenciaReadSerializer
)

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductoReadSerializer
        return ProductoSerializer

class InventarioProductosViewSet(viewsets.ModelViewSet):
    queryset = InventarioProductos.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return InventarioProductosReadSerializer
        return InventarioProductosSerializer

class TipoMovimientoViewSet(viewsets.ModelViewSet):
    queryset = TipoMovimiento.objects.all()
    serializer_class = TipoMovimientoSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return MovimientoReadSerializer
        return MovimientoSerializer

class AjusteViewSet(viewsets.ModelViewSet):
    queryset = Ajuste.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return AjusteReadSerializer
        return AjusteSerializer

class TransferenciaViewSet(viewsets.ModelViewSet):
    queryset = Transferencia.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TransferenciaReadSerializer
        return TransferenciaSerializer