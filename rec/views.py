from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Convenio

from accounts.decorators import unauthenticated_user, allowed_users, admin_only

from .filters import ConveniosFilter

import csv
import datetime


'''
=========================================================================
Bloco CRUD - Convenios
-------------------------------------------------------------------------
...
=========================================================================
'''


# exige usuário logado
@login_required(login_url='/login/')
#@admin_only # somente usuários do grupo 'admin' podem acessar a home | posso ampliar para outros grupos ['admin','staff']
#@allowed_users(allowed_roles=['admin','customer'])
def home(request):

    context = {'convenios_list':Convenio.objects.all()}
    return render(request, 'rec/dashboard.html', context)



class ConvenioListView(LoginRequiredMixin, ListView):
    model = Convenio
    template_name = 'rec/convenios_list.html' # <app>/<model>_<viewtype>.html no lugar de # blog/post_list.html
    context_object_name = 'convenios_list'
    ordering = ['nome'] # -nomedocampo o traço, indica que desejo em ordem decrescente, invertendo a query
    paginate_by = 10 #para paginar os posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ConveniosFilter(self.request.GET, queryset=self.get_queryset())
        return context 


class ConvenioDetailView(LoginRequiredMixin, DetailView):
    model = Convenio
    template_name = 'rec/convenios_detail.html'


class ConvenioCreateView(LoginRequiredMixin, CreateView):
    model = Convenio
    template_name = 'rec/convenios_form.html' 
    fields = ('nome', 'cnpj', 'telefone', 'obs')
    labels = {
        'nome':'Nome',
        'cnpj':'CNPJ',
        'telefone':'Telefone',
        'obs':'Observações',
    }

    # se quiser que retorne à home após criar é só deixar um atributo conforme abaixo:
    # success_url = '/'

    # para sobrepor a função de validação default
    def form_valid(self, form):
        # pega a instância do form de inclusão de post e alimenta o author com o user logado
        # agora, quando salvar o post, já terá o campo author alimentado
        form.instance.user = self.request.user

        return super().form_valid(form)


class ConvenioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Convenio
    template_name = 'rec/convenios_form.html' 
    fields = ('nome', 'cnpj', 'telefone', 'obs')
    labels = {
        'nome':'Nome',
        'cnpj':'CNPJ',
        'telefone':'Telefone',
        'obs':'Observações',
    }

    # se quiser que retorne à home após criar é só deixar um atributo conforme abaixo:
    # success_url = '/'

    # para sobrepor a função de validação default
    def form_valid(self, form):
        # pega a instância do form de inclusão de post e alimenta o author com o user logado
        # agora, quando salvar o post, já terá o campo author alimentado
        form.instance.user = self.request.user

        return super().form_valid(form)

    # para verificar autorizações necessárias retornando True ou False
    def test_func(self):
        convenio = self.get_object() # convenio que estou tentando editar
        #if self.request.user == post.author:
        return True # libera se for do mesmo autor
        #return False  


class ConvenioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Convenio
    template_name = 'rec/convenios_confirm_delete.html' 
    success_url = '/convenios/list/'

    # para verificar autorizações necessárias retornando True ou False
    def test_func(self):
        convenio = self.get_object() # convenio que estou tentando editar
        #if self.request.user == post.author:
        return True # libera se for do mesmo autor
        #return False  

@login_required(login_url='/login/')
def export_csv(request):

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Nome', 'CNPJ', 'Telefone', 'Observações'])

    convenios = Convenio.objects.filter()
    #convenios = Convenio.objects.all().values_list('name', 'cnpj', 'telefone', 'obs')
    #convenios = Convenio.objects.all()
    for record in convenios:
        #writer.writerow(record)
        writer.writerow([record.nome, record.cnpj, record.telefone, record.obs])

    #response['Content-Disposition'] = 'attachment; filename="members.csv"'
    response['Content-Disposition'] = 'attachment; filename=convenios_' + str(datetime.datetime.now()) + '.csv'

    return response
