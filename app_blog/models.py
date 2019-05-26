from django.db import models
from django.contrib.auth.models import User


class CategoriaPosts(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return self.nome


class Posts(models.Model):
    autor = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL, verbose_name='Autor')
    categoria = models.ForeignKey(CategoriaPosts, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Categoria')
    titulo = models.CharField('Nome', max_length=128)
    descricao = models.CharField('Descriçaõ', max_length=256)
    conteudo = models.TextField('Conteúdo')
    imagem = models.ImageField(upload_to="imagem_posts")
    publicado = models.BooleanField('Publicado', default=True)
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class MensagemDeContato(models.Model):
    nome = models.CharField(max_length=128)
    email = models.EmailField('E-mail', blank=True, null=True)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome