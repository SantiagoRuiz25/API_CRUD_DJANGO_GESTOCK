from rest_framework import serializers

from .models import (
    proveedor,
    proveedor_productos,
    guias_entrada
)

# serializador para proveedor
class proveedorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = proveedor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(proveedorSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True


# serializador para proveedor_productos
class proveedor_productosSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor_productos
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(proveedor_productosSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True


# serializador para guias_entrada
class guias_entradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = guias_entrada
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(guias_entradaSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True