from django.urls import path
from projeto.views import tabela
from projeto.views.endpoint.lista_Json import lista

urlpatterns = [
    path('', tabela, name='tabela'),
    path('lista/produtos/',lista, name="lista_produto"),
]