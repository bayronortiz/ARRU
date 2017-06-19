# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from django.views.generic import CreateView
from .forms import RegistroForm, ReservaForm, CancelarForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from .models import Estudiante
from apps.administrador.models import Toma
from django.db import IntegrityError

# Create your views here.
def index(request):
    return render(request,'estudiante/index.html')

class RegistrarEstudiante(CreateView):
    model = Estudiante
    form_class = RegistroForm
    template_name = "estudiante/registro.html"
    success_url = reverse_lazy("estudiante:index")    # Redirige automaticamente a la principal

    def get_context_data(self, **kwargs):
        context = super(RegistrarEstudiante, self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                registro = form.save()
                return render(request, "estudiante/registro.html", {'form':self.form_class, 'registro_exitoso':True})
            except IntegrityError:
                return render(request, "estudiante/registro.html", {'form':form, 'registro_existe':True})
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ReservarRuta(CreateView):
    model = Toma
    form_class = ReservaForm
    template_name = "estudiante/reserva.html"
    success_url = reverse_lazy("estudiante:index")    # Redirige automaticamente a la principal

    def get_context_data(self, **kwargs):
        context = super(ReservarRuta, self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                reserva = form.save()
                return render(request, "estudiante/reserva.html", {'form':self.form_class, 'reserva_exitosa':True})
            except IntegrityError:
                return render(request, "estudiante/reserva.html", {'form':form, 'existe_reserva':True})
        else:
            return self.render_to_response(self.get_context_data(form=form))

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
            return render(request, template_name, {'form':cancelar_ruta, 'reserva_cancelada':True})
        else:
            cancelar_ruta = CancelarForm()
            return render(request, template_name, {'form':cancelar_ruta, 'reserva_no_existe':True})

    return render(request, template_name, {'form':cancelar_ruta})