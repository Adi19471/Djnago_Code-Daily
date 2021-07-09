from django.db import models

# Create your models here.
class User(models.Model):
    na = models.CharField(max_length=100)
    ts = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=105)

    # def __str__(self):
    #     return self.name
    