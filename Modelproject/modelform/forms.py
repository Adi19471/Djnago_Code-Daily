from .models import Hero
from django import forms

class HeroForm(forms.ModelForm):
    class Meta:
        model= Hero
        fields='__all__'