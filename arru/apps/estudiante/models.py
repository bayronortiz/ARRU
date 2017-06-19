# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Estudiante(models.Model):
    codigo_e = models.CharField(max_length=9, primary_key=True, validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='El código debe ser númerico',
        ),

    ]) #Codigo estudiante
    nombre_e = models.CharField(max_length=30,validators=[
        RegexValidator(
            regex='^[a-zA-Z ]*$',
            message='El nombre no debe contener números',
        ),

     ])  #Nombre estudiante
    apellido_e = models.CharField(max_length=30, validators=[
        RegexValidator(
            regex='^[a-zA-Z ]*$',
            message='El Apellido no debe contener números',
        ),

     ])                 #Apellido estudiante

    def __str__(self):
        return  "%s %s %s" %(self.codigo_e, self.nombre_e, self.apellido_e)