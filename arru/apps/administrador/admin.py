# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Administrador)
admin.site.register(Conductor)
admin.site.register(Bus)
admin.site.register(Paradero)
admin.site.register(Posee)
admin.site.register(Ruta)
admin.site.register(Toma)
