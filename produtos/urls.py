from django.urls import path
from .views import listagem_produtos, detalhamento_produto

urlpatterns = [
    path("", listagem_produtos),
    path("<int:id>", detalhamento_produto),
]
