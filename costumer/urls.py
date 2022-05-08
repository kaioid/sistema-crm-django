from django.urls import path
from costumer.views import ClienteListView, DetalhesView

app_name = 'costumer'
urlpatterns = [
    path('lista/', ClienteListView.as_view(), name='clientes'),
    path('lista/<pk>/', DetalhesView.as_view(), name='detalhes'),
]