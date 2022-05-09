from django.urls import path
from costumer.views import ClienteListView, DetalhesClienteView, ProdutoListView, DetalhesProdutoView, \
    AdicionarClienteView, \
    AtualizarClienteView, DeletarClienteView, AdicionarProdutoView, AtualizarProdutoView, DeletarProdutoView

app_name = 'costumer'
urlpatterns = [
    path('listagem/cliente/', ClienteListView.as_view(), name='clientes'),
    path('listagem/cliente/<int:pk>/', DetalhesClienteView.as_view(), name='cliente_detalhe'),
    path('listagem/produto/', ProdutoListView.as_view(), name='produtos'),
    path('listagem/produto/<int:pk>/', DetalhesProdutoView.as_view(), name='produto_detalhe'),
    path('adicionar/cliente', AdicionarClienteView.as_view(), name='adicionar_cliente'),
    path('atualizar/cliente/<int:pk>/', AtualizarClienteView.as_view(), name='atualizar_cliente'),
    path('deletar/cliente/<int:pk>/', DeletarClienteView.as_view(), name='deletar_cliente'),
    path('adicionar/produto/', AdicionarProdutoView.as_view(), name='adicionar_produto'),
    path('atualizar/produto/<int:pk>', AtualizarProdutoView.as_view(), name='atualizar_produto'),
    path('deletar/produto/<int:pk>', DeletarProdutoView.as_view(), name='deletar_produto')

]