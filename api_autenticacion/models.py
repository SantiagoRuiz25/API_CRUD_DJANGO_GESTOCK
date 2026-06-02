from django.db import models

class Roles(models.Model):
    id_rol = models.BigAutoField(primary_key=True)  # Cambiado a BigAutoField para Postgres
    nombre_rol = models.CharField(unique=True, max_length=100)
    activo = models.BooleanField(default=True)
    
    # Campos de auditoría de usuarios
    usuario_creacion = models.CharField(max_length=100, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=100, null=True, blank=True)
    
    # Fechas automáticas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True  # ¡AHORA SÍ DJANGO CREARÁ LA TABLA!
        db_table = 'roles'


class Usuarios(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    id_rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_rol')
    correo = models.CharField(unique=True, max_length=150)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    documento = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    
    # Campos de auditoría de usuarios
    usuario_creacion = models.CharField(max_length=100, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=100, null=True, blank=True)
    
    # Fechas automáticas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True  # ¡AHORA SÍ DJANGO CREARÁ LA TABLA!
        db_table = 'usuarios'


class RecuperacionContrasena(models.Model):
    id_recuperacion = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usuario')
    codigo_verificacion = models.CharField(max_length=100, blank=True, null=True)
    fecha_expiracion = models.DateTimeField(blank=True, null=True)
    usado = models.BooleanField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    
    # Campos de auditoría de usuarios
    usuario_creacion = models.CharField(max_length=100, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=100, null=True, blank=True)
    
    # Fechas automáticas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True  # ¡AHORA SÍ DJANGO CREARÁ LA TABLA!
        db_table = 'recuperacion_contrasena'


class ContrasenaHash(models.Model):
    id_contrasena_hash = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usuario')
    contrasena_hash = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    
    # Campos de auditoría de usuarios
    usuario_creacion = models.CharField(max_length=100, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=100, null=True, blank=True)
    
    # Fechas automáticas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True  # ¡AHORA SÍ DJANGO CREARÁ LA TABLA!
        db_table = 'contrasena_hash'