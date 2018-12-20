from django.contrib import admin
from django.utils import timezone
from datetime import *
import pytz
from .models import *

class DespesaAdmin(admin.ModelAdmin):
    def proximo(self, obj):
        hoje = datetime.datetime.now()
            return hoje.date() >= obj.vencimento - timedelta(days=2)
    
    list_display = ('tipo_despesa', 'vencimento','forma_pagamento', 'quitado','proximo')
    list_filter = ('quitado','vencimento')
    ordering = ('vencimento','forma_pagamento')
        
    proximo.short_description = 'Vencimento próximo?'
    proximo.boolean = True

admin.site.register(Despesa, DespesaAdmin)



#default:"Administração do Django"
admin.site.site_header='Painel de Controle'

#default:"Administração do Site"
admin.site.index_title='Recursos'

#default:"Site de Administração do Django"
admin.site.site_title='Titulo HTML do Site'

