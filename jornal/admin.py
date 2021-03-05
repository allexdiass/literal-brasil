from django.contrib import admin
from .models import Noticia
from .models import Imagem

# Register your models here.
admin.site.register(Noticia)
admin.site.register(Imagem)
