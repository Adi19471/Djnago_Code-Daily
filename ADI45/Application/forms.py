from django import forms

class Tata(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label = 'Password(again)',widget=forms.PasswordInput)

    def clean(self):
        cleaed_data = super().clean()
        valpasw = self.cleaned_data['password']
        valrpasw = self.cleaned_data['rpassword']

        if valpasw != valrpasw :
            raise forms.ValidationError("both arae not equal")