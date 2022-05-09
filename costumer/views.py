from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from costumer.models import Cliente, Produto
from .forms import ClienteForm, ProdutoForm
from django.urls import reverse, reverse_lazy


class ClienteListView(ListView):
    model = Cliente
    paginate_by = 5
    template_name = 'clientes_lista.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


class ProdutoListView(ListView):
    model = Produto
    paginate_by = 5
    template_name = 'produtos_lista.html'
    context_object_name = 'produtos'


class DetalhesClienteView(DetailView):
    model = Cliente
    template_name = 'cliente_detalhe.html'
    context_object_name = 'clientes'


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
        return reverse('costumer:clientes')


class AdicionarProdutoView(CreateView):
    model = Produto
    template_name = 'adicionar_produto.html'
    form_class = ProdutoForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('costumer:produtos')


class AtualizarClienteView(UpdateView):
    model = Cliente
    template_name = 'atualizar_cliente.html'
    form_class = ClienteForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('costumer:clientes')


class AtualizarProdutoView(UpdateView):
    model = Produto
    template_name = 'atualizar_produto.html'
    form_class = ProdutoForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('costumer:produtos')


class DeletarClienteView(DeleteView):
    model = Cliente
    template_name = 'deletar_cliente.html'
    context_object_name = 'clientes'

    def get_success_url(self):
        return reverse('costumer:clientes')


class DeletarProdutoView(DeleteView):
    model = Produto
    template_name = 'deletar_produto.html'
    context_object_name = 'produtos'

    def get_success_url(self):
        return reverse('costumer:produtos')