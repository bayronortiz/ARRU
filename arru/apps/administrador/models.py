# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from apps import *
from apps.estudiante.models import Estudiante

# Create your models here.
class Administrador(models.Model):
    usuario = models.OneToOneField(User)  #Nombre usuario administrador

    def __str__(self):
        return self.usuario.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Administrador.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)


class Conductor(models.Model):
    id_c = models.CharField(max_length=10, primary_key=True)  #Cedula conductor, llave primaria
    nombre_c = models.CharField(max_length=30)  # Nombre conductor
    apellido_c = models.CharField(max_length=30)  # Nombre conductor

    def __str__(self):
        return  "%s %s" %(self.id_c, self.nombre_c)

class Bus(models.Model):
    cod_bus = models.CharField(max_length=3, primary_key=True)  #Codigo del bus, llave primaria
    capacidad = models.IntegerField()  # Capacidad del bus
    id_c = models.ForeignKey(Conductor, on_delete=models.CASCADE)  # Relaciona el bus con un conductor, llave foranea

    def __str__(self):
        return  "%s" %(self.cod_bus)

class Paradero(models.Model):
    cod_p = models.CharField(max_length=3, primary_key=True)  # Codigo del paradero, llave primaria
    nombre_p = models.CharField(max_length=30)  # Nombre del paradero
    direccion = models.CharField(max_length=30)  # Direccion exacta del paradero

    def __str__(self):
        return  "%s %s" %(self.nombre_p, self.cod_p)

class Ruta(models.Model):
    nombre_r = models.CharField(max_length=20, primary_key=True)  # Nombre de  ruta
    cod_bus = models.ForeignKey(Bus, on_delete=models.CASCADE)  # Relaciona la ruta con un bus, llave foranea
    paraderos = models.ManyToManyField(Paradero, through='Posee') # Indica que una ruta tiene muchos paraderos

    def __str__(self):
        return  self.nombre_r

class Posee(models.Model):
    nombre_r = models.ForeignKey(Ruta, on_delete=models.CASCADE)  # Relaciona la ruta, llave foranea
    cod_p = models.ForeignKey(Paradero, on_delete=models.CASCADE)  # Relaciona el codigo de paradero, llave foranea

    def __str__(self):
        return  "%s %s" %(self.nombre_r, self.cod_p)

class Toma(models.Model):
    HORA_SALIDA = (
        ('11', '11:00 AM'),
        ('12', '12:00 PM'),
        ('5',  '05:00 PM'),
        ('6',  '06:00 PM'),
    )
    hora = models.CharField(max_length=2, choices=HORA_SALIDA)  #Hora a la que sale la ruta, llave primaria
    fecha = models.DateField(max_length=20, auto_now_add=True)  # Fecha  en la que se toma la ruta, llave primaria
    nombre_r = models.ForeignKey(Ruta, on_delete=models.CASCADE)  # Relaciona la ruta que se tomo, llave primaria
    codigo_e = models.ForeignKey(Estudiante, on_delete=models.CASCADE)  # Relaciona el estudiante que tomo la ruta, llave primaria

    class Meta:
        unique_together = (('hora', 'fecha', 'codigo_e'), )#Llave primaria compuesta

    def __str__(self):
        return "%s %s %s" % (self.nombre_r, self.codigo_e, self.hora)