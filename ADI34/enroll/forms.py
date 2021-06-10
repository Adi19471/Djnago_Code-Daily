from django import forms

class StudentData(forms.Form):
    name=forms.CharField(label="your name chinn",label_suffix='',
     initial="chonna", required=False, disabled=True, localize='chinna')
    email = forms.EmailField()
    mobile = forms.IntegerField()

    def __str__(self):
        return self.name