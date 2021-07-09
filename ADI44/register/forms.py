from django import forms
from django.core import validators


class Reg(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='password(again)',widget=forms.PasswordInput)

    def clean(self):
        