from django import forms

#models import 
from .models import Image

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'image':''}


    def __unicode__(self):
        return self.name
    

