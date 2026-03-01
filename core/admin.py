from django.contrib import admin
from .models import Linguagem, Paradigma, Biblioteca, Framework

# Registro simples para o Paradigma (só precisamos do nome)
@admin.register(Paradigma)
class ParadigmaAdmin(admin.ModelAdmin):
    search_fields = ['nome']

# Registro avançado para a Linguagem
@admin.register(Linguagem)
class LinguagemAdmin(admin.ModelAdmin):
    # O que aparece na lista principal de linguagens
    list_display = ('title', 'nivel_abstracao', 'modo_execucao', 'tipagem')
    
    # Filtros laterais para você navegar rápido (Igual aos labels do Capacities!)
    list_filter = ('nivel_abstracao', 'modo_execucao', 'tipagem', 'paradigmas')
    
    # Campo de busca por título ou descrição
    search_fields = ['title', 'description']
    
    # Organização dos campos dentro do formulário de edição
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description')
        }),
        ('Classificação Técnica', {
            'fields': ('nivel_abstracao', 'modo_execucao', 'tipagem', 'paradigmas')
        }),
        ('Conteúdo Rico', {
            'fields': ('conteudo',),
        }),
    )
@admin.register(Biblioteca)
class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('title', 'linguagem', 'last_updated')
    list_filter = ('linguagem',) # Permite filtrar bibliotecas por linguagem na lateral
    search_fields = ('title', 'description')

@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'linguagem', 'last_updated')
    list_filter = ('linguagem',)
    search_fields = ('title', 'description')