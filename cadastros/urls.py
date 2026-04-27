from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),

    path('cadastrar/cliente/', ClienteCreate.as_view(), name="cadastrar-cliente"),
    path('listar/clientes/', ClienteList.as_view(), name="listar-clientes"),
    path('atualizar/cliente/<int:pk>/', ClienteUpdate.as_view(), name="atualizar-cliente"),
    path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name="excluir-cliente"),
    path('detalhar/cliente/<int:pk>/', ClienteDetail.as_view(), name="detalhar-cliente"),

    path('cadastrar/equipamento/', EquipamentoCreate.as_view(), name="cadastrar-equipamento"),
    path('listar/equipamentos/', EquipamentoList.as_view(), name="listar-equipamentos"),
    path('atualizar/equipamento/<int:pk>/', EquipamentoUpdate.as_view(), name="atualizar-equipamento"),
    path('excluir/equipamento/<int:pk>/', EquipamentoDelete.as_view(), name="excluir-equipamento"),
    path('detalhar/equipamento/<int:pk>/', EquipamentoDetail.as_view(), name="detalhar-equipamento"),

    path('cadastrar/peca/', PecaCreate.as_view(), name="cadastrar-peca"),
    path('listar/pecas/', PecaList.as_view(), name="listar-pecas"),
    path('atualizar/peca/<int:pk>/', PecaUpdate.as_view(), name="atualizar-peca"),
    path('excluir/peca/<int:pk>/', PecaDelete.as_view(), name="excluir-peca"),
    path('detalhar/peca/<int:pk>/', PecaDetail.as_view(), name="detalhar-peca"),
]