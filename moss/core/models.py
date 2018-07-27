import datetime
from django.db import models
from django.utils import timezone


# Create your models here
class  Cliente(models.Model):
	cnpj = models.CharField(max_length=17, unique=True)
	razao_social = models.CharField(max_length=50)
	fantasia = models.CharField(max_length=50)

	def __str__(self):
		return self.razao_social

	def  __str__(self):
		return self.fantasia



class Chamado(models.Model):
	cnpj = models.CharField(max_length=17, unique=True)
	nome = models.CharField(max_length=50)
	defeito = models.CharField(max_length=200)
	nome_sistema = models.CharField(max_length=50)
	data_abertura = models.DateTimeField('Data de Abertura de Chamdado')

	def __str__(self):
		return self.nome



class Tecnico(models.Model):
	nome = models.CharField(max_length=50)