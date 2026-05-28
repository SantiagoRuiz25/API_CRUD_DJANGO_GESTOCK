from django.db import models

# ==========================================
# Modelo Tabla Categoria_Producto
# ==========================================
class CategoriaProducto(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria_producto'


# ==========================================
# Modelo Tabla Productos
# ==========================================
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.CASCADE,
        db_column='categoria_id'
    )
    nombre = models.CharField(max_length=150)
    sku = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'


# ==========================================
# Modelo Tabla Inventario (Bodegas/Ubicaciones)
# ==========================================
class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    nombre_bodega = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_bodega

    class Meta:
        db_table = 'inventario'


# ==========================================
# Modelo Tabla Inventario_Productos (Stock Intermedio)
# ==========================================
class InventarioProductos(models.Model):
    id_inventario_producto = models.AutoField(primary_key=True)
    inventario = models.ForeignKey(
        Inventario,
        on_delete=models.CASCADE,
        db_column='inventario_id'
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='producto_id'
    )
    cantidad = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.producto.nombre} en {self.inventario.nombre_bodega} ({self.cantidad})"

    class Meta:
        db_table = 'inventario_productos'


# ==========================================
# Modelo Tabla Tipos_Movimiento
# ==========================================
class TipoMovimiento(models.Model):
    id_tipo_movimiento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)  # Ej: 'Entrada', 'Salida'
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipos_movimiento'


# ==========================================
# Modelo Tabla Movimientos
# ==========================================
class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    inventario = models.ForeignKey(
        Inventario,
        on_delete=models.CASCADE,
        db_column='inventario_id'
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='producto_id'
    )
    tipo_movimiento = models.ForeignKey(
        TipoMovimiento,
        on_delete=models.CASCADE,
        db_column='tipo_movimiento_id'
    )
    cantidad = models.IntegerField()
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mov {self.id_movimiento} - {self.tipo_movimiento.nombre}: {self.cantidad} pzs"

    class Meta:
        db_table = 'movimientos'


# ==========================================
# Modelo Tabla Ajustes
# ==========================================
class Ajuste(models.Model):
    id_ajuste = models.AutoField(primary_key=True)
    inventario_producto = models.ForeignKey(
        InventarioProductos,
        on_delete=models.CASCADE,
        db_column='inventario_producto_id'
    )
    cantidad_ajustada = models.IntegerField()  # Puede ser positivo o negativo
    motivo = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ajuste {self.id_ajuste} - Cantidad: {self.cantidad_ajustada}"

    class Meta:
        db_table = 'ajustes'


# ==========================================
# Modelo Tabla Transferencia
# ==========================================
class Transferencia(models.Model):
    id_transferencia = models.AutoField(primary_key=True)
    inventario_origen = models.ForeignKey(
        Inventario,
        on_delete=models.CASCADE,
        related_name='transferencias_origen',
        db_column='inventario_origen_id'
    )
    inventario_destino = models.ForeignKey(
        Inventario,
        on_delete=models.CASCADE,
        related_name='transferencias_destino',
        db_column='inventario_destino_id'
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='producto_id'
    )
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=50, default='Pendiente')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transf {self.id_transferencia}: {self.inventario_origen} -> {self.inventario_destino}"

    class Meta:
        db_table = 'transferencia'
# Create your models here.
