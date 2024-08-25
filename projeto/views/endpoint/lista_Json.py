from django.http import JsonResponse

from projeto.models import Categoria, Produto
from django.views import View


def lista(request):
        
    produtos = Produto.objects.all().values(
        'nome',
        'descricao',
        'preco',
        'ativo',
        'categoria',
        'usuario'
        ) # retorna queryset de dicionários
    lista_produto = list(produtos) # converte o queryset em lista
    print(lista_produto)

    return JsonResponse(lista_produto, safe=False)
