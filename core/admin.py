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