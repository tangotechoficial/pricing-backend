from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
import json
from datetime import datetime
from django.utils.timezone import make_aware
# from django.core.urlresolvers import reverse
# Create your tests here.

def cria_mercadoria(self):
        novo_comprador = {
            "CODCPRATU": 1, 
            "NOMCPRATU": "teste",
            "CODCLLCMPATU": 1,
            "DESCLLCMPATU": "teste",
            "CODDRTCLLATU": 1, 
            "DESDRTCLLATU": "teste"
        }
        self.client.login(username='eurico', password='tangoteste')
        self.client.post('/api/comprador/', novo_comprador, format='json')
        novo_fornecedor = {
            "CODFRN": 1,
            "NOMFRN": "teste",
            "CODGRPFRN": 1,
            "NOMGRPFRN": "teste"
        }
        self.client.login(username='eurico', password='tangoteste')
        self.client.post('/api/fornecedor/', novo_fornecedor, format='json')
        novo_tabAuxGrp = {
            "Id_Aux": 1,
            "CODSUBCTGPRD": 1,
            "DESSUBCTGPRD": "teste",
            "CODCTGPRD": 1,
            "DESCTGPRD": "teste",
            "CODGRPPRD": 1,
            "DESGRPPRD": "teste",
            "Linha_de_negocio":  "teste"
        }
        self.client.login(username='eurico', password='tangoteste')
        self.client.post('/api/tabauxgrp/', novo_tabAuxGrp, format='json')
        novo_relacionamento_filial_regiao = {
            "CODFILEPD": 1,
            "NOMFILEPD": "teste",
            "CODFILFAT": 1,
            "NOMFILFAT": "teste",
            "CODESTUNI": "HI",
            "NOMESTUNI": "teste",
            "TIPEDEREG": 1,
            "CODEDEREG": 1
        }
        self.client.login(username='eurico', password='tangoteste')
        self.client.post('/api/relacionamentofilial/', novo_relacionamento_filial_regiao, format='json')
        nova_mercadoria = {
            "CODPRD": 1,
            "Id_Aux": 1,
            "DESPRD": "teste",
            "CODDIVFRN": 1,
            "CODCPRATU": 1,
            "CODSML": 1,
            "dessml": "teste",
            "ABC": "T"
        }
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.post('/api/mercadoria/', nova_mercadoria, format='json')
        return response

class LoginTest(TestCase):
    """
    teste para login

    """
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


class FornecedorTest(TestCase):
    """
    teste da rota para fornecedor

    """
    databases = '__all__'

    def setUp(self):
        User.objects.create_user('eurico', password='tangoteste')


    def test_post_fornecedor(self):
        """

        testa criação de novo objeto

        """
        novo_fornecedor = {
            "CODFRN": 1,
            "NOMFRN": "teste",
            "CODGRPFRN": 1,
            "NOMGRPFRN": "teste"
        }
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.post(
            '/api/fornecedor/', novo_fornecedor, format='json')
        self.assertEqual(response.status_code, 201)

        """

        teste ataulização de campo

        """
        data = {"DESDIVFRN": "update"}
        fornecedor = self.client.put('/api/fornecedor/', data, pk=1)
        print(fornecedor)


class CompradorTest(APITestCase):
    """

    teste da rota para Comprador

    """

    databases = '__all__'

    def setUp(self):
        User.objects.create_user('eurico', password='tangoteste')

    def test_criacao_comprador(self):
        novo_comprador = {
            "CODCPRATU": 1, 
            "NOMCPRATU": "teste",
            "CODCLLCMPATU": 1,
            "DESCLLCMPATU": "teste",
            "CODDRTCLLATU": 1, 
            "DESDRTCLLATU": "teste"
        }
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.post(
            '/api/comprador/', novo_comprador, format='json')
        self.assertEqual(response.status_code, 201)
        
class RelacionamentoFilialRegiaoTest(APITestCase):
    """

    teste da rota para relacionamento_filial_regiao

    """

    databases = '__all__'

    def setUp(self):
        User.objects.create_user('eurico', password='tangoteste')

    def test_criacao_relacionamento_filial_regiao(self):
        novo_relacionamento_filial_regiao = {
            "CODFILEPD": 1,
            "NOMFILEPD": "teste",
            "CODFILFAT": 1,
            "NOMFILFAT": "teste",
            "CODESTUNI": "HI",
            "NOMESTUNI": "teste",
            "TIPEDEREG": 1,
            "CODEDEREG": 1
        }
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.post(
            '/api/relacionamentofilial/', novo_relacionamento_filial_regiao, format='json')
        self.assertEqual(response.status_code, 201)

class TabAuxGrpTest(APITestCase):
    """

    teste da rota para TabAuxGrp

    """

    databases = '__all__'

    def setUp(self):
        User.objects.create_user('eurico', password='tangoteste')

    """

    cria novo objeto TabAuxGrp

    """

    def test_criacao_tabAuxGrp(self):
        novo_tabAuxGrp = {
            "Id_Aux": 1,
            "CODSUBCTGPRD": 1,
            "DESSUBCTGPRD": "teste",
            "CODCTGPRD": 1,
            "DESCTGPRD": "teste",
            "CODGRPPRD": 1,
            "DESGRPPRD": "teste",
            "Linha_de_negocio":  "teste"
        }
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.post(
            '/api/tabauxgrp/', novo_tabAuxGrp, format='json')
        self.assertEqual(response.status_code, 201)

