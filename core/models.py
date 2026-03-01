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