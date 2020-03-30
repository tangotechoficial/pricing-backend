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

    """
		verifica se o objeto criado é uma instância da classe desejada

	"""

    def test_criacao_de_instancia_fornecedor(self):
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        self.assertTrue(isinstance(fornecedor, models.Fornecedor))
        self.assertTrue(hasattr(fornecedor, 'CODDIVFRN'))
        self.assertTrue(hasattr(fornecedor, 'DESDIVFRN'))
        self.assertTrue(hasattr(fornecedor, 'CODGRPECOFRN'))
        self.assertTrue(hasattr(fornecedor, 'NOMGRPECOFRN'))


class CompradorTest(TestCase):
    databases = '__all__'
    """
		cria uma instância de COMPRADOR
	"""

    def create_comprador(self):
        return models.Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )

    """

	verifica uma instância de comprador

	"""

    def test_criacao_de_instancia_de_comprador(self):
        comprador = self.create_comprador()
        self.assertTrue(isinstance(comprador, models.Comprador))


class FilialTest(TestCase):

    """

    cria uma instância de Relacionamento Filial Região

    """

    def create_filial(self):
        return models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )

    """
		verifica se o objeto criado é uma instância da classe desejada

	"""

    def test_criacao_de_filial(self):
        filial = self.create_filial()
        self.assertTrue(isinstance(filial, models.RelacionamentoFilialRegiao))


class TabAuxGrpTeste(TestCase):
    def test_criacao_de_grupo(self):
        grupo = models.TabAuxGrp.objects.create(
            Id_Aux=1,
            CODSUBCTGPRD=1,
            DESSUBCTGPRD='teste',
            CODCTGPRD=1,
            DESCTGPRD='teste',
            CODGRPPRD=1,
            DESGRPPRD='teste',
            Linha_de_negocio='teste',
        )

        self.assertTrue(isinstance(grupo, models.TabAuxGrp))


"""
 teste do model Mercadoria

"""


class MercadoriaTest(TestCase):
    def test_cria_mercadoria(self):
        grupo = models.TabAuxGrp.objects.create(
            Id_Aux=1,
            CODSUBCTGPRD=1,
            DESSUBCTGPRD='teste',
            CODCTGPRD=1,
            DESCTGPRD='teste',
            CODGRPPRD=1,
            DESGRPPRD='teste',
            Linha_de_negocio='teste',
        )
        comprador = models.Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODPRD=1,
            # Id_Aux = instance.grupo.set(grupo),
            DESPRD='teste',
            CODDIVFRN=fornecedor,
            CODCPRATU=comprador,
            CODFIL=filial,
            CODSML=1,
            dessml='teste',
            ABC='1'
        )
        self.assertTrue(isinstance(mercadoria, models.Mercadoria))
        self.assertTrue(isinstance(mercadoria.CODDIVFRN, models.Fornecedor))
        self.assertTrue(isinstance(mercadoria.CODCPRATU, models.Comprador))
        self.assertTrue(isinstance(mercadoria.CODCPRATU, models.Comprador))


