from django.urls import path
from projeto.views import tabela

urlpatterns = [
    path('', tabela, name='tabela'),
]