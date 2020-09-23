from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Convenio(models.Model):
    nome = models.CharField(max_length=100, unique=True )
    cnpj = models.CharField(max_length=14, null=True, blank=True, default=' ')
    telefone = models.CharField(max_length=100, null=True, blank=True, default=' ')
    obs = models.CharField(max_length=300, null=True, blank=True, default=' ')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    data_ultima_alteracao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse('convenios_detail', kwargs={'pk': self.pk})

'''
A cada alteração:

python3 manage.py makemigrations
python3 manage.py sqlmigrate
python3 manage.py migrate

'''