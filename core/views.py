from django.views.generic import ListView, DetailView
from .models import Linguagem

# Views da Wiki
class LinguagemListView(ListView):
    model = Linguagem
    template_name = 'core/linguagem_list.html'
    context_object_name = 'linguagens'

class LinguagemDetailView(DetailView):
    model = Linguagem
    template_name = 'core/linguagem_detail.html'
    context_object_name = 'linguagem'

from django.views.generic import ListView, DetailView, TemplateView
from .models import Linguagem, Vaga, Aplicacao

# Dashboard
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

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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