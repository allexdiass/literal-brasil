from django.shortcuts import render
from .models import Noticia
from django.utils import timezone

# Create your views here.


def main(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'jornal/main.html', {'noticias': noticias})