class DadosMestreVerba(TestCase):

    """

    cria uma instância de dados_mestre_verba

    """

    def create_dados_mestre_verba(self):
        comprador = models.Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODPRD=1,
            # Id_Aux = instance.grupo.set(grupo),
            DESPRD='teste',
            CODDIVFRN=fornecedor,
            CODCPRATU=comprador,
            CODFIL=filial,
            CODSML=1,
            dessml='teste',
            ABC='1'
        )
        return models.DadosMestre_Verba.objects.create(CODPRD=mercadoria, NUMANOMES='135', CODFILEPD=filial, CODDIVFRN=23, VLRPRECOSALDOMESANTERIOR=12, VLRPRECOCREDITO=23, VLRMARGEMSALDOMESANTERIOR=17,
                                                VLRPRECODEBITO=24, VLRMARGEMCREDITO=76, VLRMARGEMDEBITO=13)

    """
		verifica se o objeto criado é uma instância da classe desejada

	"""

    def test_criacao_de_model_verba(self):
        dado = self.create_dados_mestre_verba()
        self.assertTrue(isinstance(dado, models.DadosMestre_Verba))
        self.assertTrue(isinstance(dado.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(dado.CODFILEPD, models.RelacionamentoFilialRegiao))


class DadosMestreComposicaoPrecoTest(TestCase):
    """

    cria uma instância de dados_mestre_composicao_de_preco

    """

    def create_dados_mestre_composicao_preco(self):
        comprador = models.Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODPRD=1,
            # Id_Aux = instance.grupo.set(grupo),
            DESPRD='teste',
            CODDIVFRN=fornecedor,
            CODCPRATU=comprador,
            CODFIL=filial,
            CODSML=1,
            dessml='teste',
            ABC='1'
        )
        return models.DadosMestre_ComposicaoPreco.objects.create(CODPRD=mercadoria, SENSIVEL_REBATE=123, TIPEDEREG=12, CODEDEREG=10, CODFILEMP=filial,
                                                          CODFILFAT=12, FLEX=13, DATA_PRECO=make_aware(datetime.now()))

    """

    verifica se o objeto criado pertence à instância desejada

    """
    def test_criacao_de_model_composicao_preco(self):
        dado = self.create_dados_mestre_composicao_preco()
        self.assertTrue(isinstance(dado, models.DadosMestre_ComposicaoPreco))
        self.assertTrue(isinstance(dado.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(dado.CODFILEMP, models.RelacionamentoFilialRegiao))


class PlanoDeCompras(TestCase):
    """
        cria uma instância de PlanoCompras

    """

    def create_plano_de_compras(self):
        comprador = models.Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODPRD=1,
            # Id_Aux = instance.grupo.set(grupo),
            DESPRD='teste',
            CODDIVFRN=fornecedor,
            CODCPRATU=comprador,
            CODFIL=filial,
            CODSML=1,
            dessml='teste',
            ABC='1'
        )
        return models.PlanoCompras.objects.create(CODPRD=mercadoria, CODFILEMP=filial, CODFILFAT=12, DATA_PRECO=make_aware(datetime.now()), CODESTUNI=2, SEMANA=1)

    """
	verifica se o objeto criado é uma instância da classe desejada
	checa as propriedades existentes na instância

    """

    def test_criacao_de_model_plano_compras(self):
        dado = self.create_plano_de_compras()

        self.assertTrue(isinstance(dado, models.PlanoCompras))
        self.assertTrue(isinstance(dado.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(dado.CODFILEMP, models.RelacionamentoFilialRegiao))


"""
testa model de elasticidade

"""


class ElasticidadeTest(TestCase):

    def test_instancia_elasticidade(self):
        comprador = models.Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODPRD=1,
            # Id_Aux = instance.grupo.set(grupo),
            DESPRD='teste',
            CODDIVFRN=fornecedor,
            CODCPRATU=comprador,
            CODFIL=filial,
            CODSML=1,
            dessml='teste',
            ABC='1'
        )
        elasticidade = models.Elasticidade.objects.create(
            codsml=mercadoria,
            uf='oo',
            Elasticidade=0.00,
            qt=1,
            pcmed=0.00,
            unitfnd=0.00,
            verba=0.00
        )
        """

		verifica instâncias do item e de suas chaves estrangeiras

		"""
        self.assertTrue(isinstance(elasticidade, models.Elasticidade))
        self.assertTrue(isinstance(elasticidade.codsml, models.Mercadoria))


"""
teste do model Estoque

"""


