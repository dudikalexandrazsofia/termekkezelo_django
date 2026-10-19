from django import forms

from .models import Termek


class TermekForm(forms.ModelForm):
    class Meta:
        model = Termek
        fields = ['nev', 'leiras', 'ar', 'keszlet']
        widgets = {'leiras': forms.Textarea(attrs={'rows': 3})}
        error_messages = {
            'nev': {'required': 'A név megadása kötelező.'},
            'ar': {'required': 'Az ár megadása kötelező.'},
            'keszlet': {'required': 'A készlet megadása kötelező.'},
        }