# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView
from .forms import RegistroForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from .models import Estudiante

# Create your views here.
class RegistrarEstudiante(CreateView):
    model = Estudiante
    form_class = RegistroForm
    template_name = "estudiante/registro.html"
    success_url = reverse_lazy('estudiante:registro_estudiante')