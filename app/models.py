from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    descripcion = models.TextField("descripción")
    precio = models.DecimalField("precio", max_digits=10, decimal_places=2)
    stock =  models.PositiveBigIntegerField("stock", default=0)
    creado = models.DateTimeField("creado", auto_now_add=True)
    actualizado = models.DateTimeField("actualizado", auto_now=True)
    imagen = models.ImageField("imagen", upload_to="productos/", blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"