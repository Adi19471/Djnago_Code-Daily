from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=35)
    password = models.CharField(max_length=30,blank=True)

class Meta:
        ordering = ['userName']
        verbose_name = 'User MetaData'
        verbose_name_plural = 'Users MetaData'
        def __unicode__(self):
            return str(self.userName)
