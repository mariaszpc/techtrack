from django import forms
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Linguagem, Vaga, Aplicacao

# ----------------------------
# DASHBOARD
# ----------------------------
class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pegando a quantidade de itens no banco de dados para mostrar nos Cards
        context['total_linguagens'] = Linguagem.objects.count()
        context['total_vagas'] = Vaga.objects.count()
        # Conta aplicações que não estejam com status "Negado" (etapa do funil)
        context['aplicacoes_ativas'] = Aplicacao.objects.exclude(etapa_atual='Proposta').count()
        return context

# ----------------------------
# WIKI DE TECNOLOGIAS
# ----------------------------
class LinguagemListView(ListView):
    model = Linguagem
    template_name = 'core/linguagem_list.html'
    context_object_name = 'linguagens'

class LinguagemDetailView(DetailView):
    model = Linguagem
    template_name = 'core/linguagem_detail.html'
    context_object_name = 'linguagem'

class LinguagemCreateView(CreateView):
    model = Linguagem
    template_name = 'core/linguagem_form.html'
    # Quais campos vão aparecer no formulário da tela:
    fields = [
        'titulo', 'aliases', 'descricao_breve', 'conteudo', 'referencias', 
        'link_oficial', 'link_documentacao', 'nivel_abstracao', 
        'modo_execucao', 'tipagem', 'paradigmas'
    ]
    # Para onde ir depois de salvar? Volta para a lista!
    success_url = reverse_lazy('linguagem_list')

# ----------------------------
# VAGAS (Gestão de Carreira)
# ----------------------------
class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = [
            'titulo', 'empresa', 'cidade', 'modelo_trabalho', 'nivel', 'codigo',
            'link_anuncio', 'data_postagem', 'status', 'requisitos_linguagens',
            'requisitos_frameworks', 'requisitos_bibliotecas', 'requisitos_bancos',
            'descricao_vaga', 'anotacoes_pessoais'
        ]
        widgets = {
            'requisitos_linguagens': forms.CheckboxSelectMultiple(),
            'requisitos_frameworks': forms.CheckboxSelectMultiple(),
            'requisitos_bibliotecas': forms.CheckboxSelectMultiple(),
            'requisitos_bancos': forms.CheckboxSelectMultiple(),
        }
        
class VagaListView(ListView):
    model = Vaga
    template_name = 'core/vaga_list.html'
    context_object_name = 'vagas'

class VagaDetailView(DetailView):
    model = Vaga
    template_name = 'core/vaga_detail.html'
    context_object_name = 'vaga'

class VagaCreateView(CreateView):
    model = Vaga
    template_name = 'core/vaga_form.html'
    form_class = VagaForm
    success_url = reverse_lazy('vaga_list')

# ----------------------------
# APLICAÇÕES
# ----------------------------
class AplicacaoListView(ListView):
    model = Aplicacao
    template_name = 'core/aplicacao_list.html'
    context_object_name = 'aplicacoes'

class AplicacaoDetailView(DetailView):
    model = Aplicacao
    template_name = 'core/aplicacao_detail.html'
    context_object_name = 'aplicacao'

class AplicacaoCreateView(CreateView):
    model = Aplicacao
    template_name = 'core/aplicacao_form.html'
    # Os campos que vão aparecer para o usuário preencher
    fields = [
        'vaga', 'etapa_atual', 'curriculo_versao', 
        'portfolio_link', 'feedback_recebido', 'anotacoes_pos_entrevista'
    ]
    success_url = reverse_lazy('aplicacao_list')