class EstoqueTest(TestCase):
    def test_estoque(self):
        comprador = models.Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODPRD=1,
            # Id_Aux = instance.grupo.set(grupo),
            DESPRD='teste',
            CODDIVFRN=fornecedor,
            CODCPRATU=comprador,
            CODFIL=filial,
            CODSML=1,
            dessml='teste',
            ABC='1'
        )
        estoque = models.Estoque.objects.create(
            CODPRD=mercadoria,
            CODFIL=filial,
            DATINI=make_aware(datetime.now()),
            NUMSMNANO=make_aware(datetime.now()),
            NOMSMSANO=make_aware(datetime.now()),
            NOMDIASMN=make_aware(datetime.now()),
            NUMDIASMN=make_aware(datetime.now()),
            NOMABVMESANO='teste',
            VLRUNTCSTSCO=0.00,
            QDEITEETQ=1,
            VLRVNDPDAFLTETQ=0.00,
            QDEMEDVNDMNSMER=1,
            VLRCSTCMPIDL=0.00,
            VLRMEDPCOCMP=0.00,
            CODSTAPRDETQ=1,
            DESSTAPRDETQ='teste',
            CODUNDREG=1,
            DESUNDREG='teste',
            FLGUNDREG='teste'

        )
        self.assertTrue(isinstance(estoque, models.Estoque))
        self.assertTrue(isinstance(estoque.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(estoque.CODFIL, models.RelacionamentoFilialRegiao))


"""

teste do model Competitividade

"""


class CompetitividadeTest(TestCase):
    def test_competitividade(self):
        comprador = models.Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODPRD=1,
            # Id_Aux = instance.grupo.set(grupo),
            DESPRD='teste',
            CODDIVFRN=fornecedor,
            CODCPRATU=comprador,
            CODFIL=filial,
            CODSML=1,
            dessml='teste',
            ABC='1'
        )
        competitividade = models.Competitividade.objects.create(
            CODPRD=mercadoria,
            estado='SP',
            NUMANOMES=make_aware(datetime.now()),
            NUMSMNANO=make_aware(datetime.now()),
            data_emissao=make_aware(datetime.now()),
            TipoPesquisa='teste',
            pc_mrt=0.00,
            pc_psq=0.00,
            Comp=0.00,
            pc_psq_pond=0.00,
            pc_mrt_pond=0.00,
            regiao='teste',
            Uf_Destino='RJ',
            ABC='1'
        )

        self.assertTrue(isinstance(competitividade, models.Competitividade))
        self.assertTrue(isinstance(competitividade.CODPRD, models.Mercadoria))


"""

teste do model Representante

"""


