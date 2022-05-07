from django.contrib import admin
from .models import Cliente, Produto

# Register your models here.


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "sobrenome"]