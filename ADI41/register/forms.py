from django import forms
from django.core import validators


class Reg(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField(validators=[validators.MaxLengthValidator(15)])
    password = forms.CharField(widget=forms.PasswordInput)