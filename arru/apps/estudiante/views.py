# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.views.generic import CreateView
from .forms import RegistroForm, ReservaForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from .models import Estudiante
from apps.administrador.models import Toma

# Create your views here.
class RegistrarEstudiante(CreateView):
    model = Estudiante
    form_class = RegistroForm
    template_name = "estudiante/registro.html"
    success_url = reverse_lazy('estudiante:registro_estudiante')

class ReservarRuta(CreateView):
    model = Toma
    form_class = ReservaForm
    template_name = "estudiante/reserva.html"
    success_url = reverse_lazy("estudiante:reserva_ruta")


