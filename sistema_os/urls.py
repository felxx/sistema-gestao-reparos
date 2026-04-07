from django.contrib import admin
from django.urls import path, include # Não esqueça de adicionar o include aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastros.urls')), # Conectando as URLs do nosso app
]