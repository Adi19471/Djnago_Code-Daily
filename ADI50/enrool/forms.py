# forms import 
from django import forms

# models
from .models import User

# validaters
from django .core import validators

class Apply(forms.ModelForm):
    name = forms.CharField(max_length=50,required=False)
    class Meta:
      model = User
      fields = ['name','email','password']
      label  = {'name':'Enter Your Name','email':'Enter Your password'}
      help_text = {'name':'Enter Your Full Name'}
      widget = {'password':forms.PasswordInput}