from django.contrib import admin
from .models import Linguagem, Paradigma, Biblioteca, Framework, BancoDeDados, Vaga, Aplicacao

@admin.register(Linguagem)
class LinguagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nivel_abstracao', 'modo_execucao')
    search_fields = ('titulo', 'descricao_breve')

@admin.register(Biblioteca)
class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'linguagem', 'last_updated')
    search_fields = ('titulo',)

@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'linguagem', 'last_updated')
    search_fields = ('titulo',)

@admin.register(BancoDeDados)
class BancoDeDadosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo')
    search_fields = ('titulo', 'descricao_breve')

@admin.register(Paradigma)
class ParadigmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'status', 'data_postagem') 
    list_filter = ('status', 'data_postagem')
    search_fields = ('titulo', 'empresa', 'descricao_vaga')

@admin.register(Aplicacao)
class AplicacaoAdmin(admin.ModelAdmin):
    list_display = ('vaga', 'etapa_atual', 'data_envio', 'curriculo_versao')
    list_filter = ('etapa_atual', 'data_envio')
    search_fields = ('vaga__titulo', 'vaga__empresa', 'curriculo_versao')