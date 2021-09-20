from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=120)
    roll = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=120)
    marks = models.IntegerField()
    passdate = models.DateField()
    admdatetime = models.DateTimeField()


    def __str__(self) -> str:
        return self.name