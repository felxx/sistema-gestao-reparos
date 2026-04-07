from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20, verbose_name="CPF/CNPJ")
    telefone = models.CharField(max_length=20)
    endereco = models.TextField(verbose_name="Endereço")

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=50, help_text="Ex: Desktop, Notebook, Impressora")
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=100, verbose_name="Número de Série")
    especificacoes = models.TextField(verbose_name="Especificações")

    def __str__(self):
        return f"{self.tipo} {self.marca} {self.modelo}"

class ServicoTabelado(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição do Serviço")
    valor_base = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Base")

    def __str__(self):
        return self.descricao

class Peca(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.IntegerField(verbose_name="Quantidade em Estoque")
    valor_custo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor de Custo")
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor de Venda")

    def __str__(self):
        return self.nome

class OrdemDeServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)
    data_entrada = models.DateTimeField(auto_now_add=True, verbose_name="Data de Entrada")
    data_previsao = models.DateTimeField(verbose_name="Data de Previsão", null=True, blank=True)
    defeito_relatado = models.TextField(verbose_name="Defeito Relatado")
    laudo_tecnico = models.TextField(verbose_name="Laudo Técnico", null=True, blank=True)
    status = models.CharField(max_length=50, default="Aguardando Avaliação")
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Valor Total")

    def __str__(self):
        return f"OS #{self.pk} - {self.cliente.nome}"

class ItemOS(models.Model):
    ordem_de_servico = models.ForeignKey(OrdemDeServico, on_delete=models.CASCADE)
    servico = models.ForeignKey(ServicoTabelado, on_delete=models.PROTECT, null=True, blank=True)
    peca = models.ForeignKey(Peca, on_delete=models.PROTECT, null=True, blank=True)
    quantidade = models.IntegerField(default=1)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Unitário")

    def __str__(self):
        return f"Item da OS #{self.ordem_de_servico.pk}"