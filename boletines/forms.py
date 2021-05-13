from django import forms
from .models import Boletin

class BoletinForm(forms.ModelForm):
    class Meta:
        model = Boletin
        fields = [
            'name',
            'materia',
            'nota',
        ]
        labels = {
            'name': 'Name',
            'materia':'Materia',
            'nota': 'Nota',
        }