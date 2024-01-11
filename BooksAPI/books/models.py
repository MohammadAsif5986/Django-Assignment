from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

