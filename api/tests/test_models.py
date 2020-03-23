from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from api.models import DadosMestre_ComposicaoPreco, DadosMestre_Verba, PlanoCompras, Mercadoria, Fornecedor, Comprador, RelacionamentoFilialRegiao, TabAuxGrp, Elasticidade, Estoque, Competitividade, Representante, Vendas, VerbaeBC, DiretrizesEstrategica, Otimizador
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
        fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        self.assertTrue(isinstance(fornecedor, Fornecedor))
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
        return Comprador.objects.create(
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
        self.assertTrue(isinstance(comprador, Comprador))


class FilialTest(TestCase):

    """

    cria uma instância de Relacionamento Filial Região

    """

    def create_filial(self):
        return RelacionamentoFilialRegiao.objects.create(
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
        self.assertTrue(isinstance(filial, RelacionamentoFilialRegiao))


class TabAuxGrpTeste(TestCase):
    def test_criacao_de_grupo(self):
        grupo = TabAuxGrp.objects.create(
            Id_Aux=1,
            CODSUBCTGPRD=1,
            DESSUBCTGPRD='teste',
            CODCTGPRD=1,
            DESCTGPRD='teste',
            CODGRPPRD=1,
            DESGRPPRD='teste',
            Linha_de_negocio='teste',
        )

        self.assertTrue(isinstance(grupo, TabAuxGrp))


"""
 teste do model Mercadoria

"""


class MercadoriaTest(TestCase):
    def test_cria_mercadoria(self):
        grupo = TabAuxGrp.objects.create(
            Id_Aux=1,
            CODSUBCTGPRD=1,
            DESSUBCTGPRD='teste',
            CODCTGPRD=1,
            DESCTGPRD='teste',
            CODGRPPRD=1,
            DESGRPPRD='teste',
            Linha_de_negocio='teste',
        )
        comprador = Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = Mercadoria.objects.create(
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
        self.assertTrue(isinstance(mercadoria, Mercadoria))
        self.assertTrue(isinstance(mercadoria.CODDIVFRN, Fornecedor))
        self.assertTrue(isinstance(mercadoria.CODCPRATU, Comprador))
        self.assertTrue(isinstance(mercadoria.CODCPRATU, Comprador))


class DadosMestreVerba(TestCase):

    """

    cria uma instância de dados_mestre_verba

    """

    def create_dados_mestre_verba(self):
        comprador = Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = Mercadoria.objects.create(
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
        return DadosMestre_Verba.objects.create(CODPRD=mercadoria, NUMANOMES='135', CODFILEPD=filial, CODDIVFRN=23, VLRPRECOSALDOMESANTERIOR=12, VLRPRECOCREDITO=23, VLRMARGEMSALDOMESANTERIOR=17,
                                                VLRPRECODEBITO=24, VLRMARGEMCREDITO=76, VLRMARGEMDEBITO=13)

    """
		verifica se o objeto criado é uma instância da classe desejada

	"""

    def test_criacao_de_model_verba(self):
        dado = self.create_dados_mestre_verba()
        self.assertTrue(isinstance(dado, DadosMestre_Verba))
        self.assertTrue(isinstance(dado.CODPRD, Mercadoria))
        self.assertTrue(isinstance(dado.CODFILEPD, RelacionamentoFilialRegiao))


class DadosMestreComposicaoPrecoTest(TestCase):
    """

    cria uma instância de dados_mestre_composicao_de_preco

    """

    def create_dados_mestre_composicao_preco(self):
        comprador = Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = Mercadoria.objects.create(
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
        return DadosMestre_ComposicaoPreco.objects.create(CODPRD=mercadoria, SENSIVEL_REBATE=123, TIPEDEREG=12, CODEDEREG=10, CODFILEMP=filial,
                                                          CODFILFAT=12, FLEX=13, DATA_PRECO=make_aware(datetime.now()))

    # verifica se o objeto criado é uma instância da classe desejada
    def test_criacao_de_model_composicao_preco(self):
        dado = self.create_dados_mestre_composicao_preco()
        self.assertTrue(isinstance(dado, DadosMestre_ComposicaoPreco))
        self.assertTrue(isinstance(dado.CODPRD, Mercadoria))
        self.assertTrue(isinstance(dado.CODFILEMP, RelacionamentoFilialRegiao))


class PlanoDeCompras(TestCase):
    """
        cria uma instância de PlanoCompras

    """

    def create_plano_de_compras(self):
        comprador = Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
        filial = RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
        fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
        mercadoria = Mercadoria.objects.create(
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
        return PlanoCompras.objects.create(CODPRD=mercadoria, CODFILEMP=filial, CODFILFAT=12, DATA_PRECO=make_aware(datetime.now()), CODESTUNI=2, SEMANA=1)

    """
		verifica se o objeto criado é uma instância da classe desejada
		checa as propriedades existentes na instância

		"""

    def test_criacao_de_model_plano_compras(self):
        dado = self.create_plano_de_compras()

        self.assertTrue(isinstance(dado, PlanoCompras))
        self.assertTrue(isinstance(dado.CODPRD, Mercadoria))
        self.assertTrue(isinstance(dado.CODFILEMP, RelacionamentoFilialRegiao))

"""
testa model de elasticidade

"""


class ElasticidadeTest(TestCase):

		def test_instancia_elasticidade(self):
				comprador = Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
				filial = RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
				fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
				mercadoria = Mercadoria.objects.create(
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
				elasticidade = Elasticidade.objects.create(
								codsml = mercadoria,
								uf = 'oo',
								Elasticidade = 0.00,
								qt = 1,
								pcmed = 0.00,
								unitfnd = 0.00,
								verba = 0.00
				)
				"""

				verifica instâncias do item e de suas chaves estrangeiras

				"""
				self.assertTrue(isinstance(elasticidade, Elasticidade))
				self.assertTrue(isinstance(elasticidade.codsml, Mercadoria))

"""
teste do model Estoque

"""

class EstoqueTest(TestCase):
	def test_estoque(self):
				comprador = Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
				filial = RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
				fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
				mercadoria = Mercadoria.objects.create(
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
				estoque = Estoque.objects.create(
					  CODPRD = mercadoria,
						CODFIL = filial,
						DATINI = make_aware(datetime.now()),
						NUMSMNANO = make_aware(datetime.now()),
						NOMSMSANO = make_aware(datetime.now()),
						NOMDIASMN = make_aware(datetime.now()),
						NUMDIASMN = make_aware(datetime.now()),
						NOMABVMESANO = 'teste',
						VLRUNTCSTSCO = 0.00,
						QDEITEETQ = 1,
						VLRVNDPDAFLTETQ = 0.00,
						QDEMEDVNDMNSMER = 1,
						VLRCSTCMPIDL = 0.00,
						VLRMEDPCOCMP = 0.00,
						CODSTAPRDETQ = 1,
						DESSTAPRDETQ = 'teste',
						CODUNDREG = 1,
						DESUNDREG = 'teste',
						FLGUNDREG = 'teste'

				)
				self.assertTrue(isinstance(estoque, Estoque))
				self.assertTrue(isinstance(estoque.CODPRD, Mercadoria))
				self.assertTrue(isinstance(estoque.CODFIL, RelacionamentoFilialRegiao))

"""

teste do model Competitividade

"""


class CompetitividadeTest(TestCase):
	def test_competitividade(self):
				comprador = Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
				filial = RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
				fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
				mercadoria = Mercadoria.objects.create(
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
				competitividade = Competitividade.objects.create(
						CODPRD = mercadoria,
						estado = 'SP',
						NUMANOMES = make_aware(datetime.now()),
						NUMSMNANO = make_aware(datetime.now()),
						data_emissao = make_aware(datetime.now()),
						TipoPesquisa = 'teste',
						pc_mrt = 0.00,
						pc_psq = 0.00,
						Comp = 0.00,
						pc_psq_pond = 0.00,
						pc_mrt_pond = 0.00,
						regiao = 'teste',
						Uf_Destino = 'RJ',
						ABC = '1'
				)

				self.assertTrue(isinstance(competitividade, Competitividade))
				self.assertTrue(isinstance(competitividade.CODPRD, Mercadoria))

"""

teste do model Representante

"""

class RepresentanteTest(TestCase):
		def test_representante(self):
				representante = Representante.objects.create(
						CODREPCMC = 1,
						NOMREPCMC = 'teste',
						DATCADREPCMC = make_aware(datetime.now())
				)
				self.assertTrue(representante, Representante)


"""

teste da classe Vendas 

"""

class VendasTest(TestCase):
		def test_vendas(self):
				comprador = Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
				filial = RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
				fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
				mercadoria = Mercadoria.objects.create(
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
				representante = Representante.objects.create(
						CODREPCMC = 1,
						NOMREPCMC = 'teste',
						DATCADREPCMC = make_aware(datetime.now())
				)
				vendas = Vendas.objects.create(
						CODPRD = mercadoria,
						CODFILEPD = filial,
						CODFILFAT = 0,
						CODESTCLI = 0,
						CODREPCMC = representante,
						NUMPED = 0,
						NUMANOMESSMN = make_aware(datetime.now()),
						NUMANOMESDIA = make_aware(datetime.now()),
						CMV = 0.00,
						QDEITE = 0.00,
						VLRVNDLIQ = 0.00,
						MARGEM_CONTRIBUICAO = 0.00,
						MARGEM_BRUTA = 0.00,
						VLRRCTLIQ = 0.00,
						VLRIMPTOT = 0.00,
						TRANSFERENCIA = 0.00,
						DISTRIBUICAO = 0.00,
						ARMAZENAGEM = 0.00,
						FUNDING = 0.00,
						VLRSUPFLX = 0.00,
						VLRDSCFLXCNS = 0.00,
						Despesas_Financeiras = 0.00,
						Margem_por_Segmento = 0.00,
				)
				self.assertTrue(isinstance(vendas, Vendas))
				self.assertTrue(isinstance(vendas.CODPRD, Mercadoria))
				self.assertTrue(isinstance(vendas.CODFILEPD, RelacionamentoFilialRegiao))
				self.assertTrue(isinstance(vendas.CODREPCMC, Representante))

"""
teste do model VerbaeBC

"""

class VerbaeBCTest(TestCase):
		def test_verba_e_bc(self):
				comprador = Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
				filial = RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
				fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
				mercadoria = Mercadoria.objects.create(
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
				verba = VerbaeBC.objects.create(
						CODPRD = mercadoria,
						CODFILEPD = filial,
						CODFILFAT = 1,
						CODESTCLI = 1,
						NUMANOMESDIA = make_aware(datetime.now()),
						QUANTIDADE_ITENS_PEDIDO = 1,
						VALOR_TOTAL_VENDA_LIQUIDA = 0.00,
						VALOR_UNITARIO_CMV = 0.00,
						VALOR_TOTAL_CMV = 0.00,
						VALOR_UNITARIO_FUNDING = 0.00,
						VALOR_TOTAL_FUNDING = 0.00,
						QUANTIDADE_ITENS_PROMOCAO = 1,
						QUANTIDADE_ITENS_BENEFICIO = 1,
						VALOR_UNITARIO_PROMOCAO = 0.00,
						VALOR_UNITARIO_BENEFICIO = 0.00,
						VALOR_UNITARIO_FUNDING_PRECO = 0.00,
						VALOR_UNITARIO_FUNDING_MARGEM = 0.00,
						VALOR_TOTAL_PROMOCAO = 0.00,
						VALOR_TOTAL_BENEFICIO = 0.00,
						VALOR_TOTAL_FUNDING_PRECO = 0.00,
						VALOR_TOTAL_FUNDING_MARGEM = 0.00,
						VALOR_TOTAL_DMS_SANSUNG = 0.00,
						REBATE = 0.00,
				)
				self.assertTrue(isinstance(verba, VerbaeBC))
				self.assertTrue(isinstance(verba.CODPRD, Mercadoria))
				self.assertTrue(isinstance(verba.CODFILEPD, RelacionamentoFilialRegiao))


"""

teste do model Diretriz Estratégica

"""

class DiretrizesEstrategicaTeste(TestCase):
		def test_diretriz_estrategica(self):
				grupo = TabAuxGrp.objects.create(
						Id_Aux=1,
						CODSUBCTGPRD=1,
						DESSUBCTGPRD='teste',
						CODCTGPRD=1,
						DESCTGPRD='teste',
						CODGRPPRD=1,
						DESGRPPRD='teste',
						Linha_de_negocio='teste',
				)
				diretriz_estrategica = DiretrizesEstrategica.objects.create(
						Id_Aux = grupo,
						DATINI = make_aware(datetime.now()),
						CODDRTCLLATU = 1,
						DESDRTCLLATU = 'teste',
						CODCLLCMPATU = 1,
						DESCLLCMPATU = 'teste',
						NOMFNCCPRATU = 'teste',
						CODGRPPRD = 1,
						DESGRPPRD = 'teste',
						CODCTGPRD = 1,
						DESCTGPRD = 'teste',
						CODSUBCTGPRD = 1,
						DESSUBCTGPRD = 'teste',
						CODGRPECOFRN = 1,
						NOMGRPECOFRN = 'teste',
						CODDIVFRN = 1,
						DESDIVFRN = 'teste',
						CODESTUNI = '000',
						NOMESTUNI = 'teste',
						VLRVNDFATLIQ = 'teste',
						VLRMRGBRT = 'teste',
						NOMREGGEO = 'teste',
				)
				self.assertTrue(isinstance(diretriz_estrategica, DiretrizesEstrategica))
				self.assertTrue(isinstance(diretriz_estrategica.Id_Aux, TabAuxGrp))

"""

teste do model Otimizador

"""
class OtimizadorTest(TestCase):
		def test_otimmizador_instances(self):
				comprador = Comprador.objects.create(
            CODCPRATU=1,
            NOMCPRATU='teste',
            CODCLLCMPATU=1,
            DESCLLCMPATU='teste',
            CODDRTCLLATU=1,
            DESDRTCLLATU='teste'
        )
				filial = RelacionamentoFilialRegiao.objects.create(
            CODFILEPD=1,
            NOMFILEPD='teste',
            CODFILFAT=1,
            NOMFILFAT='teste',
            CODESTUNI='SP',
            NOMESTUNI='teste',
            TIPEDEREG=1,
            CODEDEREG=1
        )
				fornecedor = Fornecedor.objects.create(
            CODDIVFRN=1,
            DESDIVFRN='teste',
            CODGRPECOFRN=1,
            NOMGRPECOFRN='teste'
        )
				mercadoria = Mercadoria.objects.create(
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
				otimizador = Otimizador.objects.create(
						DATA_PRECO = make_aware(datetime.now()),
						CODPRD = mercadoria,
						CODFILEMP = filial,
						CODFILFAT = 0,
						CODESTUNI = 0,
						VERBA_OTIMIZADA = 0.00,
						VERBA_INPUT = 0.00,
						VERBA_NECESSARIA = 0.00,
						VERBA_DISPONIVEL = 0.00,

				)
				self.assertTrue(isinstance(otimizador, Otimizador))
				self.assertTrue(isinstance(otimizador.CODPRD, Mercadoria))
				self.assertTrue(isinstance(otimizador.CODFILEMP, RelacionamentoFilialRegiao))





