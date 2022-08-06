from django.contrib import admin

# Register your models here.
from .models import DadosPessoais
from .models import Poll, Choice, Carro

admin.site.register(DadosPessoais)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Carro)

