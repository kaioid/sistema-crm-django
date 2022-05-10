from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from costumer.models import Cliente, Produto
from .forms import ClienteForm, ProdutoForm
from django.urls import reverse, reverse_lazy


class ClienteListView(ListView):
    model = Cliente
    paginate_by = 5
    template_name = 'clientes_lista.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(Q(nome__icontains=name) | Q(sobrenome__icontains=name))
        else:
            object_list = self.model.objects.all()
        return object_list


class ProdutoListView(ListView):
    model = Produto
    paginate_by = 5
    template_name = 'produtos_lista.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(nome__icontains=name)
        else:
            object_list = self.model.objects.all()
        return object_list


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
    fields = [
        "nome",
        "sobrenome",
        "email",
        "data_nascimento",
        "ddd",
        "telefone",
        "produtos_cadastrados"
    ]
    context_object_name = 'clientes'

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

    context_object_name = 'produtos'


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