class RepresentanteTest(APITestCase):
    """

    teste da rota para Representante

    """

    databases = '__all__'

    def setUp(self):
        User.objects.create_user('eurico', password='tangoteste')

    """

    cria novo objeto Representante

    """

    def test_criacao_representante(self):
        novo_representante = {
            "CODREPCMC": 1,
            "NOMREPCMC": "teste",
            "DATCADREPCMC": make_aware(datetime.now())
        }
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.post(
            '/api/representante/', novo_representante, format='json')
        self.assertEqual(response.status_code, 201)

class MercadoriaTest(APITestCase):
    """

    teste para rota de Mercadoria


    """
    databases = '__all__'
    
    def setUp(self):
        User.objects.create_user('eurico', password='tangoteste')


    def test_criacao_de_nova_mercadoria(self):    
        response = cria_mercadoria(self)
        self.assertEqual(response.status_code, 400)
        
        



class DadosMestreVerbaTest(APITestCase):
    """
    teste da rota para DadosMestre_Verba

    """
    databases = '__all__'

    def setUp(self):
        User.objects.create_user('eurico', password='tangoteste')

    def test_insercao_dados_mestre_verba(self):
        """
        
        checa inserção de valor logado

        """
        novo_dado_verba = {
            "NUMANOMES": 1,
            "CODPRD": 1, 
            "DESPRD": "teste",
            "CODFILEPD": 1,
            "CODDIVFRN": 1,
            "VLRPRECOSALDOMESANTERIOR": 1.0,
            "VLRPRECOCREDITO": 1.0,
            "VLRPRECODEBITO": 1.0,
            "VLRMARGEMSALDOMESANTERIOR": 1.0,
            "VLRMARGEMCREDITO": 1.0,
            "VLRMARGEMDEBITO": 1.0
        }

        self.client.login(username='eurico', password='tangoteste')
        response = self.client.post('/api/dadosmestreverba/', novo_dado_verba, format='json')
        self.assertEqual(response.status_code, 201)


    def test_insercao_novo_valor_error(self):
        """
        
        checa erro em inserção de valor deslogado

        """
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
        response = self.client.post(
            '/api/dadosmestreverba/', data, format='json')
        self.assertEqual(response.status_code, 401)


    def test_consumo_de_dados_mestre_verba_deslogado(self):
        """

        Testa erro de consumo de dados mestre verba deslogador

        """
        response = self.client.get('/api/dadosmestreverba/', format='json')
        self.assertEqual(response.status_code, 401)


    def test_consumo_de_dados_mestre_verba_logado_sucesso(self):
        """

        Testa consumo de dados mestre verba logado

        """
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.get('/api/dadosmestreverba/', format='json')
        self.assertEqual(response.status_code, 200)


    def test_consumo_de_dados_composicao_deslogado(self):
        """

        Testa erro de consumo de dados composição preco deslogado

        """
        response = self.client.get(
            '/api/dadosmestrecomposicao/', format='json')
        self.assertEqual(response.status_code, 401)
    

    def test_consumo_de_dados_composicao_logado_sucesso(self):
        """

        Testa consumo de dados composição preco logado

        """
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.get(
            '/api/dadosmestrecomposicao/', format='json')
        self.assertEqual(response.status_code, 200)


    def test_consumo_de_plano_compras_deslogado(self):
        """

        Testa erro de consumo de planos compras deslogado

        """
        response = self.client.get('/api/planocompras/', format='json')
        self.assertEqual(response.status_code, 401)

    

    def test_consumo_de_planos_compras_logado_sucesso(self):
        """

        Testa consumo de planos compras logado

        """
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.get('/api/planocompras/', format='json')
        self.assertEqual(response.status_code, 200)


    def test_consumo_dados_mestre_verba(self):
        """
        
        checa o retorno de dados_mestre_verba

        """
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.get('/api/dadosmestreverba/', format='json')
        self.assertEqual(json.loads(response.content)['results'], [])
        self.assertEqual(len(json.loads(response.content)['results']), 0)

    def test_consumo_dados_mestre_composicao_preco(self):
        """

        checa o retorno de dados mestre composicao preco

        """
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.get(
            '/api/dadosmestrecomposicao/', format='json')
        self.assertEqual(json.loads(response.content)['results'], [])
        self.assertEqual(len(json.loads(response.content)['results']), 0)

    def test_consumo_plano_compras(self):
        """
        
        checa o retorno de plano de compras

        """
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.get('/api/planocompras/', format='json')
        self.assertEqual(json.loads(response.content)['results'], [])
        self.assertEqual(len(json.loads(response.content)['results']), 0)


    def test_consumo_diretrizes_estrategicas_csv(self):
        """
        
        checa o retorno de diretrizes estrategicas  csv

        """
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.get('/api/diretrizesestrategicacsv/', format='json')
        self.assertEqual(json.loads(response.content)['results'], [])
        self.assertEqual(len(json.loads(response.content)['results']), 0)


    def test_consumo_diretrizes_estrategicas(self):
        """

        checa o retorno de diretrizes estrategicas 

        """ 
        self.client.login(username='eurico', password='tangoteste')
        response = self.client.get('/api/diretrizesestrategica/', format='json')
        self.assertEqual(json.loads(response.content)['results'], [])
        self.assertEqual(len(json.loads(response.content)['results']), 0)
