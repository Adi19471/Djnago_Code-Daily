from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=120)
    branch = models.CharField(max_length=250)
    medeam = models.BooleanField(default=True)

