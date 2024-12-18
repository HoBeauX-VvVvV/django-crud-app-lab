from django import forms
from .models import Dogs

class DogsForm(forms.ModelForm):
    class Meta:
        model = Dogs
        fields = ['name', 'breed', 'color', 'age']