# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cliente, Usuario, StatusTarefa, Tarefa, Ponto, CompensacaoHora

admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(StatusTarefa)
admin.site.register(Tarefa)
admin.site.register(Ponto)
admin.site.register(CompensacaoHora)
# Register your models here.
