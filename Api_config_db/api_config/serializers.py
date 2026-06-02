from rest_framework import serializers

from .models import (
    sistema,
    backup,
    seguridad,
    notificacion
)


class sistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = sistema
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(sistemaSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True


class backupSerializer(serializers.ModelSerializer):
    class Meta:
        model = backup
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(backupSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True


class seguridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = seguridad
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(seguridadSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True


class notificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = notificacion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(notificacionSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'POST':
                self.fields['usuario_modificacion'].read_only = True
            elif request.method in ['PUT', 'PATCH']:
                self.fields['usuario_creacion'].read_only = True
                self.fields['usuario_modificacion'].required = True