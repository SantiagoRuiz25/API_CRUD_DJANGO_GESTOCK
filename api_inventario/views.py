from rest_framework import generics
from .models import (
    CategoriaProducto, Producto, Inventario, 
    InventarioProductos, TipoMovimiento, Movimiento, 
    Ajuste, Transferencia
)
from .serializers import (
    CategoriaProductoSerializer,
    ProductoSerializer, ProductoReadSerializer,
    InventarioSerializer,
    InventarioProductosSerializer, InventarioProductosReadSerializer,
    TipoMovimientoSerializer,
    MovimientoSerializer, MovimientoReadSerializer,
    AjusteSerializer, AjusteReadSerializer,
    TransferenciaSerializer, TransferenciaReadSerializer
)

# ==========================================
# Vistas para CATEGORIAS DE PRODUCTOS
# ==========================================
class CategoriaProductoListCreateView(generics.ListCreateAPIView):
    queryset = CategoriaProducto.objects.filter(activo=True)
    serializer_class = CategoriaProductoSerializer

class CategoriaProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

    def perform_destroy(self, instance):
        # Borrado lógico por seguridad en inventarios
        instance.activo = False
        instance.save()


# ==========================================
# Vistas para PRODUCTOS
# ==========================================
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.filter(activo=True)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductoReadSerializer
        return ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductoReadSerializer
        return ProductoSerializer

    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()


# ==========================================
# Vistas para INVENTARIOS (BODEGAS)
# ==========================================
class InventarioListCreateView(generics.ListCreateAPIView):
    queryset = Inventario.objects.filter(activo=True)
    serializer_class = InventarioSerializer

class InventarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()


# ==========================================
# Vistas para INVENTARIO PRODUCTOS (STOCK)
# ==========================================
class InventarioProductosListCreateView(generics.ListCreateAPIView):
    queryset = InventarioProductos.objects.filter(activo=True)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InventarioProductosReadSerializer
        return InventarioProductosSerializer

class InventarioProductosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventarioProductos.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InventarioProductosReadSerializer
        return InventarioProductosSerializer

    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()


# ==========================================
# Vistas para TIPOS DE MOVIMIENTO
# ==========================================
class TipoMovimientoListCreateView(generics.ListCreateAPIView):
    queryset = TipoMovimiento.objects.filter(activo=True)
    serializer_class = TipoMovimientoSerializer

class TipoMovimientoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoMovimiento.objects.all()
    serializer_class = TipoMovimientoSerializer

    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()


# ==========================================
# Vistas para MOVIMIENTOS
# ==========================================
class MovimientoListCreateView(generics.ListCreateAPIView):
    queryset = Movimiento.objects.filter(activo=True)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovimientoReadSerializer
        return MovimientoSerializer

class MovimientoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movimiento.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovimientoReadSerializer
        return MovimientoSerializer

    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()


# ==========================================
# Vistas para AJUSTES DE STOCK
# ==========================================
class AjusteListCreateView(generics.ListCreateAPIView):
    queryset = Ajuste.objects.filter(activo=True)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AjusteReadSerializer
        return AjusteSerializer

class AjusteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ajuste.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AjusteReadSerializer
        return AjusteSerializer

    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()


# ==========================================
# Vistas para TRANSFERENCIAS
# ==========================================
class TransferenciaListCreateView(generics.ListCreateAPIView):
    queryset = Transferencia.objects.filter(activo=True)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransferenciaReadSerializer
        return TransferenciaSerializer

class TransferenciaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transferencia.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransferenciaReadSerializer
        return TransferenciaSerializer

    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()