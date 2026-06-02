from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import rolesViewSet, usuariosViewSet, contrasena_hashViewSet, recuperacion_contrasenaViewSet

from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

#registro de endpoints del api

router.register(r'roles', rolesViewSet)
router.register(r'usuarios', usuariosViewSet)
router.register(r'contrasena_hash', contrasena_hashViewSet)
router.register(r'recuperacion_contrasena', recuperacion_contrasenaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]