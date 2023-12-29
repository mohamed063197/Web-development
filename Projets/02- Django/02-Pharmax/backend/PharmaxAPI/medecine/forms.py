from django import forms
from .models import Medecine

class MedecineForm(forms.ModelForm):
 
    class Meta:
        model = Medecine
        fields = ('title', 'desc', 'favorite', 'slug', 'img')
        
