from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Funcionario


@login_required
def home(request):
    funcionario = Funcionario.objects.all()
    data = {
        'funcionario' : funcionario,
        'usuario': request.environ
        
    }
    return render(request, 'home.html',data)
