from .models import User 

from django import forms

from django.core import validators


class StudentRegistation(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','mobile','password']

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
