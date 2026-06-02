from rest_framework import viewsets

from .models import (
    sistema,
    backup,
    seguridad,
    notificacion
)

from .serializers import (
    sistemaSerializer,
    backupSerializer,
    seguridadSerializer,
    notificacionSerializer
)


class sistemaViewSet(viewsets.ModelViewSet):
    queryset = sistema.objects.all()
    serializer_class = sistemaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario_creacion=1)


class backupViewSet(viewsets.ModelViewSet):
    queryset = backup.objects.all()
    serializer_class = backupSerializer

    def perform_create(self, serializer):
        serializer.save(usuario_creacion=1)


class seguridadViewSet(viewsets.ModelViewSet):
    queryset = seguridad.objects.all()
    serializer_class = seguridadSerializer

    def perform_create(self, serializer):
        serializer.save(usuario_creacion=1)


class notificacionViewSet(viewsets.ModelViewSet):
    queryset = notificacion.objects.all()
    serializer_class = notificacionSerializer

    def perform_create(self, serializer):
        serializer.save(usuario_creacion=1)