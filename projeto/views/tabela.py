from django.shortcuts import render

from projeto.models import Categoria, Produto

def tabela(request):
    
    context = {

    }
    return render(request, 'index.html', context=context)