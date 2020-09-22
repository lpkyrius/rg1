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
    print('chamou a home')
    context = {}
    return render(request, 'rec/dashboard.html', context)


@login_required(login_url='login')
def convenio_list(request):
    return render(request, "rec/convenios_list.html")


@login_required(login_url='login')
def convenio_form(request):
    print('chamou a convenio form')
    context = {}
    return render(request, "rec/convenios_form.html", context)



@login_required(login_url='login')
def convenio_delete(request):
    print('chamou a convenio list')
    context = {}
    return render(request, "rec/convenios_list.html", context)

