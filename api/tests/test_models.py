from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from api import models
from datetime import datetime
from django.utils.timezone import make_aware
import json

"""
Models test

"""


class FornecedorTest(TestCase):
    databases = '__all__'

    def test_criacao_de_instancia_fornecedor(self):
        """
            verifica se o objeto criado é uma instância da classe desejada

        """
        fornecedor = models.Fornecedor.objects.create(
            CODFRN=1,
            NOMFRN='teste',
            CODGRPFRN=1,
            NOMGRPFRN='teste'
        )
        self.assertTrue(isinstance(fornecedor, models.Fornecedor))
        self.assertTrue(hasattr(fornecedor, 'CODFRN'))
        self.assertTrue(hasattr(fornecedor, 'NOMFRN'))
        self.assertTrue(hasattr(fornecedor, 'CODGRPFRN'))
        self.assertTrue(hasattr(fornecedor, 'NOMGRPFRN'))


class CompradorTest(TestCase):
    databases = '__all__'

    def create_comprador(self):
        """
            cria uma instância de COMPRADOR
        """
        return models.Comprador.objects.create(
            CODCPR=1,
            NOMCPR='teste',
            CODDIVCMP=1,
            DESDIVCMP='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )

    def test_criacao_de_instancia_de_comprador(self):
        """

        verifica uma instância de comprador

        """
        comprador = self.create_comprador()
        self.assertTrue(isinstance(comprador, models.Comprador))


class FilialTest(TestCase):

    def create_filial(self):
        """

        cria uma instância de Relacionamento Filial Região

        """
        return models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            TIPEDEREG=1,
            CODEDEREG=1
        )

    def test_criacao_de_filial(self):
        """
            verifica se o objeto criado é uma instância da classe desejada

        """
        filial = self.create_filial()
        self.assertTrue(isinstance(filial, models.RelacionamentoFilialRegiao))


class MercadoriaTest(TestCase):


    def test_cria_mercadoria(self):
        """
        teste do model Mercadoria

        """
        comprador = models.Comprador.objects.create(
            CODCPR=1,
            NOMCPR='teste',
            CODDIVCMP=1,
            DESDIVCMP='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        fornecedor = models.Fornecedor.objects.create(
            CODFRN=1,
            NOMFRN='teste',
            CODGRPFRN=1,
            NOMGRPFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODMER=1,
            DESMER='teste',
            CODFRNPCPMER=fornecedor,
            CODCPRATU=comprador,
            CODGRPMERSMR=1,
            DESGRPMERSMR='teste',
            CLFCRVABCMER='1'
        )
        self.assertTrue(isinstance(mercadoria, models.Mercadoria))
        self.assertTrue(isinstance(mercadoria.CODFRNPCPMER, models.Fornecedor))
        self.assertTrue(isinstance(mercadoria.CODCPRATU, models.Comprador))


class TabAuxGrpTeste(TestCase):
    def test_criacao_de_grupo(self):
        comprador = models.Comprador.objects.create(
            CODCPR=1,
            NOMCPR='teste',
            CODDIVCMP=1,
            DESDIVCMP='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        fornecedor = models.Fornecedor.objects.create(
            CODFRN=1,
            NOMFRN='teste',
            CODGRPFRN=1,
            NOMGRPFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODMER=1,
            DESMER='teste',
            CODFRNPCPMER=fornecedor,
            CODCPRATU=comprador,
            CODGRPMERSMR=1,
            DESGRPMERSMR='teste',
            CLFCRVABCMER='1'
        )
        grupo = models.TabAuxGrp.objects.create(
            Id_Aux = 1,
            CODMER = mercadoria,
            CODCLSMER = 1,
            DESCLSMER = 'teste',
            CODFMLMER = 1,
            DESFMLMER = 'teste',
            CODGRPMER = 1,
            DESGRPMER = 'teste'
        )
        self.assertTrue(isinstance(grupo, models.TabAuxGrp))
        self.assertTrue(isinstance(grupo.CODMER, models.Mercadoria))


class DadosMestreVerba(TestCase):


    def create_dados_mestre_verba(self):
        """

        cria uma instância de dados_mestre_verba

        """
        return models.DadosMestre_Verba.objects.create(
                CODPRD = 1,
                CODSMLPCO = 1,
                CODFILEPD = 1,
                DATREF = make_aware(datetime.now()),
                VLRSLDPCOMESANT = 1.0,
                VLRCRDPCO = 1.0,
                VLRDBTPCO = 1.0,
                VLRSLDMRGMESANT = 1.0,
                VLRCRDMRG = 1.0,
                VLRDBTMRG = 1.0
                )


    def test_criacao_de_model_verba(self):
        """
            verifica se o objeto criado é uma instância da classe desejada

        """
        dado = self.create_dados_mestre_verba()
        self.assertTrue(isinstance(dado, models.DadosMestre_Verba))



