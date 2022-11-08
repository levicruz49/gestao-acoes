from django.contrib import admin
from gestaoacoes.base.apps.configuracoes.models import Corretora, EmpresasListadas

# Register your models here.

admin.site.register(Corretora)
admin.site.register(EmpresasListadas)