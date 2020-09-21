from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users, admin_only


# exige usuário logado
@login_required(login_url='login')
#@admin_only # somente usuários do grupo 'admin' podem acessar a home | posso ampliar para outros grupos ['admin','staff']
#@allowed_users(allowed_roles=['admin','customer'])
def home(request):

    context = {}
    print('chamou a home')
    return render(request, 'rec/dashboard.html', context)
