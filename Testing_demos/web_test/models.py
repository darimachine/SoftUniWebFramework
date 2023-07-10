from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from common.validator import only_letters_validator


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100,validators=(only_letters_validator,))

    last_name= models.CharField(max_length=100,validators=(only_letters_validator,))

    age = models.IntegerField(
        MinValueValidator(0),

    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'