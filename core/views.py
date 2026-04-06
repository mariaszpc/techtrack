from django.views.generic import ListView, DetailView
from .models import Linguagem

class LinguagemListView(ListView):
    model = Linguagem
    template_name = 'core/linguagem_list.html'
    context_object_name = 'linguagens'

class LinguagemDetailView(DetailView):
    model = Linguagem
    template_name = 'core/linguagem_detail.html'
    context_object_name = 'linguagem'
