from django.db import models

class proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    # Corrección: Se eliminó max_length porque IntegerField no lo soporta en Django
    telefono = models.IntegerField(max_length=10)  
    activo = models.BooleanField(default=True)
    
    # Campos de auditoría de usuarios (Agregados para el Serializer)
    usuario_creacion = models.CharField(max_length=100, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=100, null=True, blank=True)
    
    # Fechas automáticas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class guias_entrada(models.Model):
    id_guia = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey(
        proveedor,
        on_delete=models.CASCADE,
        db_column='id_proveedor'
    )
    estado = models.CharField(max_length=50)
    # Corrección: Se quitó el unique=True. Si lo dejas, no podrías registrar dos guías con el mismo correo
    correo = models.EmailField()  
    activo = models.BooleanField(default=True)
    
    # Campos de auditoría de usuarios (Agregados para el Serializer)
    usuario_creacion = models.CharField(max_length=100, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=100, null=True, blank=True)
    
    # Fechas automáticas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


class proveedor_productos(models.Model):
    id_proveedor_productos = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey(
        proveedor,
        on_delete=models.CASCADE,
        db_column='id_proveedor'
    )
    id_producto = models.IntegerField()
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    activo = models.BooleanField(default=True)
    
    # Campos de auditoría de usuarios (Agregados para el Serializer)
    usuario_creacion = models.CharField(max_length=100, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=100, null=True, blank=True)
    
    # Fechas automáticas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)