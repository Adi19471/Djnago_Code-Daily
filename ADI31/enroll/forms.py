from django import forms

class StudentData(forms.Form):
    name = forms.CharField(initial="chinna")
    email = forms.EmailField()
    first_name = forms.CharField()
    phone = forms.CharField()