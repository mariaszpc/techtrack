from django.db import models
from mdeditor.fields import MDTextField

class Paradigma(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    title = models.CharField(max_length=100)

    # NÍVEL DE ABSTRAÇÃO
    ABSTRACAO_CHOICES = [
        ('Baixo', 'Baixo'), #(valor_no_banco, rótulo_na_tela)
        ('Médio', 'Médio'),
        ('Alto', 'Alto'),
    ]
    nivel_abstracao = models.CharField(max_length=20, choices=ABSTRACAO_CHOICES)

    # MODO DE EXECUÇÃO
    EXECUCAO_CHOICES = [
        ('Compilado', 'Compilado'),
        ('Interpretado', 'Interpretado'),
        ('Híbrida/JIT', 'Híbrida/JIT'),
    ]
    modo_execucao = models.CharField(max_length=20, choices=EXECUCAO_CHOICES)

    # TIPAGEM
    TIPAGEM_CHOICES = [
        ('Estática', 'Estática'),
        ('Dinâmica', 'Dinâmica'),
        ('Forte', 'Forte'),
        ('Fraca', 'Fraca'),
        ('untyped', 'untyped'),
    ]
    tipagem = models.CharField(max_length=20, choices=TIPAGEM_CHOICES)

    # PARADIGMAS (Vários para uma linguagem)
    paradigmas = models.ManyToManyField(Paradigma, blank=True)

    # Conteúdo Rico
    description = models.TextField()
    conteudo = MDTextField()

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "Linguagens"

class Biblioteca(models.Model):
    title = models.CharField(max_length=100)
    aliases = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    
    # RELACIONAMENTO: Cada biblioteca pertence a uma Linguagem
    # Se a linguagem for deletada, as bibliotecas dela também são (on_delete=models.CASCADE)
    linguagem = models.ForeignKey(Linguagem, on_delete=models.CASCADE, related_name='bibliotecas')
    
    # Links e Documentação
    documentacao = models.URLField(max_length=500, blank=True, help_text="Link para a documentação oficial")
    link_oficial = models.URLField(max_length=500, blank=True, help_text="Link para o site ou repositório")
    
    # Datas automáticas
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    # Conteúdo Rico (Markdown)
    content = MDTextField()

    def __str__(self):
        return f"{self.title} ({self.linguagem.title})"

    class Meta:
        verbose_name_plural = "Bibliotecas"

class Framework(models.Model):
    title = models.CharField(max_length=100)
    aliases = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    
    # RELACIONAMENTO: Um framework pertence a uma linguagem (Ex: Django -> Python)
    linguagem = models.ForeignKey(Linguagem, on_delete=models.CASCADE, related_name='frameworks')
    
    # Links e Documentação
    documentacao = models.URLField(max_length=500, blank=True)
    link_oficial = models.URLField(max_length=500, blank=True)
    
    # Datas automáticas
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    # Conteúdo Rico (Markdown)
    content = MDTextField()

    def __str__(self):
        return f"{self.title} ({self.linguagem.title})"

    class Meta:
        verbose_name_plural = "Frameworks"

class Vaga(models.Model):
    titulo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=100)
    link_anuncio = models.URLField(max_length=500)
    data_postagem = models.DateField(blank=True, null=True)
    
    # Status do seu Processo (Sua gestão de carreira)
    STATUS_CHOICES = [
        ('Interesse', 'Apenas Interesse'),
        ('Aplicado', 'Currículo Enviado'),
        ('Entrevista', 'Em Fase de Entrevistas'),
        ('Teste', 'Teste Técnico em Andamento'),
        ('Negado', 'Não Selecionada'),
        ('Aprovado', 'Contratada! 🎉'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Interesse')

    # RELAÇÕES
    # Usamos ManyToMany porque uma vaga pede várias techs, e uma tech aparece em várias vagas.
    requisitos_linguagens = models.ManyToManyField('Linguagem', blank=True)
    requisitos_frameworks = models.ManyToManyField('Framework', blank=True)
    requisitos_bibliotecas = models.ManyToManyField('Biblioteca', blank=True)
    # requisitos_bancos = models.ManyToManyField('BancoDeDados', blank=True) # Criaremos este depois

    # Conteúdo Rico
    descricao_vaga = MDTextField(help_text="Cole aqui a descrição completa para consulta posterior")
    anotacoes_pessoais = MDTextField(help_text="O que você estudou ou preparou para essa vaga específica?")

    def __str__(self):
        return f"{self.titulo} - {self.empresa}"

    class Meta:
        verbose_name_plural = "Vagas"

class Aplicacao(models.Model):
    # RELACIONAMENTO: Uma aplicação pertence a uma Vaga
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name='aplicacoes')
    
    data_envio = models.DateField(auto_now_add=True)
    
    # Etapas do funil de recrutamento
    ETAPA_CHOICES = [
        ('CV', 'Envio de Currículo'),
        ('Fit', 'Fit Cultural / RH'),
        ('Tecnico', 'Teste Técnico'),
        ('Gestor', 'Entrevista com Gestor'),
        ('Proposta', 'Proposta Recebida'),
    ]
    etapa_atual = models.CharField(max_length=20, choices=ETAPA_CHOICES, default='CV')
    
    # Detalhes da sua participação
    curriculo_versao = models.CharField(max_length=100, blank=True, help_text="Ex: CV_DataScience_v2.pdf")
    portfolio_link = models.URLField(blank=True, help_text="Link para o projeto enviado")
    
    # Conteúdo Rico para histórico
    feedback_recebido = MDTextField(blank=True, help_text="O que a empresa disse sobre você?")
    anotacoes_pos_entrevista = MDTextField(blank=True, help_text="O que você achou da empresa?")

    def __str__(self):
        return f"Aplicação: {self.vaga.titulo} ({self.get_etapa_atual_display()})"

    class Meta:
        verbose_name_plural = "Aplicações"