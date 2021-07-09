from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    

    def clean(self):
        cleaned_data = super().clean()
        valname = self.changed_data['name']
        valemail = self.cleaned_data['email']
        if len(valname) < 5 :
            raise forms.ValidationError("ray put 5 charecter above")
        if len(valemail) < 6 :
            raise formas.validationError("nerror above 5 characters")

    