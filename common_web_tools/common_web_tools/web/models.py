from django.db import models

# Create your models here.
class Profile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk} {self.name} {self.email}"