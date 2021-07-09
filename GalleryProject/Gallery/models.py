from django.db import models

# Create your models here.
class Image(models.Model):
    # name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    date  = models.DateTimeField(auto_now_add=True)

    