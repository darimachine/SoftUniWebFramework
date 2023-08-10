from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

class Product(models.Model):
    NAME_MAX_LENGTH = 25
    PRICE_MIN_VALUE = 0
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    price = models.FloatField(
        validators=[
            MinValueValidator(PRICE_MIN_VALUE)
        ]
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )



