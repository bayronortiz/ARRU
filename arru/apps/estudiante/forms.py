# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django import forms
from .models import Estudiante
from apps.administrador.models import Toma, Ruta

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Estudiante

        fields = [
            'codigo_e',
            'nombre_e',
            'apellido_e',
        ]

        labels = {
            'codigo_e': '',
            'nombre_e': '',
            'apellido_e': '',
        }

        widgets = {
            'codigo_e': forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Código'}),
            'nombre_e': forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Nombre'}),
            'apellido_e': forms.TextInput(attrs={'class': 'textbox', 'placeholder':'Apellido'}),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Toma

        fields = [
            'codigo_e',
            'nombre_r',
            'hora',
            ]

        labels = {
            'codigo_e': '',
            'nombre_r': '',
            'hora': '',
            }

        widgets = {
            'codigo_e': forms.TextInput(attrs={'class': 'textbox', 'placeholder':'Código'}),
            'nombre_r': forms.Select(attrs={'class': 'textbox', 'initial' : 'meme','placeholder':'Ruta'}),
            'hora': forms.Select(attrs={'class': 'textbox', 'placeholder':'Hora'}),
            }


class CancelarForm(forms.ModelForm):
    class Meta:
        model = Toma

        fields =[
            'codigo_e',
            'nombre_r',
            'hora',
            ]

        labels = {
            'codigo_e': '',
            'nombre_r': '',
            'hora': '',
        }

        widgets = {
            'codigo_e': forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Código'}),
            'nombre_r': forms.Select(attrs={'class': 'textbox', 'placeholder': 'Ruta'}),
            'hora': forms.Select(attrs={'class': 'textbox', 'placeholder': 'Hora'}),
        }