from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=350)
    desc = models.TextField()
    date_time = models.DateField()

    