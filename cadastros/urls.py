from django.urls import path
from .views import PaginaInicialView, ClienteCreate, EquipamentoCreate, ClienteUpdate, ClienteDelete, ClienteList, ClienteDetail

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),
    path('cadastrar/cliente/', ClienteCreate.as_view(), name="cadastrar-cliente"),
    path('listar/clientes/', ClienteList.as_view(), name="listar-clientes"),
    path('atualizar/cliente/<int:pk>/', ClienteUpdate.as_view(), name="atualizar-cliente"),
    path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name="excluir-cliente"),
    path('detalhar/cliente/<int:pk>/', ClienteDetail.as_view(), name="detalhar-cliente"),
    path('cadastrar/equipamento/', EquipamentoCreate.as_view(), name="cadastrar-equipamento"),
]