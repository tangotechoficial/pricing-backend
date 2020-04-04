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
    cod_campo = models.OneToOneField(Campo, models.DO_NOTHING, db_column='cod_campo', primary_key=True)
    cod_sequencia = models.ForeignKey('Sequencia', models.DO_NOTHING, db_column='cod_sequencia')

    class Meta:
        managed = False
        db_table = 'CAMPO_SEQUENCIA'
        unique_together = (('cod_campo', 'cod_sequencia'),)


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
    cod_chavecontas = models.ForeignKey(ChaveContas, models.DO_NOTHING, db_column='cod_chavecontas')
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
    cod_esquema_calculo = models.CharField(primary_key=True, max_length=10)
    cod_condicao = models.CharField(max_length=10)
    cod_camada = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'CONDICAO_CAMADA_ESQUEMA'
        unique_together = (('cod_esquema_calculo', 'cod_condicao', 'cod_camada'),)


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
    cod_sequencia = models.OneToOneField(Sequencia, models.DO_NOTHING, db_column='cod_sequencia', primary_key=True)
    cod_condicao = models.ForeignKey(Condicao, models.DO_NOTHING, db_column='cod_condicao')

    class Meta:
        managed = False
        db_table = 'SEQUENCIA_CONDICAO'
        unique_together = (('cod_sequencia', 'cod_condicao'),)


class TipoValor(models.Model):
    cod_tipovalor = models.CharField(primary_key=True, max_length=10)
    desc_tipovalor = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'TIPO_VALOR'