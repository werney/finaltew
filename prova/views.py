from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def index(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})
