from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# @login_required
def home(request):
    return render(request, 'core/index.html', )

@login_required
def acesso_nao_permitido(request):
    return render(request, 'core/acesso_nao_permitido.html', )