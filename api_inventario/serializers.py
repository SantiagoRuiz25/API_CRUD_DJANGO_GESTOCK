from rest_framework import serializers
from .models import (
    CategoriaProducto, Producto, Inventario, 
    InventarioProductos, TipoMovimiento, Movimiento, 
    Ajuste, Transferencia
)

# ==========================================
# Serializer CategoriaProducto
# ==========================================
class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'


# ==========================================
# Serializers Producto
# ==========================================
class ProductoSerializer(serializers.ModelSerializer):
    """Maneja la creación y edición usando IDs directos"""
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoReadSerializer(serializers.ModelSerializer):
    """Maneja la lectura anidando los datos de la categoría"""
    categoria = CategoriaProductoSerializer(read_only=True)
    
    class Meta:
        model = Producto
        fields = '__all__'


# ==========================================
# Serializer Inventario (Bodegas)
# ==========================================
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'


# ==========================================
# Serializers InventarioProductos (Stock)
# ==========================================
class InventarioProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioProductos
        fields = '__all__'

class InventarioProductosReadSerializer(serializers.ModelSerializer):
    inventario = InventarioSerializer(read_only=True)
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = InventarioProductos
        fields = '__all__'


# ==========================================
# Serializer Tipos de Movimiento
# ==========================================
class TipoMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMovimiento
        fields = '__all__'


# ==========================================
# Serializers Movimientos
# ==========================================
class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = '__all__'

class MovimientoReadSerializer(serializers.ModelSerializer):
    inventario = InventarioSerializer(read_only=True)
    producto = ProductoSerializer(read_only=True)
    tipo_movimiento = TipoMovimientoSerializer(read_only=True)

    class Meta:
        model = Movimiento
        fields = '__all__'


# ==========================================
# Serializers Ajustes
# ==========================================
class AjusteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ajuste
        fields = '__all__'

class AjusteReadSerializer(serializers.ModelSerializer):
    inventario_producto = InventarioProductosReadSerializer(read_only=True)

    class Meta:
        model = Ajuste
        fields = '__all__'


# ==========================================
# Serializers Transferencias
# ==========================================
class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transferencia
        fields = '__all__'

class TransferenciaReadSerializer(serializers.ModelSerializer):
    inventario_origen = InventarioSerializer(read_only=True)
    inventario_destino = InventarioSerializer(read_only=True)
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = Transferencia
        fields = '__all__'