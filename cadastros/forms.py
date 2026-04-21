from django import forms

from .models import Cliente, Equipamento


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "cpf_cnpj", "telefone", "endereco"]


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ["cliente", "tipo", "marca", "modelo", "numero_serie", "especificacoes"]