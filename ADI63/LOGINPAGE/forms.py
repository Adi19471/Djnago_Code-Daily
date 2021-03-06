from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):
    password2 = forms.CharField(label='Confoirm password(agin)',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels ={'email':'Email'}