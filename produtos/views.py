from django.shortcuts import render, get_object_or_404
from produtos.models import Produto
from produtos.forms import ProdutoModelForm

def listagem_produtos(request):
    produtos = Produto.objects.all()
    produtos_dos_vendedores = Produto.objects.all()
    produtos_dos_vendedores = [{
        "vendedor" : {"nome" : "maik"},
        "produtos" : produtos
    }]
    context = {"produtos_dos_vendedores": produtos_dos_vendedores}
    return render(request, "templates/listagem_produtos.html", context)

def detalhamento_produto(request, id):
    produto = get_object_or_404(Produto, pk=1)
    context = {
        "produto": produto
    }
    return render(request, "templates/detalhamento_produto.html", context)

def cadastrar_produto(request):
    form = ProdutoModelForm()
    context = {
        "form" : form
    }
    return render(request, "templates/cadastrar_produtos.html", context)