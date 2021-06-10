from django import forms

class StudentData(forms.Form):
    name=forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()

    def __str__(self):
        return self.name