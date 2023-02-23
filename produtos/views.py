from django.shortcuts import render, get_object_or_404
from produtos.models import Produto, Anunciante, TIPO_PRODUTO, TIPO_SERVICO
from produtos.forms import ProdutoModelForm, ServicoModelForm
from django.http import HttpResponseRedirect


def listagem_produtos(request):
    anunciantes = Anunciante.objects.all()
    produtos_dos_vendedores = []
    for anunciante in anunciantes:
        produtos_do_vendedor  = anunciante.produto_set.filter(tipo=TIPO_PRODUTO, excluido = False)
        if produtos_do_vendedor:
            produtos_dos_vendedores.append({
                "vendedor": {"nome" : anunciante.nome},
                "produtos": produtos_do_vendedor,
            })
    context = {"produtos_dos_vendedores": produtos_dos_vendedores}
    return render(request, "templates/listagem_produtos.html", context)

def detalhamento_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    context = {
        "produto": produto
    }
    return render(request, "templates/detalhamento_produto.html", context)

def cadastrar_produto(request):
    form = ProdutoModelForm()
    context = {
        "form" : form
    }
    if request.method == "GET":
        print("É um GET")
    if request.method == "POST":
        print("É um POST")
        form = ProdutoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/produtos/")
    return render(request, "templates/cadastrar_produtos.html", context)

def alterar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == "POST":
        form = ProdutoModelForm(request.POST)
        if form.is_valid():
            produto.nome = form.cleaned_data["nome"]
            produto.estoque = form.cleaned_data["estoque"]
            produto.preco = form.cleaned_data["preco"]
            produto.save()
            return HttpResponseRedirect(f"/produtos/{produto.id}")
    form = ProdutoModelForm(instance=produto)
    context = {
        "form": form
    }
    return render(request, "templates/alterar_produto.html", context)

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == "POST":
        produto.excluido = True
        produto.save()
        return HttpResponseRedirect("/produtos/")
    context = {
        "produto": produto
    }
    return render(request, "templates/excluir_produto.html", context)

def listagem_servicos(request):
    anunciantes = Anunciante.objects.all()
    servicos_dos_vendedores = []
    for anunciante in anunciantes:
        servicos_vendedores  = anunciante.produto_set.filter(tipo=TIPO_SERVICO, excluido = False)
        if servicos_vendedores:
            servicos_dos_vendedores.append({
                "vendedor": {"nome" : anunciante.nome},
                "servicos" : servicos_vendedores,
            })
    context = {"servicos_dos_vendedores": servicos_dos_vendedores }
    return render(request, "templates/listagem_servicos.html", context)

def cadastro_servico(request):
    if request.method == "POST":
        form = ServicoModelForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.tipo = TIPO_SERVICO
            produto.save()
            return HttpResponseRedirect("/servicos/")

    form = ServicoModelForm()
    context = {
        "form" : form
    }
    
    return render(request, "templates/cadastrar_servico.html", context)