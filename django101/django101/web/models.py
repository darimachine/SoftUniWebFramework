from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=32
    )
    def __str__(self):
        return self.name
class Todo(models.Model):
    TITLE_MAX_LENGTH = 24
    title=models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    description=models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title