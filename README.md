# Sistema de Gerenciamento de Clientes


Sistema de Gerenciamento com duas entidades relacionadas (Produto, Cliente) possui todas as funcionalidades para gerenciar clientes/produtos (Listar, Adicionar, Atualizar e Deletar).

Utilizei Django para a implementação do back-end e Bootstrap para o front-end.


### Para rodar este projeto em sua máquina:
Instalar dependências
```
pip install -r requirements.txt
```
ou
```
pip3 install -r requirements.txt
```
Criar tabelas
```
python manage.py migrate
```
Criar um usuário
```
python manage.py createsuperuser
```
Rodar a aplicação
```
python manage.py runserver
```
