from django import forms
from django.core import validators

class Tata(forms.Form):
    name = forms.CharField(error_messages={'required':'enter your name'})
    email = forms.EmailField(error_messages={'required':'enter your email'})
    password = forms.CharField(widget=forms.PasswordInput)
    # rpassword = forms.CharField(label = 'Password(again)',widget=forms.PasswordInput)

