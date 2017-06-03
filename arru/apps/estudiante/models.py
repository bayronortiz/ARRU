# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Estudiante(models.Model):
    codigo_e = models.CharField(max_length=9, primary_key=True) #Codigo estudiante
    nombre_e = models.CharField(max_length=30)                  #Nombre estudiante
    apellido_e = models.CharField(max_length=30)                #Apellido estudiante

    def __str__(self):
        return  "%s %s %s" %(self.codigo_e, self.nombre_e, self.apellido_e)
