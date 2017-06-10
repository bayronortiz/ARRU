from django import forms
from .models import Estudiante

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Estudiante

        fields = [
            'codigo_e',
            'nombre_e',
            'apellido_e',
        ]

        labels = {
            'codigo_e': 'Codigo',
            'nombre_e': 'Nombre',
            'apellido_e': 'Apellido',
        }

        widgets = {
            'codigo_e': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_e': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_e': forms.TextInput(attrs={'class': 'form-control'}),
        }