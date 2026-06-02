from rest_framework import serializers

from .models import (
    CategoriaProducto,
    Producto,
    Inventario,
    InventarioProductos,
    TipoMovimiento,
    Movimiento,
    Ajuste,
    Transferencia
)

# ==========================================
# SERIALIZER BASE AUDITORIA
# ==========================================
class AuditoriaSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')

        if request:

            if request.method == 'POST':

                if 'usuario_modificacion' in self.fields:
                    self.fields['usuario_modificacion'].read_only = True

            elif request.method in ['PUT', 'PATCH']:

                if 'usuario_creacion' in self.fields:
                    self.fields['usuario_creacion'].read_only = True

                if 'usuario_modificacion' in self.fields:
                    self.fields['usuario_modificacion'].required = True


# ==========================================
# CATEGORIA PRODUCTO
# ==========================================
class CategoriaProductoSerializer(AuditoriaSerializer):

    class Meta:
        model = CategoriaProducto
        fields = '__all__'


# ==========================================
# PRODUCTOS
# ==========================================
class ProductoSerializer(AuditoriaSerializer):

    class Meta:
        model = Producto
        fields = '__all__'


class ProductoReadSerializer(serializers.ModelSerializer):

    id_categoria_producto = CategoriaProductoSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'


# ==========================================
# INVENTARIO
# ==========================================
class InventarioSerializer(AuditoriaSerializer):

    class Meta:
        model = Inventario
        fields = '__all__'


# ==========================================
# INVENTARIO PRODUCTOS
# ==========================================
class InventarioProductosSerializer(AuditoriaSerializer):

    class Meta:
        model = InventarioProductos
        fields = '__all__'


class InventarioProductosReadSerializer(serializers.ModelSerializer):

    id_inventario = InventarioSerializer(read_only=True)
    id_producto = ProductoReadSerializer(read_only=True)

    class Meta:
        model = InventarioProductos
        fields = '__all__'


# ==========================================
# TIPOS MOVIMIENTO
# ==========================================
class TipoMovimientoSerializer(AuditoriaSerializer):

    class Meta:
        model = TipoMovimiento
        fields = '__all__'


# ==========================================
# MOVIMIENTOS
# ==========================================
class MovimientoSerializer(AuditoriaSerializer):

    class Meta:
        model = Movimiento
        fields = '__all__'


class MovimientoReadSerializer(serializers.ModelSerializer):

    id_tipo_movimiento = TipoMovimientoSerializer(read_only=True)
    id_producto = ProductoReadSerializer(read_only=True)

    class Meta:
        model = Movimiento
        fields = '__all__'


# ==========================================
# AJUSTES
# ==========================================
class AjusteSerializer(AuditoriaSerializer):

    class Meta:
        model = Ajuste
        fields = '__all__'

        extra_kwargs = {
            'diferencia': {'read_only': True}
        }


class AjusteReadSerializer(serializers.ModelSerializer):

    id_producto = ProductoReadSerializer(read_only=True)

    class Meta:
        model = Ajuste
        fields = '__all__'


# ==========================================
# TRANSFERENCIAS
# ==========================================
class TransferenciaSerializer(AuditoriaSerializer):

    class Meta:
        model = Transferencia
        fields = '__all__'


class TransferenciaReadSerializer(serializers.ModelSerializer):

    id_producto = ProductoReadSerializer(read_only=True)

    class Meta:
        model = Transferencia
        fields = '__all__'