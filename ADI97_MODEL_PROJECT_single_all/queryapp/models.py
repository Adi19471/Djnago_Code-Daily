from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=70)
    marks = models.CharField(max_length=100)
    pass_date = models.DateField()

    def __str__(self) -> str:
        return self.name


class Techer(models.Model):
    name = models.CharField(max_length=70)
    empnum = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()

    def __str__(self) -> str:
        return self.name