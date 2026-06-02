from django.db import models

# ==========================================
# Modelo Tabla Categoria_Producto
# ==========================================
class CategoriaProducto(models.Model):
    id_categoria_producto = models.AutoField(primary_key=True, db_column='id_categoria_producto')
    nombre = models.CharField(max_length=50, blank=True, null=True)

    activo = models.BooleanField(default=True)

    usuario_creacion = models.CharField(max_length=100, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre if self.nombre else f"Categoría {self.id_categoria_producto}"

    class Meta:
        db_table = 'categoria_producto'


# ==========================================
# Modelo Tabla Inventario
# ==========================================
class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True, db_column='id_inventario')
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    activo = models.BooleanField(default=True)

    usuario_creacion = models.CharField(max_length=100, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre if self.nombre else f"Inventario {self.id_inventario}"

    class Meta:
        db_table = 'inventario'


# ==========================================
# Modelo Tabla Productos
# ==========================================
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, db_column='id_producto')

    id_categoria_producto = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.CASCADE,
        db_column='id_categoria_producto',
        blank=True,
        null=True
    )

    nombre = models.CharField(max_length=100, blank=True, null=True)
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_inicial = models.IntegerField(default=0, blank=True, null=True)

    activo = models.BooleanField(default=True)

    usuario_creacion = models.CharField(max_length=100, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre if self.nombre else f"Producto {self.id_producto}"

    class Meta:
        db_table = 'productos'


# ==========================================
# Modelo Tabla Inventario_Productos
# ==========================================
class InventarioProductos(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')

    id_inventario = models.ForeignKey(
        Inventario,
        on_delete=models.CASCADE,
        db_column='id_inventario',
        blank=True,
        null=True
    )

    id_producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='id_producto',
        blank=True,
        null=True
    )

    cantidad = models.IntegerField(default=0, blank=True, null=True)

    activo = models.BooleanField(default=True)

    usuario_creacion = models.CharField(max_length=100, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        prod = self.id_producto.nombre if self.id_producto else "Sin Producto"
        inv = self.id_inventario.nombre if self.id_inventario else "Sin Inventario"
        return f"{prod} en {inv}"

    class Meta:
        db_table = 'inventario_productos'


# ==========================================
# Modelo Tabla Tipos_Movimiento
# ==========================================
class TipoMovimiento(models.Model):
    id_tipo_movimiento = models.AutoField(primary_key=True, db_column='id_tipo_movimiento')
    nombre = models.CharField(max_length=50, unique=True, blank=True, null=True)

    activo = models.BooleanField(default=True)

    usuario_creacion = models.CharField(max_length=100, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre if self.nombre else f"Tipo {self.id_tipo_movimiento}"

    class Meta:
        db_table = 'tipos_movimiento'


# ==========================================
# Modelo Tabla Movimientos
# ==========================================
class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True, db_column='id_movimiento')

    id_tipo_movimiento = models.ForeignKey(
        TipoMovimiento,
        on_delete=models.CASCADE,
        db_column='id_tipo_movimiento',
        blank=True,
        null=True
    )

    id_producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='id_producto',
        blank=True,
        null=True
    )

    cantidad = models.IntegerField(blank=True, null=True)
    motivo = models.CharField(max_length=100, blank=True, null=True)

    fecha = models.DateTimeField(auto_now_add=True)

    activo = models.BooleanField(default=True)

    usuario_creacion = models.CharField(max_length=100, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Movimiento {self.id_movimiento}"

    class Meta:
        db_table = 'movimientos'


# ==========================================
# Modelo Tabla Ajustes
# ==========================================
class Ajuste(models.Model):
    id_ajuste = models.AutoField(primary_key=True, db_column='id_ajuste')

    id_producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='id_producto',
        blank=True,
        null=True
    )

    cantidad_esperada = models.IntegerField(blank=True, null=True)
    cantidad_real = models.IntegerField(blank=True, null=True)

    diferencia = models.IntegerField(
        db_column='diferencia',
        editable=False,
        blank=True,
        null=True
    )

    motivo = models.CharField(max_length=100, blank=True, null=True)

    activo = models.BooleanField(default=True)

    usuario_creacion = models.CharField(max_length=100, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ajuste {self.id_ajuste}"

    class Meta:
        db_table = 'ajustes'


# ==========================================
# Modelo Tabla Transferencia
# ==========================================
class Transferencia(models.Model):
    id_transferencia = models.AutoField(primary_key=True, db_column='id_transferencia')

    id_producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='id_producto',
        blank=True,
        null=True
    )

    cantidad = models.IntegerField(blank=True, null=True)

    activo = models.BooleanField(default=True)

    usuario_creacion = models.CharField(max_length=100, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transferencia {self.id_transferencia}"

    class Meta:
        db_table = 'transferencia'