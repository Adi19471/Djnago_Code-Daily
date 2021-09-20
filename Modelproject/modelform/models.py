from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=200,default=None)
    company_name = models.CharField(max_length=150,default=None)
    bike_name =models.CharField(max_length=100,default=None)
    bike_message = models.TextField()
    deliver_date = models.DateField(auto_now_add=True)
    