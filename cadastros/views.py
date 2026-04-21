from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Cliente, Equipamento

class PaginaInicialView(TemplateView):
    template_name = "cadastros/index.html"

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'cpf_cnpj', 'telefone', 'endereco']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class EquipamentoCreate(CreateView):
    model = Equipamento
    fields = ['cliente', 'tipo', 'marca', 'modelo', 'numero_serie', 'especificacoes']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')