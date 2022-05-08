from django.views.generic import ListView, DetailView
from costumer.models import Cliente


class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes_lista.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


class DetalhesView(DetailView):
    model = Cliente
    template_name = 'vista_detalhada.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'

