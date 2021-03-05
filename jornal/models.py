from django.db import models
from django.conf import settings
from django.db.models.deletion import SET_NULL
from django.utils import timezone


def noticia_directory_path(instance, filename):
    print(str(instance))
    return f'imagens/'


class Noticia(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    resumo = models.CharField(max_length=500)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)
    capa = models.ImageField(upload_to=noticia_directory_path, null=True)

    def publish(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class Imagem(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to=noticia_directory_path)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def publish(self):
        self.save()
