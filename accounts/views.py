from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Ao ENTRAR pelo caminho 'account/login ou account/'
# o usuário irá acessar a página de login
# render-mostre na tela, request - tipo(requisição), 'accounts/login.html' é dominio da pasta
# É O CAMINHO ATÉ OS TEMPLATES HTML

def login(request):
    print(request.POST)
    if request.method != 'POST':
    #TESTE - MÉTODO DA REQUISIÇÃO
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou Senha INVÁLIDOS')
        return render(request, 'accounts/login.html')
    else:
        #Algoritmo de login
        auth.login(request, user)
        messages.success(request, 'Login REALIZADO')
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('dashboard')

def cadastro(request):
    print(request.POST)
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    #Recolhendo dados do usuário
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha1 = request.POST.get('senha1')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha1 or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio...')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email Inválido')
        return render(request, 'accounts/cadastro.html')

    if len(senha1) < 6:
        messages.error(request, 'Senha Curta')
        return render(request, 'accounts/cadastro.html')

    if len(senha2) < 6:
        messages.error(request, 'Senha Curta')
        return render(request, 'accounts/cadastro.html')

    if senha1 != senha2:
        messages.error(request, 'Senhas Distintas')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já está sendo usado')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já está sendo usado')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Registrado com SUCESSO. Faça Login.')
    user = User.objects.create_user(username=usuario, first_name=nome,
                                    last_name=sobrenome, password=senha1,
                                    email=email)
    user.save()
    return redirect('login')
from .models import  FormContato

@login_required(redirect_field_name='login')
#Caso alguem tente entrar na dashboard sem estar logado, ele é redirecionado para a página de 'login'
def dashboard(request):

    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao ENVIAR')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    return redirect('dashboard')
