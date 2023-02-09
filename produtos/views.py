from django.shortcuts import render

def listagem_produtos(request):
    produtos_dos_vendedores= [{
        "vendedor" : {"nome": "pedro"},
        "produtos" : [
        {"nome": "uva", "preco" : 2}, 
        {"nome": "melancia", "preco" : 4},
        {"nome": "banana", "preco" : 3},
        ]
    },
    {
        "vendedor" : {"nome": "jão"},
        "produtos" : [
        {"nome": "mandioca", "preco" : 3}, 
        {"nome": "melancia", "preco" : 5},
        {"nome": "peixe", "preco" : 10},
        ]
    },
    ]
    context = {"produtos_dos_vendedores": produtos_dos_vendedores}
    return render(request, "templates/listagem_produtos.html", context)