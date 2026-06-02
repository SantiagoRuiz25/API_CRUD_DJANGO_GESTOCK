from rest_framework import serializers

# Importamos los modelos con las mayúsculas correctas
from .models import (
    Roles,
    Usuarios,
    ContrasenaHash,
    RecuperacionContrasena,
)

# Serializador para Roles
class rolesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Roles  # <-- Corregido a Mayúscula
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(rolesSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True


# Serializador para Usuarios
class usuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios  # <-- Corregido a Mayúscula
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(usuariosSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True


# Serializador para Contraseña Hash
class contrasena_hashSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContrasenaHash  # <-- Corregido a Mayúscula
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(contrasena_hashSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True
                

# Serializador para Recuperación de Contraseña
class recuperacion_contrasenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecuperacionContrasena  # <-- Corregido a Mayúscula
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(recuperacion_contrasenaSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True