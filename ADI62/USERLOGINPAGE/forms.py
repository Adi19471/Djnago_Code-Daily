from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreationForm(UserCreationForm):
    # password2 = forms.CharField(label='confoirm password(again)')
    class Meta:
        model = User
        fields = ['last_name','first_name','username','email','password']

        labels = {'user':'user','email':'Email','password':'Password'}
        # fields = '__all__'