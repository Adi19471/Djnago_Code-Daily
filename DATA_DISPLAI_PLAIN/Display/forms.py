from django import forms

class AdharCard(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
   
    messages = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


    # def __str__(self):
    #     return self(name)