from django.views.generic import ListView, DetailView, CreateView
from costumer.models import Cliente, Produto
from .forms import ClienteForm
from django.urls import reverse


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


class AdicionarClienteView(CreateView):
    model = Cliente
    template_name = 'adicionar_cliente.html'
    form_class = ClienteForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return ()



