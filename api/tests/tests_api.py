from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
import json
# from django.core.urlresolvers import reverse
# Create your tests here.

"""
  teste para login

"""
class LoginTest(TestCase):
    databases = '__all__'
    def setUp(self):
        User.objects.create_user('eurico', password='tangoteste')

    def test_para_login_sucess(self):
        client = APIClient()
        response = client.login(username='eurico', password='tangoteste')
        self.assertTrue(response)

    def test_para_login_erro(self):
        client = APIClient()
        response = client.login(username='eurico', password='tango')
        self.assertFalse(response, False)


"""
  teste da rota para DadosMestre_Verba
"""
class ModelDadosMestreVerbaTest(APITestCase):
  databases = '__all__'
  def setUp(self):
    User.objects.create_user('eurico', password='tangoteste')

  #checa inserção de valor logado
  def test_insercao_dados_mestre_verba(self):
    data = {
          "NUMANOMES": 1,
          "CODPRD": 1,
          "DESPRD": "kdlskdlskdlk",
          "CODFILEPD": 1,
          "CODDIVFRN": 1,
          "VLRPRECOSALDOMESANTERIOR": 1,
          "VLRPRECOCREDITO": 1,
          "VLRPRECODEBITO": 1,
          "VLRMARGEMSALDOMESANTERIOR": 1,
          "VLRMARGEMCREDITO": 1,
          "VLRMARGEMDEBITO": 1
    }

    self.client.login(username='eurico', password='tangoteste')
    response = self.client.post('/api/dadosmestreverba/', data, format='json')
    print(response)
    print(data)
    self.assertEqual(response.status_code, 201)

  #checa erro em inserção de valor deslogado
  def test_insercao_novo_valor_error(self):
    data = {
          "NUMANOMES": 1,
          "CODPRD": 1,
          "DESPRD": "kdlskdlskdlk",
          "CODFILEPD": 1,
          "CODDIVFRN": 1,
          "VLRPRECOSALDOMESANTERIOR": 1,
          "VLRPRECOCREDITO": 1,
          "VLRPRECODEBITO": 1,
          "VLRMARGEMSALDOMESANTERIOR": 1,
          "VLRMARGEMCREDITO": 1,
          "VLRMARGEMDEBITO": 1
    }
    response = self.client.post('/api/dadosmestreverba/', data, format='json')
    self.assertEqual(response.status_code, 401)

  def test_consumo_de_dados_mestre_verba_deslogado(self):
    response = self.client.get('/api/dadosmestreverba/', format='json')
    self.assertEqual(response.status_code, 401)

  def test_consumo_de_dados_mestre_verba_logado_sucesso(self):
    self.client.login(username='eurico', password='tangoteste')
    response = self.client.get('/api/dadosmestreverba/', format='json')
    self.assertEqual(response.status_code, 200)

  def test_consumo_de_dados_composicao_deslogado(self):
    response = self.client.get('/api/dadosmestrecomposicao/', format='json')
    self.assertEqual(response.status_code, 401)

  def test_consumo_de_dados_composicao_logado_sucesso(self):
    self.client.login(username='eurico', password='tangoteste')
    response = self.client.get('/api/dadosmestrecomposicao/', format='json')
    self.assertEqual(response.status_code, 200)

  def test_consumo_de_plano_compras_deslogado(self):
    response = self.client.get('/api/planocompras/', format='json')
    self.assertEqual(response.status_code, 401)

  def test_consumo_de_planos_compras_logado_sucesso(self):
    self.client.login(username='eurico', password='tangoteste')
    response = self.client.get('/api/planocompras/', format='json')
    self.assertEqual(response.status_code, 200)

  #checa o retorno de dados_mestre_verba 
  def test_consumo_dados_mestre_verba(self):
    self.client.login(username='eurico', password='tangoteste')
    response = self.client.get('/api/dadosmestreverba/', format='json')
    self.assertEqual(json.loads(response.content)['results'], [])
    self.assertEqual(len(json.loads(response.content)['results']), 0)

  #checa o retorno de dados mestre composicao preco 
  def test_consumo_dados_mestre_composicao_preco(self):
    self.client.login(username='eurico', password='tangoteste')
    response = self.client.get('/api/dadosmestrecomposicao/', format='json')
    self.assertEqual(json.loads(response.content)['results'], [])
    self.assertEqual(len(json.loads(response.content)['results']), 0)

  #checa o retorno de plano de compras
  def test_consumo_plano_compras(self):
    self.client.login(username='eurico', password='tangoteste')
    response = self.client.get('/api/planocompras/', format='json')
    self.assertEqual(json.loads(response.content)['results'], [])
    self.assertEqual(len(json.loads(response.content)['results']), 0)


  #checa o retorno de diretrizes estrategicas 
  def test_consumo_diretrizes_estrategicas_csv(self):
    self.client.login(username='eurico', password='tangoteste')
    response = self.client.get('api/diretrizesestrategicacsv/', format='json')
    self.assertEqual(json.loads(response.content)['results'], [])
    self.assertEqual(len(json.loads(response.content)['results']), 0)

