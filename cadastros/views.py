from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClienteForm, EquipamentoForm
from .models import Cliente, Equipamento, Peca
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PaginaInicialView(TemplateView):
    template_name = "cadastros/index.html"

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'cpf_cnpj', 'telefone', 'endereco']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-clientes')
    extra_context = {'titulo': 'Cadastrar Novo Cliente'}

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-clientes')

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cadastros/form_excluir.html'
    success_url = reverse_lazy('listar-clientes')

class ClienteList(ListView):
    model = Cliente
    template_name = 'cadastros/listar_clientes.html' 
    extra_context = {'titulo': 'Lista de Clientes Cadastrados'}

class ClienteDetail(DetailView):
    model = Cliente
    template_name = 'cadastros/detalhar_cliente.html'

class EquipamentoCreate(CreateView):
    model = Equipamento
    fields = ['cliente', 'tipo', 'marca', 'modelo', 'numero_serie', 'especificacoes']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-equipamentos')
    extra_context = {'titulo': 'Registar Novo Equipamento'}

class EquipamentoUpdate(UpdateView):
    model = Equipamento
    fields = ['cliente', 'tipo', 'marca', 'modelo', 'numero_serie', 'especificacoes']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-equipamentos')
    extra_context = {'titulo': 'Editar Equipamento'}

class EquipamentoDelete(DeleteView):
    model = Equipamento
    template_name = 'cadastros/form_excluir.html'
    success_url = reverse_lazy('listar-equipamentos')
    extra_context = {'titulo': 'Excluir Equipamento'}

class EquipamentoList(ListView):
    model = Equipamento
    template_name = 'cadastros/listar_equipamentos.html'
    extra_context = {'titulo': 'Lista de Equipamentos Registados'}

class EquipamentoDetail(DetailView):
    model = Equipamento
    template_name = 'cadastros/detalhar_equipamento.html'
    extra_context = {'titulo': 'Detalhes do Equipamento'}