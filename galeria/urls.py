from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'), # Quando o usuário acessar a raiz do site, ele será redirecionado para a função index do arquivo views.py
    path('imagem/<int:foto_id>', imagem, name='imagem'), # Quando o usuário acessar a rota /imagem, ele será redirecionado para a função imagem do arquivo views.py
    path('buscar', buscar, name='buscar') # Quando o usuário acessar a rota /buscar, ele será redirecionado para a função buscar do arquivo views.py
]