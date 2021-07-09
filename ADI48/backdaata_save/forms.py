from django import forms
from .models import User
from django.core import validators

class Apply(forms.ModelForm):
    class Meta:
     model = User
     fields = ['name','password','email']