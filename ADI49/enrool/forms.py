# forms import 
from django import forms

# models
from .models import User

# validaters
from django .core import validators

class Apply(forms.ModelForm):
    class Meta:
        model = User

        fields = ['name','email','password']
        label  = {'name':'Enter Your Name','email':'Enter Your password'}
        help_text = {'name':'Enter Your Full Name'}
        error_messages = {'name':{'required':'name is not mentiones'}}

        widget = {'password':forms.PasswordInput,'name':forms.TextInput(attrs={'class':'myclass','placeholder':'ADI'})}