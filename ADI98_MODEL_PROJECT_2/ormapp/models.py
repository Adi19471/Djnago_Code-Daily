from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=120)
    scale_type =models.CharField(max_length=220)
    scale_price = models.IntegerField()

    def __str__(self) -> str:
        return self.name