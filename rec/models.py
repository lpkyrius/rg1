from django.db import models

# Create your models here.

class Convenio(models.Model):
    nome = models.CharField(max_length=100, unique=True )
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    obs = models.CharField(max_length=100, null=True, blank=True)


'''
A cada alteração:

python3 manage.py makemigrations
python3 manage.py sqlmigrate
python3 manage.py migrate

'''