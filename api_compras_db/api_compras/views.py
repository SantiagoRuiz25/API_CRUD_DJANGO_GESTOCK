from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    proveedor,
    proveedor_productos,
    guias_entrada
)

from .serializers import (
    proveedorSerializer,
    proveedor_productosSerializer,
    guias_entradaSerializer
)


class proveedorViewSet(viewsets.ModelViewSet):
    queryset = proveedor.objects.all()
    serializer_class = proveedorSerializer


class proveedor_productosViewSet(viewsets.ModelViewSet):
    queryset = proveedor_productos.objects.all()
    serializer_class = proveedor_productosSerializer


class guias_entradaViewSet(viewsets.ModelViewSet):
    queryset = guias_entrada.objects.all()
    serializer_class = guias_entradaSerializer

