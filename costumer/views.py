from django.views.generic import ListView, DetailView
from costumer.models import Cliente, Produto


class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes_lista.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


class DetalhesView(DetailView):
    model = Cliente
    template_name = 'cliente_detalhe.html'
    context_object_name = 'clientes'


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos_lista.html'
    context_object_name = 'produtos'


class DetalhesProdutoView(DetailView):
    model = Produto
    template_name = 'produto_detalhe.html'
    context_object_name = 'produtos'


