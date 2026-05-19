from django.contrib import admin
from django.urls import path
from core.views import (
    LinguagemListView, LinguagemDetailView, DashboardView, 
    LinguagemCreateView, VagaListView, VagaDetailView, VagaCreateView,
    AplicacaoListView, AplicacaoDetailView, AplicacaoCreateView
)

urlpatterns = [
    # Rota do Painel Administrativo
    path("admin/", admin.site.urls),
    
    # Rota inicial vazia levando para o Dashboard:
    path('', DashboardView.as_view(), name='dashboard'),
    
    # Rotas da Wiki
    path('wiki/', LinguagemListView.as_view(), name='linguagem_list'),
    path('wiki/nova/', LinguagemCreateView.as_view(), name='linguagem_create'),
    path('wiki/<int:pk>/', LinguagemDetailView.as_view(), name='linguagem_detail'),

    # Rotas de Vagas 
    path('vagas/', VagaListView.as_view(), name='vaga_list'),
    path('vagas/nova/', VagaCreateView.as_view(), name='vaga_create'),
    path('vagas/<int:pk>/', VagaDetailView.as_view(), name='vaga_detail'),

    # Rotas de Aplicações
    path('aplicacoes/', AplicacaoListView.as_view(), name='aplicacao_list'),
    path('aplicacoes/nova/', AplicacaoCreateView.as_view(), name='aplicacao_create'),
    path('aplicacoes/<int:pk>/', AplicacaoDetailView.as_view(), name='aplicacao_detail')
]