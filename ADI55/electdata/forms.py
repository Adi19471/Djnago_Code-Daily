from django import forms

# from django.core import validators

from .models import User

class StudentRegister(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name','password','email']
        # fields = '__all__'

        exclude =['name']