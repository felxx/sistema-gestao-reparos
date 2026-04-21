from django.urls import path
from .views import PaginaInicialView, ClienteCreate, EquipamentoCreate

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),
    path('cadastrar/cliente/', ClienteCreate.as_view(), name="cadastrar-cliente"),
    path('cadastrar/equipamento/', EquipamentoCreate.as_view(), name="cadastrar-equipamento"),
]