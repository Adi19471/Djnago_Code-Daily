# forms import 
from django import forms

# models
from .models import User

# validaters
from django .core import validators

class Apply(forms.ModelForm):
    
    class Meta:
      model = User
      fields = ['name']
      label = {'name':'Enter Name'}
   