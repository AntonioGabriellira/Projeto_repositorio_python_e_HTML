from django.urls import path
from .views import listagem_produtos, detalhamento_produto, cadastrar_produto, excluir_produto, alterar_produto

urlpatterns = [
    path("", listagem_produtos),
    path("<int:id>", detalhamento_produto),
    path("cadastrar", cadastrar_produto),
    path("<int:id>/alterar_produto", alterar_produto),
    path("<int:id>/excluir", excluir_produto),
]
