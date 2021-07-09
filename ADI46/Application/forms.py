from django import forms
from django.core import validators

class Tata(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    name = forms.CharField(error_messages={'required':'enter your name'})
    email = forms.EmailField(error_messages={'required':'enter your email'})
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter Your password'},max_length=50,min_length=10)
    # rpassword = forms.CharField(label = 'Password(again)',widget=forms.PasswordInput)

