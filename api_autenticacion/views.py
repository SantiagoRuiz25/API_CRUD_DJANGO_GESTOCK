from rest_framework import viewsets
from .models import Roles, Usuarios, ContrasenaHash, RecuperacionContrasena

# Importamos los serializers exactamente como están escritos en tu archivo (con minúsculas)
from .serializers import (
    rolesSerializer, 
    usuariosSerializer, 
    contrasena_hashSerializer, 
    recuperacion_contrasenaSerializer
)

# ViewSet para Roles
class rolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = rolesSerializer

# ViewSet para Usuarios
class usuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = usuariosSerializer  # <-- Asegúrate de que use la minúscula aquí también

# ViewSet para Contraseña Hash
class contrasena_hashViewSet(viewsets.ModelViewSet):
    queryset = ContrasenaHash.objects.all()
    serializer_class = contrasena_hashSerializer

# ViewSet para Recuperación de Contraseña
class recuperacion_contrasenaViewSet(viewsets.ModelViewSet):
    queryset = RecuperacionContrasena.objects.all()
    serializer_class = recuperacion_contrasenaSerializer