# class DadosMestreComposicaoPrecoTest(TestCase):
#     """

#     cria uma instância de dados_mestre_composicao_de_preco

#     """

#     def create_dados_mestre_composicao_preco(self):
#         comprador = models.Comprador.objects.create(
#             CODCPR=1,
#             NOMCPR='teste',
#             CODDIVCMP=1,
#             DESDIVCMP='teste',
#             CODDRTCLLATU=1,
#             DESDRTCLLATU='teste'
#         )
#         fornecedor = models.Fornecedor.objects.create(
#             CODFRN=1,
#             NOMFRN='teste',
#             CODGRPFRN=1,
#             NOMGRPFRN='teste'
#         )
#         mercadoria = models.Mercadoria.objects.create(
#             CODMER=1,
#             DESMER='teste',
#             CODFRNPCPMER=fornecedor,
#             CODCPRATU=comprador,
#             CODGRPMERSMR=1,
#             DESGRPMERSMR='teste',
#             CLFCRVABCMER='1'
#         )
#         filial = models.RelacionamentoFilialRegiao.objects.create(
#             CODFILEPD=1,
#             NOMFILEPD='teste',
#             CODFILFAT=1,
#             NOMFILFAT='teste',
#             CODESTUNI='SP',
#             TIPEDEREG=1,
#             CODEDEREG=1
#         )
#         return models.DadosMestre_ComposicaoPreco.objects.create(
#                     CODPRD = mercadoria,
#                     CODFILEPD = filial,
#                     CODFILFAT = 1,
#                     DATREF = make_aware(datetime.now()),
#                     CODESTUNI = 'SP',
#                     TIPEDEREG = 1,
#                     VLRMRGBRT = 1.0,
#                     VLRVBA = 1.0,
#                     VLRFND = 1.0,
#                     VLRFNDRBTITE = 1.0,
#                     VLRICM = 1.0,
#                     VLRPIS = 1.0,
#                     VLRDVL = 1.0,
#                     VLRUNTPCOALV = 1.0,
#                     VLRFLXCNS = 1.0,
#                     VLRCSTCAL = 1.0,
#                     VLRBNF = 1.0,
#                     VLRCPLCSTPCO = 1.0,
#                     VLRPCOBSEMER = 1.0,
#                     CODREGPCO = 1.0,
#                     NUMRLCCIDGIR = 1.0,
#                     TIPCALUTZPCOLIQ = 1.0,        
#                 )

    """

    verifica se o objeto criado pertence à instância desejada

    """

    # def test_criacao_de_model_composicao_preco(self):
    #     dado = self.create_dados_mestre_composicao_preco()
    #     self.assertTrue(isinstance(dado, models.DadosMestre_ComposicaoPreco))
    #     self.assertTrue(isinstance(dado.CODPRD, models.Mercadoria))
    #     self.assertTrue(isinstance(
    #         dado.CODFILEPD, models.RelacionamentoFilialRegiao))


