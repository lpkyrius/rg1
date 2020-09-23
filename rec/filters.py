import django_filters
from .models import Convenio

'''
=========================================================================
Classe dos filtros/ordenação utilizados na tela de listagem dos convênios
-------------------------------------------------------------------------
A ordenação e o filtro são mantidos na impressão, mas não no export csv,
este leva todos os registros, que podem ser filtrados e ordenados via 
Excel.
=========================================================================
'''

class ConveniosFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Crescente'),
        ('descending', 'Decrescente'),
    )
    ordering = django_filters.ChoiceFilter(label='Ordem', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Convenio
        fields = {
            'nome': ['icontains'],
            'cnpj': ['icontains'],
        }
    
    def filter_by_order(self, queryset, name, value):
        expression = 'nome' if value == 'ascending' else '-nome'
        return queryset.order_by(expression)
    
    