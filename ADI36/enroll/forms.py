from django import forms

class StudentData(forms.Form):
    name= forms.CharField()
    email = forms.EmailField()
    