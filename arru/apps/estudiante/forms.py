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
            'codigo_e': 'Código',
            'nombre_e': 'Nombre',
            'apellido_e': 'Apellido',
        }

        widgets = {
            'codigo_e': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_e': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_e': forms.TextInput(attrs={'class': 'form-control'}),
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
            'codigo_e': 'Código',
            'nombre_r': 'Ruta',
            'hora': 'Hora',
            }

        widgets = {
            'codigo_e': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_r': forms.Select(attrs={'class': 'form-control'}),
            'hora': forms.Select(attrs={'class': 'form-control'}),
            }

