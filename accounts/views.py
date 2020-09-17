from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

#pdf
from django.template.loader import render_to_string
from django.db.models import Sum
from django.conf.urls.static import static

# Create your views here.
from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only

#@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Conta criada para ' + username)

            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

#@unauthenticated_user
def loginPage(request):

    # pega os valores durante o login | de forma segura através do csrf_token
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        # autenticando o usuário
        user = authenticate(request, username=username, password=password)
        # se realmente autenticou
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Usuário ou Senha incorreta')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# exige usuário logado
@login_required(login_url='login')
#@admin_only # somente usuários do grupo 'admin' podem acessar a home | posso ampliar para outros grupos ['admin','staff']
#@allowed_users(allowed_roles=['admin','customer'])
def home(request):

    #return render(request, 'rg1/dashboard.html', context)
    return HttpResponse('Home Page')


