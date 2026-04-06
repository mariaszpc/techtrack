from django.contrib import admin
from django.urls import path
from core.views import LinguagemListView, LinguagemDetailView 

urlpatterns = [
    # Rota do Painel Administrativo
    path("admin/", admin.site.urls),
    
    # Rotas da Wiki
    path('wiki/', LinguagemListView.as_view(), name='linguagem_list'),
    path('wiki/<int:pk>/', LinguagemDetailView.as_view(), name='linguagem_detail'),
]