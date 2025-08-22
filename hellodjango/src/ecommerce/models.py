from django.db import models

# Create your models here.
class ProductModel(models.Model): # Este modelo se guardará en la base de datos
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    seller = models.TextField()
    avalability = models.IntegerField(default=1)