from django.db import models

# Create your models here.
class ProductModel(models.Model): # Este modelo se guardará en la base de datos
    title = models.CharField(max_length=50, default="producto de desconocido")
    price = models.FloatField(default=1.1)
    description = models.TextField(default="Inserte descripción")
    seller = models.TextField(default="Temu")
    availability = models.IntegerField(default=1) 