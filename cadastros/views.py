from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClienteForm, EquipamentoForm
from .models import Cliente, Equipamento
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PaginaInicialView(TemplateView):
    template_name = "cadastros/index.html"

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-clientes')

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

class ClienteDetail(DetailView):
    model = Cliente
    template_name = 'cadastros/detalhar_cliente.html'

class EquipamentoCreate(CreateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')