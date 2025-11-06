from django.urls import path
from .views import CriarProduto, ListarProduto, EditarProduto, DeletarProduto , IndexView

app_name = 'gerenciar_produtos'

urlpatterns = [
    path('', IndexView.as_view(), name='index'), 
    path('criar', CriarProduto.as_view(), name='criar_produto'),
    path('listar', ListarProduto.as_view(), name='listar_produto'),
    path('editar/<int:produto_id>/', EditarProduto.as_view(), name='editar_produto'),
    path('deletar/<int:produto_id>/',DeletarProduto.as_view(), name='deletar_produto'),
]