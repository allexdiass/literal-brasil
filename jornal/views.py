from django.shortcuts import render
from .models import Noticia
from django.utils import timezone
from django.http import HttpRequest

# Create your views here.


def main(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    client_address = request.META['REMOTE_ADDR']
    return render(request, 'jornal/main.html', {'noticias': noticias})
