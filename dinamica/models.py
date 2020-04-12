from django.db import models

class Camada(models.Model):
    cod_camada = models.CharField(primary_key=True, max_length=10)
    nome_camada = models.CharField(max_length=50)
    tipo_base_vendas = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'CAMADA'


class Campo(models.Model):
    cod_campo = models.CharField(primary_key=True, max_length=10)
    nome_campo = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'CAMPO'


class CampoSequencia(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    cod_campo = models.ForeignKey(Campo, models.DO_NOTHING, db_column='cod_campo', blank=True, null=True)
    cod_sequencia = models.ForeignKey('Sequencia', models.DO_NOTHING, db_column='cod_sequencia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CAMPO_SEQUENCIA'


class ChaveContas(models.Model):
    cod_chavecontas = models.CharField(primary_key=True, max_length=10)
    desc_chavecontas = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'CHAVE_CONTAS'


class Condicao(models.Model):
    cod_condicao = models.CharField(primary_key=True, max_length=10)
    desc_condicao = models.CharField(max_length=30)
    cod_camada = models.ForeignKey(Camada, models.DO_NOTHING, db_column='cod_camada')
    cod_chavecontas = models.ForeignKey(ChaveContas, models.DO_NOTHING, db_column='cod_chavecontas', null=True, blank=True)
    cod_tipovalor = models.ForeignKey('TipoValor', models.DO_NOTHING, db_column='cod_tipovalor')
    escala_qtde = models.IntegerField()
    pos_neg = models.CharField(max_length=1)
    tip_base_vendas = models.CharField(max_length=1)
    mandatoria = models.IntegerField()
    estatistica = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CONDICAO'


class CondicaoCamadaEsquema(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    cod_esquema_calculo = models.CharField(max_length=10, blank=True, null=True)
    cod_condicao = models.CharField(max_length=10)
    cod_camada = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'CONDICAO_CAMADA_ESQUEMA'


class EsquemaDeCalculo(models.Model):
    cod_esquema_calculo = models.CharField(primary_key=True, max_length=10)
    tipo_base_vendas = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ESQUEMA_DE_CALCULO'


class Sequencia(models.Model):
    cod_sequencia = models.CharField(primary_key=True, max_length=10)
    nome_sequencia = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'SEQUENCIA'


class SequenciaCondicao(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    cod_sequencia = models.ForeignKey(Sequencia, models.DO_NOTHING, db_column='cod_sequencia')
    cod_condicao = models.ForeignKey(Condicao, models.DO_NOTHING, db_column='cod_condicao')

    class Meta:
        managed = False
        db_table = 'SEQUENCIA_CONDICAO'


class TipoValor(models.Model):
    cod_tipovalor = models.CharField(primary_key=True, max_length=10)
    desc_tipovalor = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'TIPO_VALOR'

class FilialExpedicao(models.Model):
    codfilemp = models.IntegerField(primary_key=True)
    desfilemp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FILIAL_EXPEDICAO'

class FilialFaturamento(models.Model):
    codfilempfat = models.IntegerField(primary_key=True)
    desfilempfat = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FILIAL_FATURAMENTO'

class Estado(models.Model):
    codestuni = models.CharField(primary_key=True, max_length=2)
    desestuni = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ESTADO'

class Regiao(models.Model):
    codedereg = models.IntegerField(primary_key=True)
    codestuni = models.ForeignKey(Estado, models.DO_NOTHING, db_column='codestuni', blank=True, null=True)
    tipedereg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REGIAO'

class Mercadoria(models.Model):
    codprd = models.IntegerField(primary_key=True)
    desprd = models.CharField(max_length=50, blank=True, null=True)
    coddrtcllatu = models.IntegerField()
    desdrtcllatu = models.CharField(max_length=50, blank=True, null=True)
    codgrpprd = models.IntegerField()
    desgrpprd = models.CharField(max_length=50, blank=True, null=True)
    codclsprd = models.IntegerField()
    desclsprd = models.CharField(max_length=50, blank=True, null=True)
    codsubctgprd = models.IntegerField()
    dessubctgprd = models.CharField(max_length=50, blank=True, null=True)
    codsmr = models.IntegerField()
    dessmr = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MERCADORIA'

class ChavePrecificao(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    codmer = models.ForeignKey('Mercadoria', models.DO_NOTHING, db_column='codmer', blank=True, null=True)
    codfilemp = models.ForeignKey('FilialExpedicao', models.DO_NOTHING, db_column='codfilemp', blank=True, null=True)
    codfilempfat = models.ForeignKey('FilialFaturamento', models.DO_NOTHING, db_column='codfilempfat', blank=True, null=True)
    tipedereg = models.IntegerField(blank=True, null=True)
    codedereg = models.ForeignKey('Regiao', models.DO_NOTHING, db_column='codedereg', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CHAVE_PRECIFICAO'

class Preco(models.Model):
    id = models.IntegerField(primary_key=True)
    cod_esquema_calculo = models.ForeignKey(EsquemaDeCalculo, models.DO_NOTHING, db_column='cod_esquema_calculo', blank=True, null=True)
    tipo_base_vendas = models.CharField(max_length=1)
    datainicio = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    chave = models.ForeignKey(ChavePrecificao, models.DO_NOTHING, db_column='chave', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PRECO'

class CodterchvCodcnl(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    codterchv = models.CharField(max_length=10)
    codcnl = models.CharField(max_length=10)
    permrgadicnlvnd = models.IntegerField(blank=True, null=True)
    startdate = models.DateField()
    enddate = models.DateField()

    class Meta:
        managed = False
        db_table = 'CODTERCHV_CODCNL'