class RepresentanteTest(TestCase):
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
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODPRD=1,
            # Id_Aux = instance.grupo.set(grupo),
            DESPRD='teste',
            CODDIVFRN=fornecedor,
            CODCPRATU=comprador,
            CODFIL=filial,
            CODSML=1,
            dessml='teste',
            ABC='1'
        )
        representante = models.Representante.objects.create(
            CODREPCMC=1,
            NOMREPCMC='teste',
            DATCADREPCMC=make_aware(datetime.now())
        )
        vendas = models.Vendas.objects.create(
            CODPRD=mercadoria,
            CODFILEPD=filial,
            CODFILFAT=0,
            CODESTCLI=0,
            CODREPCMC=representante,
            NUMPED=0,
            NUMANOMESSMN=make_aware(datetime.now()),
            NUMANOMESDIA=make_aware(datetime.now()),
            CMV=0.00,
            QDEITE=0.00,
            VLRVNDLIQ=0.00,
            MARGEM_CONTRIBUICAO=0.00,
            MARGEM_BRUTA=0.00,
            VLRRCTLIQ=0.00,
            VLRIMPTOT=0.00,
            TRANSFERENCIA=0.00,
            DISTRIBUICAO=0.00,
            ARMAZENAGEM=0.00,
            FUNDING=0.00,
            VLRSUPFLX=0.00,
            VLRDSCFLXCNS=0.00,
            Despesas_Financeiras=0.00,
            Margem_por_Segmento=0.00,
        )
        self.assertTrue(isinstance(vendas, models.Vendas))
        self.assertTrue(isinstance(vendas.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(vendas.CODFILEPD,
                                   models.RelacionamentoFilialRegiao))
        self.assertTrue(isinstance(vendas.CODREPCMC, models.Representante))


"""
teste do model VerbaeBC

"""


class VerbaeBCTest(TestCase):
    def test_verba_e_bc(self):
        comprador = models.Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODPRD=1,
            # Id_Aux = instance.grupo.set(grupo),
            DESPRD='teste',
            CODDIVFRN=fornecedor,
            CODCPRATU=comprador,
            CODFIL=filial,
            CODSML=1,
            dessml='teste',
            ABC='1'
        )
        verba = models.VerbaeBC.objects.create(
            CODPRD=mercadoria,
            CODFILEPD=filial,
            CODFILFAT=1,
            CODESTCLI=1,
            NUMANOMESDIA=make_aware(datetime.now()),
            QUANTIDADE_ITENS_PEDIDO=1,
            VALOR_TOTAL_VENDA_LIQUIDA=0.00,
            VALOR_UNITARIO_CMV=0.00,
            VALOR_TOTAL_CMV=0.00,
            VALOR_UNITARIO_FUNDING=0.00,
            VALOR_TOTAL_FUNDING=0.00,
            QUANTIDADE_ITENS_PROMOCAO=1,
            QUANTIDADE_ITENS_BENEFICIO=1,
            VALOR_UNITARIO_PROMOCAO=0.00,
            VALOR_UNITARIO_BENEFICIO=0.00,
            VALOR_UNITARIO_FUNDING_PRECO=0.00,
            VALOR_UNITARIO_FUNDING_MARGEM=0.00,
            VALOR_TOTAL_PROMOCAO=0.00,
            VALOR_TOTAL_BENEFICIO=0.00,
            VALOR_TOTAL_FUNDING_PRECO=0.00,
            VALOR_TOTAL_FUNDING_MARGEM=0.00,
            VALOR_TOTAL_DMS_SANSUNG=0.00,
            REBATE=0.00,
        )
        self.assertTrue(isinstance(verba, models.VerbaeBC))
        self.assertTrue(isinstance(verba.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(verba.CODFILEPD,
                                   models.RelacionamentoFilialRegiao))


"""

teste do model Diretriz Estratégica

"""


class DiretrizesEstrategicaTeste(TestCase):
    def test_diretriz_estrategica(self):
        grupo = models.TabAuxGrp.objects.create(
            Id_Aux=1,
            CODSUBCTGPRD=1,
            DESSUBCTGPRD='teste',
            CODCTGPRD=1,
            DESCTGPRD='teste',
            CODGRPPRD=1,
            DESGRPPRD='teste',
            Linha_de_negocio='teste',
        )
        diretriz_estrategica = models.DiretrizesEstrategica.objects.create(
            Id_Aux=grupo,
            DATINI=make_aware(datetime.now()),
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            NOMFNCCPRATU='teste',
            CODGRPPRD=1,
            DESGRPPRD='teste',
            CODCTGPRD=1,
            DESCTGPRD='teste',
            CODSUBCTGPRD=1,
            DESSUBCTGPRD='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste',
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODESTUNI='000',
            NOMESTUNI='teste',
            VLRVNDFATLIQ='teste',
            VLRMRGBRT='teste',
            NOMREGGEO='teste',
        )
        self.assertTrue(isinstance(
            diretriz_estrategica, models.DiretrizesEstrategica))
        self.assertTrue(isinstance(diretriz_estrategica.Id_Aux, models.TabAuxGrp))


"""

teste do model Otimizador

"""


class OtimizadorTest(TestCase):
    def test_otimmizador_instances(self):
        comprador = models.Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = models.RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = models.Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = models.Mercadoria.objects.create(
            CODPRD=1,
            # Id_Aux = instance.grupo.set(grupo),
            DESPRD='teste',
            CODDIVFRN=fornecedor,
            CODCPRATU=comprador,
            CODFIL=filial,
            CODSML=1,
            dessml='teste',
            ABC='1'
        )
        otimizador = models.Otimizador.objects.create(
            DATA_PRECO=make_aware(datetime.now()),
            CODPRD=mercadoria,
            CODFILEMP=filial,
            CODFILFAT=0,
            CODESTUNI=0,
            VERBA_OTIMIZADA=0.00,
            VERBA_INPUT=0.00,
            VERBA_NECESSARIA=0.00,
            VERBA_DISPONIVEL=0.00,

        )
        self.assertTrue(isinstance(otimizador, models.Otimizador))
        self.assertTrue(isinstance(otimizador.CODPRD, models.Mercadoria))
        self.assertTrue(isinstance(otimizador.CODFILEMP,
                                   models.RelacionamentoFilialRegiao))

