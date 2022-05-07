from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    registro_cadastro = models.DateTimeField(auto_now_add=True)     # registro do momento em que foi cadastrado
    registro_atualizacao = models.DateTimeField(auto_now=True)      # registro do momento em que foi atualizado

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "produto"


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    data_nascimento = models.DateField()
    ddd = models.CharField(max_length=3)
    telefone = models.CharField(max_length=10)
    produtos_cadastrados = models.ManyToManyField(Produto, default="Não contratou nenhum serviço")
    registro_cadastro = models.DateTimeField(auto_now_add=True)
    registro_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)   # em caso de cancelamento de serviço se tornará inativo

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    class Meta:
        db_table = "cliente"