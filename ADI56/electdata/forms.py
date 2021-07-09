from django import forms

# from django.core import validators

from .models import User

class StudentRegister(forms.ModelForm):
    class Meta:
        model = User
    
        fields = ['na','ts','password','email']


     

       