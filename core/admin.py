from django.contrib import admin
from .models import Linguagem, Paradigma, Biblioteca, Framework, Vaga, Aplicacao, BancoDeDados

# Registro simples para o Paradigma (só precisa do nome)
@admin.register(Paradigma)
class ParadigmaAdmin(admin.ModelAdmin):
    search_fields = ['nome']

@admin.register(Linguagem)
class LinguagemAdmin(admin.ModelAdmin):
    list_display = ('title', 'nivel_abstracao', 'modo_execucao', 'tipagem')
    
    list_filter = ('nivel_abstracao', 'modo_execucao', 'tipagem', 'paradigmas')
    
    search_fields = ['title', 'description']
    
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
    list_filter = ('linguagem',)
    search_fields = ('title', 'description')

@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'linguagem', 'last_updated')
    list_filter = ('linguagem',)
    search_fields = ('title', 'description')

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'status', 'data_postagem')
    list_filter = ('status', 'requisitos_linguagens')
    search_fields = ('titulo', 'empresa', 'descricao_vaga')

@admin.register(Aplicacao)
class AplicacaoAdmin(admin.ModelAdmin):
    list_display = ('vaga', 'etapa_atual', 'data_envio')
    list_filter = ('etapa_atual', 'data_envio')
    search_fields = ('vaga__titulo', 'vaga__empresa')

@admin.register(BancoDeDados)
class BancoDeDadosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('nome', 'description')