class PlanoDeCompras(TestCase):
    """
        cria uma instância de PlanoCompras

    """

    def test_criacao_de_model_plano_compras(self):
        comprador = models.Comprador.objects.create(
            CODCPR=1,
            NOMCPR='teste',
            CODDIVCMP=1,
            DESDIVCMP='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        fornecedor = models.Fornecedor.objects.create(
            CODFRN=1,
            NOMFRN='teste',
            CODGRPFRN=1,
            NOMGRPFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODMER=1,
            DESMER='teste',
            CODFRNPCPMER=fornecedor,
            CODCPRATU=comprador,
            CODGRPMERSMR=1,
            DESGRPMERSMR='teste',
            CLFCRVABCMER='1'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        plano_compras = models.PlanoCompras.objects.create(
            CODPRD = mercadoria,
            CODFILEPD = filial,
            CODFILFAT = 1,
            CODESTUNI = 'sp',
            MONTH = "09",
            YEAR = "09",
            WEEK = "09",
            VOLVNDSUG = 1.0,
            VOLVNDSUGALC = 1.0,
            MRGBRTPEROCD = 1.0,
            VLRPCOSUG = 1.0,
            VLRPCOBASESUG = 1.0,
            VLRIMPTOTSUG = 1.0,
            VLRICMSSUG = 1.0,
            VLRPISCOFSUG = 1.0,
            VLRDEVSUG = 1.0,
            VLRFLXSUG = 1.0,
            VLRMRGBRTSUG = 1.0,
            VRBUNTSUGSUG = 1.0,
            VLRVRBPLAN   = 'teste',
            VLRCMVPCOSUG = 1.0,
            VLRCMVPCOATU = 1.0,
            VLRCMVCMPATU = 'teste',
            VOLVNDPLN = 1.0,
            VLRPCOPLN = 1.0,
            VLRPCOBASEPLN = 1.0,
            VLRIMPTOTPLN = 1.0,
            VLRICMSPLN = 1.0,
            VLRPISCOFPLN = 1.0,
            VLRDEVPLN = 1.0,
            VLRFLXPLN = 1.0,
            VLRMRGBRTPLN = 1.0,
            VRBUNTSUGPLN = 1.0,
            VLRVRBPLN = 1.0,
            VLRCMVPCOPLN = 1.0,
            VLRCMVCMPPLN = 1.0
        )

        """
        verifica se o objeto criado é uma instância da classe desejada
        checa as propriedades existentes na instância

        """



        self.assertTrue(isinstance(plano_compras, models.PlanoCompras))
        self.assertTrue(isinstance(plano_compras.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(
            plano_compras.CODFILEPD, models.RelacionamentoFilialRegiao))


"""
testa model de elasticidade

"""


class ElasticidadeTest(TestCase):

    def test_instancia_elasticidade(self):
        comprador = models.Comprador.objects.create(
            CODCPR=1,
            NOMCPR='teste',
            CODDIVCMP=1,
            DESDIVCMP='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        fornecedor = models.Fornecedor.objects.create(
            CODFRN=1,
            NOMFRN='teste',
            CODGRPFRN=1,
            NOMGRPFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODMER=1,
            DESMER='teste',
            CODFRNPCPMER=fornecedor,
            CODCPRATU=comprador,
            CODGRPMERSMR=1,
            DESGRPMERSMR='teste',
            CLFCRVABCMER='1'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        elasticidade = models.Elasticidade.objects.create(
                CODPRD = mercadoria,
                CODESTUNI = 'SP',
                CODFILEPD = filial,
                CODFILFAT = 1,
                VLRVARVNDPCO = 1.0,
                DESMER = 'teste',
                CLFCRVABCMER = '1', 
                CODGRPMERSMR = 1,
                DESGRPMERSMR = 'teste',
                DESFMLMER = 1,
                DESCLSMER = 1,
                DESDIVCMP = 'teste',
        )
        """

		verifica instâncias do item e de suas chaves estrangeiras

		"""
        self.assertTrue(isinstance(elasticidade, models.Elasticidade))
        self.assertTrue(isinstance(elasticidade.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(elasticidade.CODFILEPD, models.RelacionamentoFilialRegiao))


"""
teste do model Estoque

"""


class EstoqueTest(TestCase):
    def test_estoque(self):
        comprador = models.Comprador.objects.create(
            CODCPR=1,
            NOMCPR='teste',
            CODDIVCMP=1,
            DESDIVCMP='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        fornecedor = models.Fornecedor.objects.create(
            CODFRN=1,
            NOMFRN='teste',
            CODGRPFRN=1,
            NOMGRPFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODMER=1,
            DESMER='teste',
            CODFRNPCPMER=fornecedor,
            CODCPRATU=comprador,
            CODGRPMERSMR=1,
            DESGRPMERSMR='teste',
            CLFCRVABCMER='1'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        estoque = models.Estoque.objects.create(
            
            CODPRD = mercadoria,
            CODFILEPD = filial,
            DATREF = make_aware(datetime.now()),
            NUMSMNANO = make_aware(datetime.now()),
            NOMDIASMN = make_aware(datetime.now()),
            NOMMESANO = make_aware(datetime.now()),
            NOMSMSANO = make_aware(datetime.now()),
            VLRUNTCSTSCO = 1.0,
            QDEITEETQ = 1,
            VLRVNDPDAFLTETQ = 1.0,
            VLRCSTCMPIDL = 1.0,
            VLRMEDPCOCMP = 1.0,
            CODSTAPRDETQ = 1

        )
        self.assertTrue(isinstance(estoque, models.Estoque))
        self.assertTrue(isinstance(estoque.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(
            estoque.CODFILEPD, models.RelacionamentoFilialRegiao))


"""

teste do model Competitividade

"""


class CompetitividadeTest(TestCase):
    def test_competitividade(self):
        comprador = models.Comprador.objects.create(
            CODCPR=1,
            NOMCPR='teste',
            CODDIVCMP=1,
            DESDIVCMP='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        fornecedor = models.Fornecedor.objects.create(
            CODFRN=1,
            NOMFRN='teste',
            CODGRPFRN=1,
            NOMGRPFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODMER=1,
            DESMER='teste',
            CODFRNPCPMER=fornecedor,
            CODCPRATU=comprador,
            CODGRPMERSMR=1,
            DESGRPMERSMR='teste',
            CLFCRVABCMER='1'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        competitividade = models.Competitividade.objects.create(
            CODPRD = mercadoria,
            CODIDTCUR = 1,
            CODESTUNI = "sp",
            CODESTUNIORI = "sp",
            CODESTUNIDSN = "sp",
            NUMANO = make_aware(datetime.now()),
            NUMANOMES = make_aware(datetime.now()),
            NUMSMNANO = make_aware(datetime.now()),
            NOMMES = make_aware(datetime.now()),
            DATREF = make_aware(datetime.now()),
            CODSML = 1,
            DESGRPMERSMR = 'teste',
            CODTIPAPU = 'teste',
            VLRPCOMEDMCD = 1.0,
            VLRPCOBSEMER = 1.0,
            CLFCRVABCMER = '1',
            CODDIVFRN = fornecedor
        )

        self.assertTrue(isinstance(competitividade, models.Competitividade))
        self.assertTrue(isinstance(competitividade.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(competitividade.CODDIVFRN, models.Fornecedor))




class RepresentanteTest(TestCase):
    """

    teste do model Representante

    """
    def test_representante(self):
        representante = models.Representante.objects.create(
            CODREPCMC=1,
            NOMREPCMC='teste',
            DATCADREPCMC=make_aware(datetime.now())
        )
        self.assertTrue(representante, models.Representante)


"""

teste da classe Vendas 

"""


class VendasTest(TestCase):
    def test_vendas(self):
        comprador = models.Comprador.objects.create(
            CODCPR=1,
            NOMCPR='teste',
            CODDIVCMP=1,
            DESDIVCMP='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        fornecedor = models.Fornecedor.objects.create(
            CODFRN=1,
            NOMFRN='teste',
            CODGRPFRN=1,
            NOMGRPFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODMER=1,
            DESMER='teste',
            CODFRNPCPMER=fornecedor,
            CODCPRATU=comprador,
            CODGRPMERSMR=1,
            DESGRPMERSMR='teste',
            CLFCRVABCMER='1'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        representante = models.Representante.objects.create(
            CODREPCMC=1,
            NOMREPCMC='teste',
            DATCADREPCMC=make_aware(datetime.now())
        )
        vendas = models.Vendas.objects.create(
            CODPRD = mercadoria,
            CODFILEPD = 1,
            CODFILFAT = 1,
            CODESTCLI = 'SP',
            CODREPCMC = representante,
            NUMPED = 1,
            NUMANOMESSMN = make_aware(datetime.now()),
            NUMANOMESDIA = make_aware(datetime.now()),
            VLRVNDLIQ = 1.0,
            QDEITE = 1,
            VLRDSCFLXCNS = 1.0,
            VLRSUPFLX = 1.0,
            VLRIMPTOT = 1.0,
            VLRRCTLIQAPU = 1.0,
            VLRCSTMEDPRD = 1.0,
            PERMRGADICNLVND = 1.0,
            VLRFND = 1.0,
            VLRMRGBRT = 1.0,
            VLRCSTTRNTNLCUB = 1.0,
            VLRCSTDTB = 1.0,
            VLRCSTARG = 1.0,
            VLRMRGCRB = 1.0
        )
        self.assertTrue(isinstance(vendas, models.Vendas))
        self.assertTrue(isinstance(vendas.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(vendas.CODREPCMC, models.Representante))




class VerbaeBCTest(TestCase):
    """
    teste do model VerbaeBC

    """
    def test_verba_e_bc(self):
        comprador = models.Comprador.objects.create(
            CODCPR=1,
            NOMCPR='teste',
            CODDIVCMP=1,
            DESDIVCMP='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        fornecedor = models.Fornecedor.objects.create(
            CODFRN=1,
            NOMFRN='teste',
            CODGRPFRN=1,
            NOMGRPFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODMER=1,
            DESMER='teste',
            CODFRNPCPMER=fornecedor,
            CODCPRATU=comprador,
            CODGRPMERSMR=1,
            DESGRPMERSMR='teste',
            CLFCRVABCMER='1'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        verba = models.VerbaeBC.objects.create(
            CODPRD = mercadoria,
            CODFILEPD = filial,
            CODFILFAT = 1,
            CODCLI = 1, 
            CODESTCLI = 1,
            NUMANOMESDIA = make_aware(datetime.now()),
            QDEITEPED = 1,
            VLRVNDLIQ = 1.0,
            VLRUNTCSTMER = 1.0,
            VLRCSTMER = 1.0,
            VLRUNTFNDMER = 1.0,
            VLRFND = 1.0,
            QDEITEPMC = 1,
            QDEITEBFC = 1,
            VLRUNTFNDPMCVND = 1.0,
            VLRUNTDSCBFCITE = 1.0,
            VLRUNTFNDPCO = 1.0,
            VLRUNTFNDMRG = 1.0,
            VLRRLZPMC = 1.0,
            VLRBFC = 1.0,
            VLRFNDPCOVND = 1.0,
            VLRFNDPCOCST = 1.0,
            VLRMNSFNDRCBFRN = 1.0,
            VLRRBTCAL = 1.0
        )
        self.assertTrue(isinstance(verba, models.VerbaeBC))
        self.assertTrue(isinstance(verba.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(verba.CODFILEPD,
                                   models.RelacionamentoFilialRegiao))




class DiretrizesEstrategicaTeste(TestCase):
    """

    teste do model Diretriz Estratégica

    """
    def test_diretriz_estrategica(self):
        """

        cria a instância principal

        """
        diretriz_estrategica = models.DiretrizesEstrategica.objects.create(
            CODESTUNI = 1,
            CODDIVFRN = 1,
            DATREFPOD = make_aware(datetime.now()),
            NOMMES = make_aware(datetime.now()), 
            NOMSMS = make_aware(datetime.now()), 
            NOMDIASMN = make_aware(datetime.now()), 
            NOMSMSANO = make_aware(datetime.now()), 
            CODUNDNGCCLI = 1,
            CODCLLCMPATU = 1,
            DESDRTCLLATU = 'teste',
            CODSGMNGCCLI = 1,
            VLRVNDFATLIQ = 1.0,
            VLRRCTLIQAPU = 1.0,
            VLRMRGCRB = 1.0,
            VLRMRGBRT = 1.0,
            NOMCPR = 'teste',
            CODFIL = 1,
            CODCLSMER = 1,
            DESCLSMER = 'teste',
            CODFMLMER = 1,
            DESGRPMER = 'teste',
            CODGRPMER = 1,
            DESFMLMER = 'teste'
        )
        self.assertTrue(isinstance(
            diretriz_estrategica, models.DiretrizesEstrategica))



"""

teste do model Otimizador

"""


class OtimizadorTest(TestCase):
    def test_otimmizador_instances(self):
        comprador = models.Comprador.objects.create(
            CODCPR=1,
            NOMCPR='teste',
            CODDIVCMP=1,
            DESDIVCMP='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        fornecedor = models.Fornecedor.objects.create(
            CODFRN=1,
            NOMFRN='teste',
            CODGRPFRN=1,
            NOMGRPFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODMER=1,
            DESMER='teste',
            CODFRNPCPMER=fornecedor,
            CODCPRATU=comprador,
            CODGRPMERSMR=1,
            DESGRPMERSMR='teste',
            CLFCRVABCMER='1'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        otimizador = models.Otimizador.objects.create(
            DATREF=make_aware(datetime.now()),
            CODPRD = mercadoria,
            CODFILEPD = filial,
            CODFILFAT = 1,
            VLRVBA = 1.0,
            VLRVBADIS = 1.0,
            VLRVBAINP = 1.0,
            VLRVBACAL = 1.0,
            VLRVBADEM = 1.0,
            VLRCSTMERVND = 0.0,
            CODESTUNI = 'SP',
            VLRMRGBRTCAL = 0.0,
            VLRMRGBRTOCD = 0.0,
            VLRMRGBRTRLZ = 0.0,
            VLRRCTLIQAPUCAL = 0.0,
            VLRRCTLIQAPUOCD = 0.0,
            VLRRCTLIQAPURLZ = 0.0,
            VLRCMVCAL = 0.0,
            VLRMCDCAL = 0.0,
            VLRMCDOCD = 0.0,
            VLRPCOBSECAL = 0.0,
            VLRPCOBSEOCD = 0.0,
            VLRPCOBSEMER = 0.0,
            VLRVNDLIQOCD = 0.0,
            VLRVNDLIQCAL = 0.0,
            VLRVNDLIQRLZ = 0.0,

        )
        self.assertTrue(isinstance(otimizador, models.Otimizador))
        self.assertTrue(isinstance(otimizador.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(otimizador.CODFILEPD,
                                   models.RelacionamentoFilialRegiao))
