from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Carro)

admin.site.register(Agendamento)

admin.site.register(Servico)

admin.site.register(Passageiro)

admin.site.register(Motorista)
