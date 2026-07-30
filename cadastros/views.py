from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClienteForm, EquipamentoForm
from .models import Cliente, Equipamento, Peca
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class GroupRequiredMixin(UserPassesTestMixin):
    group_required = None

    def test_func(self):
        return self.request.user.groups.filter(name=self.group_required).exists()

class PaginaInicialView(TemplateView):
    template_name = "cadastros/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['ultimos_clientes'] = Cliente.objects.filter(
                usuario=self.request.user
            ).order_by('-id')[:5]
        return context

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nome', 'cpf_cnpj', 'telefone', 'endereco']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-clientes')
    extra_context = {'titulo': 'Cadastrar Novo Cliente'}

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-clientes')

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)

class ClienteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = 'Gerente'
    model = Cliente
    template_name = 'cadastros/form_excluir.html'
    success_url = reverse_lazy('listar-clientes')

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'cadastros/listar_clientes.html'
    extra_context = {'titulo': 'Lista de Clientes Cadastrados'}
    paginate_by = 10 

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user).order_by('-id')

class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'cadastros/detalhar_cliente.html'

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)

class EquipamentoCreate(LoginRequiredMixin, CreateView):
    model = Equipamento
    fields = ['cliente', 'tipo', 'marca', 'modelo', 'numero_serie', 'especificacoes']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-equipamentos')
    extra_context = {'titulo': 'Registar Novo Equipamento'}

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['cliente'].queryset = Cliente.objects.filter(usuario=self.request.user)
        return form

class EquipamentoUpdate(LoginRequiredMixin, UpdateView):
    model = Equipamento
    fields = ['cliente', 'tipo', 'marca', 'modelo', 'numero_serie', 'especificacoes']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-equipamentos')
    extra_context = {'titulo': 'Editar Equipamento'}

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['cliente'].queryset = Cliente.objects.filter(usuario=self.request.user)
        return form

class EquipamentoDelete(LoginRequiredMixin, DeleteView):
    model = Equipamento
    template_name = 'cadastros/form_excluir.html'
    success_url = reverse_lazy('listar-equipamentos')
    extra_context = {'titulo': 'Excluir Equipamento'}

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)

class EquipamentoList(LoginRequiredMixin, ListView):
    model = Equipamento
    template_name = 'cadastros/listar_equipamentos.html'
    extra_context = {'titulo': 'Lista de Equipamentos Registados'}
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(
            usuario=self.request.user
        ).select_related('cliente').order_by('-id')

class EquipamentoDetail(LoginRequiredMixin, DetailView):
    model = Equipamento
    template_name = 'cadastros/detalhar_equipamento.html'
    extra_context = {'titulo': 'Detalhes do Equipamento'}

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)


class PecaCreate(LoginRequiredMixin, CreateView):
    model = Peca
    fields = ['nome', 'quantidade_estoque', 'valor_custo', 'valor_venda']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-pecas')
    extra_context = {'titulo': 'Registar Nova Peça'}

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PecaUpdate(LoginRequiredMixin, UpdateView):
    model = Peca
    fields = ['nome', 'quantidade_estoque', 'valor_custo', 'valor_venda']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-pecas')
    extra_context = {'titulo': 'Editar Peça'}

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)

class PecaDelete(LoginRequiredMixin, DeleteView):
    model = Peca
    template_name = 'cadastros/form_excluir.html'
    success_url = reverse_lazy('listar-pecas')
    extra_context = {'titulo': 'Excluir Peça'}

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)

class PecaList(LoginRequiredMixin, ListView):
    model = Peca
    template_name = 'cadastros/listar_pecas.html'
    extra_context = {'titulo': 'Estoque de Peças'}
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user).order_by('-id')

class PecaDetail(LoginRequiredMixin, DetailView):
    model = Peca
    template_name = 'cadastros/detalhar_peca.html'
    extra_context = {'titulo': 'Detalhes da Peça'}

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)