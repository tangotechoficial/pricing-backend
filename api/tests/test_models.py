from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from api.models import DadosMestre_ComposicaoPreco, DadosMestre_Verba, PlanoCompras
from datetime import datetime
from django.utils.timezone import make_aware
import json

#models test

class DadosMestreVerbaTest(TestCase):
	databases = '__all__'

	#cria uma instância de dados_mestre_verba
	def create_dados_mestre_verba(self):
		return DadosMestre_Verba.objects.create(NUMANOMES='135', CODPRD=125, CODFILEPD=22, CODDIVFRN=23, VLRPRECOSALDOMESANTERIOR=12, VLRPRECOCREDITO=23, VLRMARGEMSALDOMESANTERIOR=17,
		VLRPRECODEBITO=24, VLRMARGEMCREDITO=76, VLRMARGEMDEBITO=13 )

	#verifica se o objeto criado é uma instância da classe desejada
	def test_criacao_de_model_verba(self):
		dado = self.create_dados_mestre_verba()
		self.assertTrue(isinstance(dado, DadosMestre_Verba))

class DadosMestreComposicaoPrecoTest(TestCase):
	#cria uma instância de dados_mestre_composicao_de_preco
	def create_dados_mestre_composicao_preco(self):
		return DadosMestre_ComposicaoPreco.objects.create(CODPRD=125, SENSIVEL_REBATE=123, TIPEDEREG=12, CODEDEREG=10, CODFILEMP=10,
		CODFILFAT=12, FLEX=13, DATA_PRECO=make_aware(datetime.now()))

	#verifica se o objeto criado é uma instância da classe desejada 
	def test_criacao_de_model(self):
		dado = self.create_dados_mestre_composicao_preco()
		self.assertTrue(isinstance(dado, DadosMestre_ComposicaoPreco))


class PlanoDeCompras(TestCase):
	"""
		cria uma instância de PlanoCompras
		
	"""
	def create_plano_de_compras(self):
		return PlanoCompras.objects.create(CODPRD=125, CODFILEMP=10, CODFILFAT=12, DATA_PRECO=make_aware(datetime.now()), CODESTUNI=2)
	
	"""
		verifica se o objeto criado é uma instância da classe desejada 
		checa as propriedades existentes na instância

	"""
	def test_criacao_de_model(self):
		dado = self.create_plano_de_compras()

		self.assertTrue(isinstance(dado, PlanoCompras))
		self.assertTrue(hasattr(dado, 'CODPRD'))
		self.assertTrue(hasattr(dado, 'CODFILEMP'))
		self.assertTrue(hasattr(dado, 'PRECO_VENDA_LIQUIDO_SUGERIDO'))
	
	
