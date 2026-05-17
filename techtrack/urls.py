from django.contrib import admin
from django.urls import path
from core.views import LinguagemListView, LinguagemDetailView, DashboardView, LinguagemCreateView, VagaListView, VagaDetailView

urlpatterns = [
    # Rota do Painel Administrativo
    path("admin/", admin.site.urls),
    
    # Rota inicial vazia apontando para o Dashboard:
    path('', DashboardView.as_view(), name='dashboard'),
    
# Rotas da Wiki
    path('wiki/', LinguagemListView.as_view(), name='linguagem_list'),
    # A rota de criação deve vir ANTES da rota de detalhe
    path('wiki/nova/', LinguagemCreateView.as_view(), name='linguagem_create'),
    path('wiki/<int:pk>/', LinguagemDetailView.as_view(), name='linguagem_detail'),
    # Rotas de Vagas 
    path('vagas/', VagaListView.as_view(), name='vaga_list'),
    path('vagas/<int:pk>/', VagaDetailView.as_view(), name='vaga_detail'),
]