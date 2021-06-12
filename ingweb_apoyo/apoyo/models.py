from django.db import models

# Create your models here.

# Create Modelo para Categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="ID categoría")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")

    def __str__(self):
        return self.nombreCategoria

# Create Modelo para insumo

class Producto(models.Model):
    idProducto = models.CharField(max_length=4, primary_key=True, verbose_name="ID Producto")
    marca = models.CharField(max_length=40, blank=False, null=False, verbose_name="Marca Producto")
    nombreProducto = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre Producto")
    precio = models.IntegerField(null=False, blank=False, verbose_name="Precio Unitario")
    stock = models.IntegerField(null=True, blank=True, verbose_name="Stock")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.idProducto

class Residente(models.Model):
    idResidente = models.CharField(max_length=9, primary_key=True, verbose_name="Rut sin puntos")
    nombreResidente = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre Completo del Residente")
    edad = models.IntegerField(null=False, blank=False, verbose_name="Edad")
    nombreFamiliar = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre de familiar a cargo")
    imagenCarnet = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Foto carnet")

    def __str__(self):
        return self.idResidente
