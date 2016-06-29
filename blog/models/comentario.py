from django.db import models
from django.utils import timezone
from blog.models.post import Post


class Comentario(models.Model):
    post = models.ForeignKey('blog.models.post.Post', related_name='comentarios')
    autor = models.EmailField()
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    comentario_aprovado = models.BooleanField(default=False)

    def aprovar(self):
        self.comentario_aprovado = True
        self.save()

    def __str__(self):
        return self.texto
