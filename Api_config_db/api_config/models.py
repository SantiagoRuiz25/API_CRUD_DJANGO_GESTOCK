from django.db import models


class sistema(models.Model):
    id_sistema = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    correo_empresa = models.EmailField(max_length=100)

    usuario_creacion = models.IntegerField(null=True, blank=True)
    usuario_modificacion = models.IntegerField(null=True, blank=True)

    activo = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


class backup(models.Model):
    id_backup = models.AutoField(primary_key=True)

    copia_seguridad = models.BooleanField()
    frecuencia = models.CharField(max_length=50)

    usuario_creacion = models.IntegerField(null=True, blank=True)
    usuario_modificacion = models.IntegerField(null=True, blank=True)

    activo = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


class seguridad(models.Model):
    id_seguridad = models.AutoField(primary_key=True)

    tiempo_sesion = models.TimeField()

    usuario_creacion = models.IntegerField(null=True, blank=True)
    usuario_modificacion = models.IntegerField(null=True, blank=True)

    activo = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


class notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)

    noti_stock_bajo = models.BooleanField()
    noti_movimiento = models.BooleanField()

    usuario_creacion = models.IntegerField(null=True, blank=True)
    usuario_modificacion = models.IntegerField(null=True, blank=True)

    activo = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)