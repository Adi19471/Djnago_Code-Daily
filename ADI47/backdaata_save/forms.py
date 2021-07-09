from django import forms


class Apply(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
