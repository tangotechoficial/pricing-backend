from django.db import models

#ESTADO
class Mercadoria(models.Model):
    codmer = models.IntegerField()
    desmer = models.CharField(max_length=30)

#CAMPO
class Campo(models.Model):
    codcpofrmseqacs = models.CharField(primary_key=True, max_length=20)
    nomcpofrmseqacs = models.CharField(max_length=50)
    codfnc = models.IntegerField()
    datcad = models.DateField()
    datultatl = models.DateField()
    datdst = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadedefrmseqacs'

#SEQUENCIA
class Sequencia(models.Model):
    codseqacspco = models.CharField(primary_key=True, max_length=20)
    nomseqacspco = models.CharField(max_length=150)
    codfnc = models.IntegerField()
    datcad = models.DateField()
    datultatl = models.DateField()
    datdst = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadseqacspcodin'

#CAMPO_SEQUENCIA
class CampoSequencia(models.Model):
    codseqacspco = models.CharField(primary_key=True, max_length=20)
    codcpofrmseqacs = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rlcseqacsedefrm'
        unique_together = (('codseqacspco', 'codcpofrmseqacs'),)

#SEQUENCIA CONDICAO RELATIONSHIP
class SequenciaCondicao(models.Model):
    codseqacspco = models.CharField(primary_key=True, max_length=20)
    codcndpcodin = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rlcseqacscndpco'
        unique_together = (('codseqacspco', 'codcndpcodin'),)

#TIPOVALOR
class TipoValor(models.Model):
    codtipvlrpcodin = models.CharField(primary_key=True, max_length=20)
    nomtipvlrpcodin = models.CharField(max_length=60)
    codfnc = models.IntegerField()
    datcad = models.DateField()
    datultatl = models.DateField()
    datdst = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadtipvlrcndpcodin'

#CAMADA
class Camada(models.Model):
    codcampcodin = models.CharField(primary_key=True, max_length=20)
    nomcampcodin = models.CharField(max_length=60)
    tipcampcodin = models.CharField(max_length=4)
    codfnc = models.IntegerField()
    datcad = models.DateField()
    datultatl = models.DateField()
    datdst = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadcampcodin'

#CONDICAO
class Condicao(models.Model):
    codcndpcodin = models.CharField(primary_key=True, max_length=20)
    descndpcodin = models.CharField(max_length=50)
    codcampcodin = models.CharField(max_length=20)
    codtipvlrpcodin = models.CharField(max_length=20)
    vlrescqdepcodin = models.IntegerField()
    tipptvnegcndpcodin = models.CharField(max_length=4)
    tipbsevndcndpcodin = models.CharField(max_length=4)
    indcndprrpcodin = models.IntegerField()
    indinfetapcodin = models.IntegerField()
    codfnc = models.IntegerField()
    datcad = models.DateField()
    datultatl = models.DateField()
    datdst = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadcndpcodin'

#ESQUEMA DE CALCULO
class EsquemaDeCalculo(models.Model):
    codschcalpcodin = models.CharField(primary_key=True, max_length=30)
    tipschcalpcodin = models.CharField(max_length=4)
    codfnc = models.IntegerField()
    datcad = models.DateField()
    datultatl = models.DateField()
    datdst = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadschcalpcodin'

#CONDICAO CAMADA ESQUEMA
class CondicaoCamadaEsquema(models.Model):
    codcndpcodin = models.CharField(primary_key=True, max_length=20)
    codcampcodin = models.CharField(max_length=20)
    codschcalpcodin = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'rlccndcamschpcodin'
        unique_together = (('codcndpcodin', 'codcampcodin', 'codschcalpcodin'),)

#PRECO
class Preco(models.Model):
    codchvpcodin = models.CharField(primary_key=True, max_length=20)
    datrefpcodin = models.DateField()
    codschcalpcodin = models.CharField(max_length=30)
    vlruntpco = models.DecimalField(max_digits=15, decimal_places=2)
    tipfrmcalpcodin = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'cadpcodin'

#ESQUEMA CHAVE
class EsquemaChave(models.Model):
    codschcalpcodin = models.CharField(primary_key=True, max_length=30)
    codchvpcodin = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rlcschcalchvpcodin'
        unique_together = (('codschcalpcodin', 'codchvpcodin'),)