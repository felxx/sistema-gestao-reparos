from django.contrib import admin
from .models import Cliente, Equipamento, ServicoTabelado, Peca, OrdemDeServico, ItemOS

admin.site.register(Cliente)
admin.site.register(Equipamento)
admin.site.register(ServicoTabelado)
admin.site.register(Peca)
admin.site.register(OrdemDeServico)
admin.site.register(ItemOS)