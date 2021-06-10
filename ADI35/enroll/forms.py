from django import forms

class StudentData(forms.Form):
    name= forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())
    mobile = forms.IntegerField(widget=forms.NumberInput())
    firs_name = forms.CharField(widget=forms.Textarea)
    check = forms.CharField(widget=forms.CheckboxInput)
    radio = forms.CharField(widget=forms.RadioSelect)
    # url = forms.CharField(widget=forms.URLField)
    time = forms.CharField(widget=forms.TimeInput)
    date = forms.DateField(widget=forms.DateInput)
    file_uplode = forms.CharField(widget=forms.FileInput)

    name = forms.CharField(widget=forms.Textarea(attrs={'name':'chinna'}))

    data = forms.EmailField(widget=forms.EmailInput(attrs={'email':'adi@gmail.com','placeholder':'akumatha@'}))
    # def __str__(self):
    #     return self.name