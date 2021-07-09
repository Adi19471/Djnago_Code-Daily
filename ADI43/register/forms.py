from django import forms
from django.core import validators

def starts_with_a(value):
    if value[0] !='a':
        raise forms.ValidationError("The name should be 'A' is better your naeme",)
class Reg(forms.Form):
    name = forms.CharField(validators=[starts_with_a])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)