from django.shortcuts import render

def listagem_produtos(request):
    context = {
        "produtos" : [
        {"nome": "uva", "preco" : 2}, 
        {"nome": "melancia", "preco" : 4},
        {"nome": "banana", "preco" : 3},
        {"nome": "ggg"}
        ]
    }
    return render(request, "templates/listagem_produtos.html", context)