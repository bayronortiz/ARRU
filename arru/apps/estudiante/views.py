# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from django.views.generic import CreateView
from .forms import RegistroForm, ReservaForm, CancelarForm
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

def eliminar_ruta(request):
    template_name = "estudiante/cancelar.html"
    cancelar_ruta = CancelarForm()

    if request.method == 'POST':
        codigo = request.POST.get('codigo_e')
        hora = request.POST.get('hora')
        nombre_ruta = request.POST.get('nombre_r')
        reserva = Toma.objects.filter(codigo_e__codigo_e=codigo, nombre_r__nombre_r=nombre_ruta, hora=hora).first()

        if reserva:
            reserva.delete()
            return render(request, template_name, {'form':cancelar_ruta, 'msg':'Cupo eliminado Correctamente.'})
        else:
            cancelar_ruta = CancelarForm()
            return render(request, template_name, {'form':cancelar_ruta, 'msg':'Cupo no encontrado.'})

    return render(request, template_name, {'form':cancelar_ruta})


