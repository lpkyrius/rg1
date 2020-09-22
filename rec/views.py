from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required

from accounts.decorators import unauthenticated_user, allowed_users, admin_only

from .forms import ConvenioForm
from .models import Convenio

# exige usuário logado
#@login_required(login_url='login')
#@admin_only # somente usuários do grupo 'admin' podem acessar a home | posso ampliar para outros grupos ['admin','staff']
#@allowed_users(allowed_roles=['admin','customer'])
def home(request):
    print('chamou a home')
    context = {}
    return render(request, 'rec/dashboard.html', context)


#@login_required(login_url='login')
def convenio_list(request):
    context = {'convenios_list':Convenio.objects.all()}
    return render(request, "rec/convenios_list.html", context)


#@login_required(login_url='login')
def convenio_form(request,id=0):
    if request.method == "GET":
        if id==0: # é insert
            form = ConvenioForm() # form vazio para ser preenchido
        else: # é update
            convenio = Convenio.objects.get(pk=id) # pego o convênio atual em edição
            form = ConvenioForm(instance=convenio) # populo o form com os dados dele        
    else: # POST
        if id == 0: # insert
            form = ConvenioForm(request.POST)
        else: # update
            convenio = Convenio.objects.get(pk=id) # pego o convênio atual em edição
            form = ConvenioForm(request.POST,instance=convenio)
        if form.is_valid():
            form.save()
        return redirect('/convenios_list/')

    return render(request, "rec/convenios_form.html", {'form':form})



@login_required(login_url='login')
def convenio_delete(request,id):
    convenio = Convenio.objects.get(pk=id) # pego o convênio atual em edição
    convenio.delete()

    return redirect('/convenios_list/')

