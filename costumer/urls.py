from django.urls import path
from costumer.views import ClienteListView, DetalhesView, ProdutoListView, DetalhesProdutoView, AdicionarClienteView

app_name = 'costumer'
urlpatterns = [
    path('listagem/cliente/', ClienteListView.as_view(), name='clientes'),
    path('listagem/cliente/<pk>/', DetalhesView.as_view(), name='cliente_detalhe'),
    path('listagem/produto/', ProdutoListView.as_view(), name='produtos'),
    path('listagem/produto/<pk>/', DetalhesProdutoView.as_view(), name='produto_detalhe'),
    path('adicionar/cliente', AdicionarClienteView.as_view(), name='adicionar_cliente')
]