from django import forms
from .models import Convenio

class ConvenioForm(forms.ModelForm):

    class Meta:
        model = Convenio
        # fields = '__all__' # considera todos os campos do model
        fields = ('nome', 'cnpj', 'telefone', 'obs')
        labels = {
            'nome':'Nome',
            'cnpj':'CNPJ',
            'telefone':'Telefone',
            'obs':'Observações',
        }

    
    # para que a combo tenha na 1a posição o texto "Selecione..."
    def __init__(self, *args, **kwargs):
        super(ConvenioForm, self).__init__(*args, **kwargs)
        self.fields['nome'].empty_label = "Selecione..."
        # caso queira remover a obrigatoriedade do campo aqui:
        self.fields['cnpj'].required = False
   