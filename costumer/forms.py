from django import forms
from .models import Cliente, Produto


class DateInput(forms.DateInput):
    input_type = "date"


class ClienteForm(forms.ModelForm):

    nome = forms.CharField(label="Nome")
    sobrenome = forms.CharField(label="Sobrenome")
    email = forms.EmailField(label="E-mail")
    data_nascimento = forms.DateField(label="Data de nascimento", widget=DateInput)
    ddd = forms.RegexField(label="DDD", regex=r"^\+?1?[0-9]{2}", error_messages={"invalid": "Número de DDD inválido"})
    telefone = forms.RegexField(label="Telefone", regex=r"^\+?1?[0-9]{9,15}", error_messages={"invalid": "Número de Telefone inválido"})
    produtos_cadastrados = forms.ModelMultipleChoiceField(queryset=Produto.objects.all(), required=False)

    class Meta:
        model = Cliente
        fields = [
            "nome",
            "sobrenome",
            "email",
            "data_nascimento",
            "ddd",
            "telefone",
            "produtos_cadastrados"
        ]


class ProdutoForm(forms.ModelForm):

    nome = forms.CharField(label="Nome do produto")
    descricao = forms.CharField(label="Descrição", widget=forms.Textarea)

    class Meta:
        model = Produto
        fields = [
            "nome",
            "descricao"
        ]
