# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BasePreco(models.Model):
    tipedereg = models.BigIntegerField(db_column='TIPEDEREG', blank=True, null=True)  # Field name made lowercase.
    codedereg = models.BigIntegerField(db_column='CODEDEREG', blank=True, null=True)  # Field name made lowercase.
    codfilemp = models.BigIntegerField(db_column='CODFILEMP', blank=True, null=True)  # Field name made lowercase.
    codfilempfat = models.BigIntegerField(db_column='CODFILEMPFAT', blank=True, null=True)  # Field name made lowercase.
    codmer = models.BigIntegerField(db_column='CODMER', blank=True, null=True)  # Field name made lowercase.
    mb = models.FloatField(db_column='MB', blank=True, null=True)  # Field name made lowercase.
    mb_calculada = models.FloatField(db_column='MB_CALCULADA', blank=True, null=True)  # Field name made lowercase.
    verba_preco = models.FloatField(db_column='VERBA_PREÇO', blank=True, null=True)  # Field name made lowercase.
    fund_preco = models.BigIntegerField(db_column='FUND_PREÇO', blank=True, null=True)  # Field name made lowercase.
    rebate = models.FloatField(db_column='REBATE', blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    pis_cofins = models.FloatField(db_column='PIS_COFINS', blank=True, null=True)  # Field name made lowercase.
    devolucao = models.FloatField(db_column='DEVOLUÇÃO', blank=True, null=True)  # Field name made lowercase.
    target = models.FloatField(db_column='TARGET', blank=True, null=True)  # Field name made lowercase.
    flex = models.BigIntegerField(db_column='FLEX', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='CUSTO', blank=True, null=True)  # Field name made lowercase.
    numrlccidgir = models.BigIntegerField(db_column='NUMRLCCIDGIR', blank=True, null=True)  # Field name made lowercase.
    bonificado = models.FloatField(db_column='BONIFICADO', blank=True, null=True)  # Field name made lowercase.
    complemento = models.FloatField(db_column='COMPLEMENTO', blank=True, null=True)  # Field name made lowercase.
    precobase = models.BigIntegerField(db_column='PRECOBASE', blank=True, null=True)  # Field name made lowercase.
    data_preco = models.TextField(db_column='DATA_PREÇO', blank=True, null=True)  # Field name made lowercase.
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
    nomeregiao = models.TextField(db_column='NOMEREGIÃO', blank=True, null=True)  # Field name made lowercase.
    tipo_calculo_preco = models.TextField(db_column='TIPO_CALCULO_PREÇO', blank=True, null=True)  # Field name made lowercase.
    preco_livro = models.FloatField(db_column='PREÇO_LIVRO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BASE_PRECO'


# class Competitividade(models.Model):
#     #id = models.TextField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
#     chave = models.TextField(blank=True, null=True)
#     data_emissao = models.TextField(blank=True, null=True)
#     natop = models.TextField(db_column='natOp', blank=True, null=True)  # Field name made lowercase.
#     cfop = models.FloatField(blank=True, null=True)
#     opcao = models.TextField(blank=True, null=True)
#     tipo = models.TextField(blank=True, null=True)
#     cnpj_emitente = models.FloatField(db_column='CNPJ_Emitente', blank=True, null=True)  # Field name made lowercase.
#     xnome_emitente = models.TextField(db_column='xNome_Emitente', blank=True, null=True)  # Field name made lowercase.
#     uf_emitente_emitente = models.TextField(db_column='UF_Emitente_Emitente', blank=True, null=True)  # Field name made lowercase.
#     uf_destino = models.TextField(db_column='UF_Destino', blank=True, null=True)  # Field name made lowercase.
#     cprod = models.TextField(db_column='cProd', blank=True, null=True)  # Field name made lowercase.
#     xprod = models.TextField(db_column='xProd', blank=True, null=True)  # Field name made lowercase.
#     ncm = models.FloatField(db_column='NCM', blank=True, null=True)  # Field name made lowercase.
#     ceantrib = models.BigIntegerField(db_column='cEANTrib', blank=True, null=True)  # Field name made lowercase.
#     codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
#     codsml = models.BigIntegerField(db_column='CODSML', blank=True, null=True)  # Field name made lowercase.
#     unicx = models.FloatField(blank=True, null=True)
#     embcxa = models.FloatField(db_column='EmbCxa', blank=True, null=True)  # Field name made lowercase.
#     mrt_unidvda = models.BigIntegerField(db_column='mrt_unidVda', blank=True, null=True)  # Field name made lowercase.
#     mrt_unidcxfrn = models.BigIntegerField(db_column='mrt_unidCxFrn', blank=True, null=True)  # Field name made lowercase.
#     qtrib = models.FloatField(db_column='qTrib', blank=True, null=True)  # Field name made lowercase.
#     vuntrib = models.TextField(db_column='vUnTrib', blank=True, null=True)  # Field name made lowercase.
#     pc_mrt = models.TextField(blank=True, null=True)
#     pc_psq = models.FloatField(blank=True, null=True)
#     status = models.TextField(blank=True, null=True)
#     diretoria_compras = models.TextField(blank=True, null=True)
#     celula = models.TextField(blank=True, null=True)
#     codfrn = models.BigIntegerField(blank=True, null=True)
#     fornecedor = models.TextField(blank=True, null=True)
#     grupo_produto = models.TextField(blank=True, null=True)
#     categoria = models.TextField(blank=True, null=True)
#     subcategoria = models.TextField(blank=True, null=True)
#     produto = models.TextField(blank=True, null=True)
#     descricao_similar = models.TextField(blank=True, null=True)
#     mix = models.TextField(db_column='Mix', blank=True, null=True)  # Field name made lowercase.
#     latitude = models.FloatField(blank=True, null=True)
#     longitude = models.FloatField(blank=True, null=True)
#     estado = models.TextField(blank=True, null=True)
#     regiao = models.TextField(blank=True, null=True)
#     pc_psq_pond = models.FloatField(blank=True, null=True)
#     pc_mrt_pond = models.FloatField(blank=True, null=True)
#     abc = models.TextField(db_column='ABC', blank=True, null=True)  # Field name made lowercase.
#     categorizado = models.TextField(blank=True, null=True)
#     status_fornecedor = models.TextField(db_column='Status_Fornecedor', blank=True, null=True)  # Field name made lowercase.
#     comp = models.FloatField(db_column='Comp', blank=True, null=True)  # Field name made lowercase.
#     tipopesquisa = models.TextField(db_column='TipoPesquisa', blank=True, null=True)  # Field name made lowercase.
#     numano = models.BigIntegerField(db_column='NUMANO', blank=True, null=True)  # Field name made lowercase.
#     numanomes = models.BigIntegerField(db_column='NUMANOMES', blank=True, null=True)  # Field name made lowercase.
#     numsmnano = models.BigIntegerField(db_column='NUMSMNANO', blank=True, null=True)  # Field name made lowercase.
#     nommes = models.TextField(db_column='NOMMES', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'COMPETITIVIDADE'


class ElasticidadeDemanda(models.Model):
    cate = models.TextField(blank=True, null=True)
    uf = models.TextField(blank=True, null=True)
    exp = models.BigIntegerField(blank=True, null=True)
    filfat = models.BigIntegerField(blank=True, null=True)
    elast_proposta = models.FloatField(blank=True, null=True)
    abc = models.TextField(db_column='ABC', blank=True, null=True)  # Field name made lowercase.
    codmer = models.BigIntegerField(blank=True, null=True)
    prodtuto = models.TextField(blank=True, null=True)
    codsml = models.BigIntegerField(blank=True, null=True)
    descricao_similar = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    subcategoria = models.TextField(blank=True, null=True)
    celula = models.TextField(blank=True, null=True)
    diretoria_compras = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ELASTICIDADE_DEMANDA'


class Ettprd(models.Model):
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    desprd = models.TextField(db_column='DESPRD', blank=True, null=True)  # Field name made lowercase.
    codgrpprd = models.BigIntegerField(db_column='CODGRPPRD', blank=True, null=True)  # Field name made lowercase.
    desgrpprd = models.TextField(db_column='DESGRPPRD', blank=True, null=True)  # Field name made lowercase.
    codctgprd = models.BigIntegerField(db_column='CODCTGPRD', blank=True, null=True)  # Field name made lowercase.
    desctgprd = models.TextField(db_column='DESCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codsubctgprd = models.BigIntegerField(db_column='CODSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    dessubctgprd = models.TextField(db_column='DESSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codstaprdetq = models.TextField(db_column='CODSTAPRDETQ', blank=True, null=True)  # Field name made lowercase.
    desstaprdetq = models.TextField(db_column='DESSTAPRDETQ', blank=True, null=True)  # Field name made lowercase.
    coddivfrn = models.BigIntegerField(db_column='CODDIVFRN', blank=True, null=True)  # Field name made lowercase.
    desdivfrn = models.TextField(db_column='DESDIVFRN', blank=True, null=True)  # Field name made lowercase.
    codgrpecofrn = models.BigIntegerField(db_column='CODGRPECOFRN', blank=True, null=True)  # Field name made lowercase.
    nomgrpecofrn = models.TextField(db_column='NOMGRPECOFRN', blank=True, null=True)  # Field name made lowercase.
    coddrtcllatu = models.BigIntegerField(db_column='CODDRTCLLATU', blank=True, null=True)  # Field name made lowercase.
    desdrtcllatu = models.TextField(db_column='DESDRTCLLATU', blank=True, null=True)  # Field name made lowercase.
    codcllcmpatu = models.BigIntegerField(db_column='CODCLLCMPATU', blank=True, null=True)  # Field name made lowercase.
    descllcmpatu = models.TextField(db_column='DESCLLCMPATU', blank=True, null=True)  # Field name made lowercase.
    codcpratu = models.BigIntegerField(db_column='CODCPRATU', blank=True, null=True)  # Field name made lowercase.
    nomcpratu = models.TextField(db_column='NOMCPRATU', blank=True, null=True)  # Field name made lowercase.
    # codigo_linha_negocio = models.BigIntegerField(db_column='CODIGO_LINHA_NEGOCIO', blank=True, null=True)  # Field name made lowercase.
    # descricao_linha_negocio = models.TextField(db_column='DESCRICAO_LINHA_NEGOCIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ETTPRD'


class Metasdiarias(models.Model):
    datini = models.TextField(db_column='DATINI', blank=True, null=True)  # Field name made lowercase.
    nomdiasmn = models.TextField(db_column='NOMDIASMN', blank=True, null=True)  # Field name made lowercase.
    numsmnano = models.BigIntegerField(db_column='NUMSMNANO', blank=True, null=True)  # Field name made lowercase.
    qdediasmn = models.BigIntegerField(db_column='QDEDIASMN', blank=True, null=True)  # Field name made lowercase.
    primeiro_dia = models.TextField(db_column='PRIMEIRO_DIA', blank=True, null=True)  # Field name made lowercase.
    ultimo_dia = models.TextField(db_column='ULTIMO_DIA', blank=True, null=True)  # Field name made lowercase.
    nommes = models.TextField(db_column='NOMMES', blank=True, null=True)  # Field name made lowercase.
    nomsms = models.TextField(db_column='NOMSMS', blank=True, null=True)  # Field name made lowercase.
    nomsmsano = models.TextField(db_column='NOMSMSANO', blank=True, null=True)  # Field name made lowercase.
    codfil = models.BigIntegerField(db_column='CODFIL', blank=True, null=True)  # Field name made lowercase.
    desfil = models.TextField(db_column='DESFIL', blank=True, null=True)  # Field name made lowercase.
    codgrpprd = models.BigIntegerField(db_column='CODGRPPRD', blank=True, null=True)  # Field name made lowercase.
    desgrpprd = models.TextField(db_column='DESGRPPRD', blank=True, null=True)  # Field name made lowercase.
    codctgprd = models.BigIntegerField(db_column='CODCTGPRD', blank=True, null=True)  # Field name made lowercase.
    desctgprd = models.TextField(db_column='DESCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codsubctgprd = models.BigIntegerField(db_column='CODSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    dessubctgprd = models.TextField(db_column='DESSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codgrpecofrn = models.BigIntegerField(db_column='CODGRPECOFRN', blank=True, null=True)  # Field name made lowercase.
    nomgrpecofrn = models.TextField(db_column='NOMGRPECOFRN', blank=True, null=True)  # Field name made lowercase.
    coddivfrn = models.BigIntegerField(db_column='CODDIVFRN', blank=True, null=True)  # Field name made lowercase.
    desdivfrn = models.TextField(db_column='DESDIVFRN', blank=True, null=True)  # Field name made lowercase.
    coddivreg = models.TextField(db_column='CODDIVREG', blank=True, null=True)  # Field name made lowercase.
    nomreggeo = models.TextField(db_column='NOMREGGEO', blank=True, null=True)  # Field name made lowercase.
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
    nomestuni = models.TextField(db_column='NOMESTUNI', blank=True, null=True)  # Field name made lowercase.
    codundreg = models.BigIntegerField(db_column='CODUNDREG', blank=True, null=True)  # Field name made lowercase.
    desundreg = models.TextField(db_column='DESUNDREG', blank=True, null=True)  # Field name made lowercase.
    codtipcnoocd = models.TextField(db_column='CODTIPCNOOCD', blank=True, null=True)  # Field name made lowercase.
    destipcnoocd = models.TextField(db_column='DESTIPCNOOCD', blank=True, null=True)  # Field name made lowercase.
    codcnoocd = models.TextField(db_column='CODCNOOCD', blank=True, null=True)  # Field name made lowercase.
    descnoocd = models.TextField(db_column='DESCNOOCD', blank=True, null=True)  # Field name made lowercase.
    vlrvndfatliq = models.FloatField(db_column='VLRVNDFATLIQ', blank=True, null=True)  # Field name made lowercase.
    vlrrctliqapu = models.FloatField(db_column='VLRRCTLIQAPU', blank=True, null=True)  # Field name made lowercase.
    vlrmrgcrb = models.FloatField(db_column='VLRMRGCRB', blank=True, null=True)  # Field name made lowercase.
    vlrmrgbrt = models.FloatField(db_column='VLRMRGBRT', blank=True, null=True)  # Field name made lowercase.
    destipopevnd = models.TextField(db_column='DESTIPOPEVND', blank=True, null=True)  # Field name made lowercase.
    desdrtcllatu = models.TextField(db_column='DESDRTCLLATU', blank=True, null=True)  # Field name made lowercase.
    descllcmpatu = models.TextField(db_column='DESCLLCMPATU', blank=True, null=True)  # Field name made lowercase.
    nomcpratu = models.TextField(db_column='NOMCPRATU', blank=True, null=True)  # Field name made lowercase.
    indctgtop = models.TextField(db_column='INDCTGTOP', blank=True, null=True)  # Field name made lowercase.
    concat = models.TextField(db_column='CONCAT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'METASDIARIAS'


class Movetq(models.Model):
    datini = models.TextField(db_column='DATINI', blank=True, null=True)  # Field name made lowercase.
    numsmnano = models.BigIntegerField(db_column='NUMSMNANO', blank=True, null=True)  # Field name made lowercase.
    nomdiasmn = models.TextField(db_column='NOMDIASMN', blank=True, null=True)  # Field name made lowercase.
    nomabvmesano = models.TextField(db_column='NOMABVMESANO', blank=True, null=True)  # Field name made lowercase.
    nomsmsano = models.TextField(db_column='NOMSMSANO', blank=True, null=True)  # Field name made lowercase.
    numdiasmn = models.BigIntegerField(db_column='NUMDIASMN', blank=True, null=True)  # Field name made lowercase.
    codgrpprd = models.BigIntegerField(db_column='CODGRPPRD', blank=True, null=True)  # Field name made lowercase.
    desgrpprd = models.TextField(db_column='DESGRPPRD', blank=True, null=True)  # Field name made lowercase.
    codctgprd = models.BigIntegerField(db_column='CODCTGPRD', blank=True, null=True)  # Field name made lowercase.
    desctgprd = models.TextField(db_column='DESCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codsubctgprd = models.BigIntegerField(db_column='CODSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    dessubctgprd = models.TextField(db_column='DESSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codgrpecofrn = models.BigIntegerField(db_column='CODGRPECOFRN', blank=True, null=True)  # Field name made lowercase.
    nomgrpecofrn = models.TextField(db_column='NOMGRPECOFRN', blank=True, null=True)  # Field name made lowercase.
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    desprd = models.TextField(db_column='DESPRD', blank=True, null=True)  # Field name made lowercase.
    codstaprdetq = models.FloatField(db_column='CODSTAPRDETQ', blank=True, null=True)  # Field name made lowercase.
    desstaprdetq = models.TextField(db_column='DESSTAPRDETQ', blank=True, null=True)  # Field name made lowercase.
    coddivfrn = models.BigIntegerField(db_column='CODDIVFRN', blank=True, null=True)  # Field name made lowercase.
    desdivfrn = models.TextField(db_column='DESDIVFRN', blank=True, null=True)  # Field name made lowercase.
    codfil = models.BigIntegerField(db_column='CODFIL', blank=True, null=True)  # Field name made lowercase.
    desfil = models.TextField(db_column='DESFIL', blank=True, null=True)  # Field name made lowercase.
    coddrtcllatu = models.BigIntegerField(db_column='CODDRTCLLATU', blank=True, null=True)  # Field name made lowercase.
    desdrtcllatu = models.TextField(db_column='DESDRTCLLATU', blank=True, null=True)  # Field name made lowercase.
    codcllcmpatu = models.BigIntegerField(db_column='CODCLLCMPATU', blank=True, null=True)  # Field name made lowercase.
    descllcmpatu = models.TextField(db_column='DESCLLCMPATU', blank=True, null=True)  # Field name made lowercase.
    codcpratu = models.BigIntegerField(db_column='CODCPRATU', blank=True, null=True)  # Field name made lowercase.
    nomcpratu = models.TextField(db_column='NOMCPRATU', blank=True, null=True)  # Field name made lowercase.
    codundreg = models.BigIntegerField(db_column='CODUNDREG', blank=True, null=True)  # Field name made lowercase.
    desundreg = models.TextField(db_column='DESUNDREG', blank=True, null=True)  # Field name made lowercase.
    flgundreg = models.BigIntegerField(db_column='FLGUNDREG', blank=True, null=True)  # Field name made lowercase.
    vlruntcstsco = models.FloatField(db_column='VLRUNTCSTSCO', blank=True, null=True)  # Field name made lowercase.
    vlretqhiglgt = models.BigIntegerField(db_column='VLRETQHIGLGT', blank=True, null=True)  # Field name made lowercase.
    qdeiteatvsemetqvnd = models.BigIntegerField(db_column='QDEITEATVSEMETQVND', blank=True, null=True)  # Field name made lowercase.
    vlretqexemer = models.FloatField(db_column='VLRETQEXEMER', blank=True, null=True)  # Field name made lowercase.
    vlrvndpdafltetq = models.FloatField(db_column='VLRVNDPDAFLTETQ', blank=True, null=True)  # Field name made lowercase.
    vlrvndsmnmer = models.FloatField(db_column='VLRVNDSMNMER', blank=True, null=True)  # Field name made lowercase.
    qdeiteetq = models.FloatField(db_column='QDEITEETQ', blank=True, null=True)  # Field name made lowercase.
    vlrfatmercstcmpidl = models.FloatField(db_column='VLRFATMERCSTCMPIDL', blank=True, null=True)  # Field name made lowercase.
    vlracuetqcstsco = models.FloatField(db_column='VLRACUETQCSTSCO', blank=True, null=True)  # Field name made lowercase.
    vlracurctliq = models.FloatField(db_column='VLRACURCTLIQ', blank=True, null=True)  # Field name made lowercase.
    vlracupgt = models.FloatField(db_column='VLRACUPGT', blank=True, null=True)  # Field name made lowercase.
    vlracurcb = models.FloatField(db_column='VLRACURCB', blank=True, null=True)  # Field name made lowercase.
    qdemedvndmnsmer = models.FloatField(db_column='QDEMEDVNDMNSMER', blank=True, null=True)  # Field name made lowercase.
    vlrdircstmedmer = models.FloatField(db_column='VLRDIRCSTMEDMER', blank=True, null=True)  # Field name made lowercase.
    qdedirmeretqtra = models.FloatField(db_column='QDEDIRMERETQTRA', blank=True, null=True)  # Field name made lowercase.
    qdevnddirmerpnd = models.FloatField(db_column='QDEVNDDIRMERPND', blank=True, null=True)  # Field name made lowercase.
    vlrcstcmpidl = models.FloatField(db_column='VLRCSTCMPIDL', blank=True, null=True)  # Field name made lowercase.
    vlrmedpcocmp = models.FloatField(db_column='VLRMEDPCOCMP', blank=True, null=True)  # Field name made lowercase.
    inditeidcgirisf = models.FloatField(db_column='INDITEIDCGIRISF', blank=True, null=True)  # Field name made lowercase.
    qtdrgt = models.BigIntegerField(db_column='QTDRGT', blank=True, null=True)  # Field name made lowercase.
    flgitezrd = models.TextField(db_column='FLGITEZRD', blank=True, null=True)  # Field name made lowercase.
    perdvocstcmpidl = models.BigIntegerField(db_column='PERDVOCSTCMPIDL', blank=True, null=True)  # Field name made lowercase.
    numerador_cbtetq = models.FloatField(db_column='NUMERADOR_CBTETQ', blank=True, null=True)  # Field name made lowercase.
    denominador_cbtetq = models.FloatField(db_column='DENOMINADOR_CBTETQ', blank=True, null=True)  # Field name made lowercase.
    vlracurctliqocd = models.BigIntegerField(db_column='VLRACURCTLIQOCD', blank=True, null=True)  # Field name made lowercase.
    vlracumrgbrtrlz = models.BigIntegerField(db_column='VLRACUMRGBRTRLZ', blank=True, null=True)  # Field name made lowercase.
    vlracumrgbrtocd = models.BigIntegerField(db_column='VLRACUMRGBRTOCD', blank=True, null=True)  # Field name made lowercase.
    vlracumrgcrbrlz = models.BigIntegerField(db_column='VLRACUMRGCRBRLZ', blank=True, null=True)  # Field name made lowercase.
    vlracumrgcrbocd = models.BigIntegerField(db_column='VLRACUMRGCRBOCD', blank=True, null=True)  # Field name made lowercase.
    vlracufatliqrlz = models.BigIntegerField(db_column='VLRACUFATLIQRLZ', blank=True, null=True)  # Field name made lowercase.
    vlracufatliqocd = models.BigIntegerField(db_column='VLRACUFATLIQOCD', blank=True, null=True)  # Field name made lowercase.
    vlrmrgcrbajt = models.FloatField(db_column='VLRMRGCRBAJT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVETQ'


class Movplncmpcal(models.Model):
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    codfilepd = models.BigIntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.BigIntegerField(db_column='CODFILFAT', blank=True, null=True)  # Field name made lowercase.
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
    month = models.FloatField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    year = models.FloatField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    week = models.TextField(db_column='WEEK', blank=True, null=True)  # Field name made lowercase.
    volvndsug = models.FloatField(db_column='VOLVNDSUG', blank=True, null=True)  # Field name made lowercase.
    volvndsugalc = models.FloatField(db_column='VOLVNDSUGALC', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperocd = models.FloatField(db_column='MRGBRTPEROCD', blank=True, null=True)  # Field name made lowercase.
    vlrpcosug = models.FloatField(db_column='VLRPCOSUG', blank=True, null=True)  # Field name made lowercase.
    vlrpcobasesug = models.FloatField(db_column='VLRPCOBASESUG', blank=True, null=True)  # Field name made lowercase.
    vlrimptotsug = models.FloatField(db_column='VLRIMPTOTSUG', blank=True, null=True)  # Field name made lowercase.
    vlricmssug = models.FloatField(db_column='VLRICMSSUG', blank=True, null=True)  # Field name made lowercase.
    vlrpiscofsug = models.FloatField(db_column='VLRPISCOFSUG', blank=True, null=True)  # Field name made lowercase.
    vlrdevsug = models.FloatField(db_column='VLRDEVSUG', blank=True, null=True)  # Field name made lowercase.
    vlrflxsug = models.FloatField(db_column='VLRFLXSUG', blank=True, null=True)  # Field name made lowercase.
    vlrmrgbrtsug = models.FloatField(db_column='VLRMRGBRTSUG', blank=True, null=True)  # Field name made lowercase.
    vrbuntsugsug = models.BigIntegerField(db_column='VRBUNTSUGSUG', blank=True, null=True)  # Field name made lowercase.
    vlrvrbplan = models.TextField(db_column='VLRVRBPLAN', blank=True, null=True)  # Field name made lowercase.
    vlrcmvpcosug = models.FloatField(db_column='VLRCMVPCOSUG', blank=True, null=True)  # Field name made lowercase.
    vlrcmvpcoatu = models.FloatField(db_column='VLRCMVPCOATU', blank=True, null=True)  # Field name made lowercase.
    vlrcmvcmpatu = models.FloatField(db_column='VLRCMVCMPATU', blank=True, null=True)  # Field name made lowercase.
    vlrpcomrc = models.FloatField(db_column='VLRPCOMRC', blank=True, null=True)  # Field name made lowercase.
    vlrcompsug = models.FloatField(db_column='VLRCOMPSUG', blank=True, null=True)  # Field name made lowercase.
    volvndpln = models.FloatField(db_column='VOLVNDPLN', blank=True, null=True)  # Field name made lowercase.
    vlrpcopln = models.FloatField(db_column='VLRPCOPLN', blank=True, null=True)  # Field name made lowercase.
    vlrpcobasepln = models.FloatField(db_column='VLRPCOBASEPLN', blank=True, null=True)  # Field name made lowercase.
    vlrimptotpln = models.FloatField(db_column='VLRIMPTOTPLN', blank=True, null=True)  # Field name made lowercase.
    vlricmspln = models.FloatField(db_column='VLRICMSPLN', blank=True, null=True)  # Field name made lowercase.
    vlrpiscofpln = models.FloatField(db_column='VLRPISCOFPLN', blank=True, null=True)  # Field name made lowercase.
    vlrdevpln = models.FloatField(db_column='VLRDEVPLN', blank=True, null=True)  # Field name made lowercase.
    vlrflxpln = models.FloatField(db_column='VLRFLXPLN', blank=True, null=True)  # Field name made lowercase.
    vlrmrgbrtpln = models.FloatField(db_column='VLRMRGBRTPLN', blank=True, null=True)  # Field name made lowercase.
    vrbuntsugpln = models.FloatField(db_column='VRBUNTSUGPLN', blank=True, null=True)  # Field name made lowercase.
    vlrvrbpln = models.FloatField(db_column='VLRVRBPLN', blank=True, null=True)  # Field name made lowercase.
    vlrcmvpcopln = models.FloatField(db_column='VLRCMVPCOPLN', blank=True, null=True)  # Field name made lowercase.
    vlrcmvcmppln = models.FloatField(db_column='VLRCMVCMPPLN', blank=True, null=True)  # Field name made lowercase.
    vlrcomppln = models.FloatField(db_column='VLRCOMPPLN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVPLNCMPCAL'


class Movvbs(models.Model):
    numanomesdia = models.BigIntegerField(db_column='NUMANOMESDIA', blank=True, null=True)  # Field name made lowercase.
    codfilepd = models.BigIntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.BigIntegerField(db_column='CODFILFAT', blank=True, null=True)  # Field name made lowercase.
    codcli = models.BigIntegerField(db_column='CODCLI', blank=True, null=True)  # Field name made lowercase.
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    numped = models.BigIntegerField(db_column='NUMPED', blank=True, null=True)  # Field name made lowercase.
    quantidade_itens_pedido = models.FloatField(db_column='QUANTIDADE_ITENS_PEDIDO', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_venda_liquida = models.FloatField(db_column='VALOR_UNITARIO_VENDA_LIQUIDA', blank=True, null=True)  # Field name made lowercase.
    valor_total_venda_liquida = models.FloatField(db_column='VALOR_TOTAL_VENDA_LIQUIDA', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_cmv = models.FloatField(db_column='VALOR_UNITARIO_CMV', blank=True, null=True)  # Field name made lowercase.
    valor_total_cmv = models.FloatField(db_column='VALOR_TOTAL_CMV', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_funding = models.FloatField(db_column='VALOR_UNITARIO_FUNDING', blank=True, null=True)  # Field name made lowercase.
    valor_total_funding = models.FloatField(db_column='VALOR_TOTAL_FUNDING', blank=True, null=True)  # Field name made lowercase.
    quantidade_itens_promocao = models.FloatField(db_column='QUANTIDADE_ITENS_PROMOCAO', blank=True, null=True)  # Field name made lowercase.
    quantidade_itens_beneficio = models.FloatField(db_column='QUANTIDADE_ITENS_BENEFICIO', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_promocao = models.FloatField(db_column='VALOR_UNITARIO_PROMOÇÃO', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_beneficio = models.FloatField(db_column='VALOR_UNITARIO_BENEFICIO', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_funding_preco = models.FloatField(db_column='VALOR_UNITARIO_FUNDING_PRECO', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_funding_margem = models.FloatField(db_column='VALOR_UNITARIO_FUNDING_MARGEM', blank=True, null=True)  # Field name made lowercase.
    valor_total_promocao = models.FloatField(db_column='VALOR_TOTAL_PROMOÇÃO', blank=True, null=True)  # Field name made lowercase.
    valor_total_beneficio = models.FloatField(db_column='VALOR_TOTAL_BENEFICIO', blank=True, null=True)  # Field name made lowercase.
    valor_total_funding_preco = models.FloatField(db_column='VALOR_TOTAL_FUNDING_PRECO', blank=True, null=True)  # Field name made lowercase.
    valor_total_funding_margem = models.FloatField(db_column='VALOR_TOTAL_FUNDING_MARGEM', blank=True, null=True)  # Field name made lowercase.
    valor_total_dms_sansung = models.FloatField(db_column='VALOR_TOTAL_DMS_SANSUNG', blank=True, null=True)  # Field name made lowercase.
    rebate = models.FloatField(db_column='REBATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVVBS'


class Movvndhstfim(models.Model):
    numanomessmn = models.BigIntegerField(db_column='NUMANOMESSMN', blank=True, null=True)  # Field name made lowercase.
    numanomes = models.BigIntegerField(db_column='NUMANOMES', blank=True, null=True)  # Field name made lowercase.
    numanomesdia = models.BigIntegerField(db_column='NUMANOMESDIA', blank=True, null=True)  # Field name made lowercase.
    codcliend = models.BigIntegerField(db_column='CODCLIEND', blank=True, null=True)  # Field name made lowercase.
    codcnlcmccli = models.BigIntegerField(db_column='CODCNLCMCCLI', blank=True, null=True)  # Field name made lowercase.
    codmnccli = models.BigIntegerField(db_column='CODMNCCLI', blank=True, null=True)  # Field name made lowercase.
    codestcli = models.TextField(db_column='CODESTCLI', blank=True, null=True)  # Field name made lowercase.
    codfilepd = models.BigIntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.BigIntegerField(db_column='CODFILFAT', blank=True, null=True)  # Field name made lowercase.
    codmer = models.BigIntegerField(db_column='CODMER', blank=True, null=True)  # Field name made lowercase.
    codgrpprd = models.BigIntegerField(db_column='CODGRPPRD', blank=True, null=True)  # Field name made lowercase.
    codctgprd = models.BigIntegerField(db_column='CODCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codsubctgprd = models.BigIntegerField(db_column='CODSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    numped = models.BigIntegerField(db_column='NUMPED', blank=True, null=True)  # Field name made lowercase.
    codrepcmc = models.BigIntegerField(db_column='CODREPCMC', blank=True, null=True)  # Field name made lowercase.
    nomrepcmc = models.TextField(db_column='NOMREPCMC', blank=True, null=True)  # Field name made lowercase.
    datnscrepcmc = models.TextField(db_column='DATNSCREPCMC', blank=True, null=True)  # Field name made lowercase.
    datcadrepcmc = models.TextField(db_column='DATCADREPCMC', blank=True, null=True)  # Field name made lowercase.
    tippedvnd = models.TextField(db_column='TIPPEDVND', blank=True, null=True)  # Field name made lowercase.
    vlrvndliqprs = models.FloatField(db_column='VLRVNDLIQPRS', blank=True, null=True)  # Field name made lowercase.
    vlrvndliqtlv = models.FloatField(db_column='VLRVNDLIQTLV', blank=True, null=True)  # Field name made lowercase.
    vlrvndliqb2b = models.FloatField(db_column='VLRVNDLIQB2B', blank=True, null=True)  # Field name made lowercase.
    vlrvndliq = models.FloatField(db_column='VLRVNDLIQ', blank=True, null=True)  # Field name made lowercase.
    qdeite = models.BigIntegerField(db_column='QDEITE', blank=True, null=True)  # Field name made lowercase.
    vlrdscflxcns = models.FloatField(db_column='VLRDSCFLXCNS', blank=True, null=True)  # Field name made lowercase.
    vlrsupflx = models.FloatField(db_column='VLRSUPFLX', blank=True, null=True)  # Field name made lowercase.
    vlrimptot = models.FloatField(db_column='VLRIMPTOT', blank=True, null=True)  # Field name made lowercase.
    vlrrctliq = models.FloatField(db_column='VLRRCTLIQ', blank=True, null=True)  # Field name made lowercase.
    cmv = models.FloatField(db_column='CMV', blank=True, null=True)  # Field name made lowercase.
    permrgadicnlvnd = models.FloatField(db_column='PERMRGADICNLVND', blank=True, null=True)  # Field name made lowercase.
    funding = models.FloatField(db_column='FUNDING', blank=True, null=True)  # Field name made lowercase.
    margem_bruta = models.FloatField(db_column='MARGEM_BRUTA', blank=True, null=True)  # Field name made lowercase.
    transferencia = models.FloatField(db_column='TRANSFERENCIA', blank=True, null=True)  # Field name made lowercase.
    distribuicao = models.FloatField(db_column='DISTRIBUICAO', blank=True, null=True)  # Field name made lowercase.
    armazenagem = models.FloatField(db_column='ARMAZENAGEM', blank=True, null=True)  # Field name made lowercase.
    vendasrca = models.FloatField(db_column='VENDASRCA', blank=True, null=True)  # Field name made lowercase.
    vendasclt = models.FloatField(db_column='VENDASCLT', blank=True, null=True)  # Field name made lowercase.
    televendas = models.FloatField(db_column='TELEVENDAS', blank=True, null=True)  # Field name made lowercase.
    cartaocredito = models.FloatField(db_column='CARTAOCREDITO', blank=True, null=True)  # Field name made lowercase.
    marketplace = models.BigIntegerField(db_column='MARKETPLACE', blank=True, null=True)  # Field name made lowercase.
    conta_corrente = models.FloatField(db_column='CONTA_CORRENTE', blank=True, null=True)  # Field name made lowercase.
    acordocomercial = models.BigIntegerField(db_column='ACORDOCOMERCIAL', blank=True, null=True)  # Field name made lowercase.
    parceirocom = models.FloatField(db_column='PARCEIROCOM', blank=True, null=True)  # Field name made lowercase.
    margem_contribuicao = models.FloatField(db_column='MARGEM_CONTRIBUICAO', blank=True, null=True)  # Field name made lowercase.
    leadtime = models.BigIntegerField(db_column='LEADTIME', blank=True, null=True)  # Field name made lowercase.
    concat = models.TextField(db_column='CONCAT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVVNDHSTFIM'


class OutputPln(models.Model):
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    codfilepd = models.BigIntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.BigIntegerField(db_column='CODFILFAT', blank=True, null=True)  # Field name made lowercase.
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
    month = models.FloatField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    year = models.FloatField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    codsubctgprd = models.BigIntegerField(db_column='CODSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codctgprd = models.BigIntegerField(db_column='CODCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codgrpprd = models.BigIntegerField(db_column='CODGRPPRD', blank=True, null=True)  # Field name made lowercase.
    coddivfrn = models.BigIntegerField(db_column='CODDIVFRN', blank=True, null=True)  # Field name made lowercase.
    week = models.TextField(db_column='WEEK', blank=True, null=True)  # Field name made lowercase.
    qdediasmn = models.BigIntegerField(db_column='QDEDIASMN', blank=True, null=True)  # Field name made lowercase.
    volvndliqsubocd = models.FloatField(db_column='VOLVNDLIQSUBOCD', blank=True, null=True)  # Field name made lowercase.
    mrgbrtocd = models.FloatField(db_column='MRGBRTOCD', blank=True, null=True)  # Field name made lowercase.
    vlrrctliqocd = models.FloatField(db_column='VLRRCTLIQOCD', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperocd = models.FloatField(db_column='MRGBRTPEROCD', blank=True, null=True)  # Field name made lowercase.
    vlrhstvndliqsub = models.FloatField(db_column='VLRHSTVNDLIQSUB', blank=True, null=True)  # Field name made lowercase.
    vlrhstvndliqprd = models.FloatField(db_column='VLRHSTVNDLIQPRD', blank=True, null=True)  # Field name made lowercase.
    vlrhstrctliqprd = models.FloatField(db_column='VLRHSTRCTLIQPRD', blank=True, null=True)  # Field name made lowercase.
    rprhst = models.FloatField(db_column='RPRHST', blank=True, null=True)  # Field name made lowercase.
    rprrctliq = models.FloatField(db_column='RPRRCTLIQ', blank=True, null=True)  # Field name made lowercase.
    volvndsug = models.FloatField(db_column='VOLVNDSUG', blank=True, null=True)  # Field name made lowercase.
    mrgbrtsug = models.FloatField(db_column='MRGBRTSUG', blank=True, null=True)  # Field name made lowercase.
    vlrrctliqsug = models.FloatField(db_column='VLRRCTLIQSUG', blank=True, null=True)  # Field name made lowercase.
    rprhstbnf = models.FloatField(db_column='RPRHSTBNF', blank=True, null=True)  # Field name made lowercase.
    rprhstflx = models.FloatField(db_column='RPRHSTFLX', blank=True, null=True)  # Field name made lowercase.
    rprhstmrgcnl = models.FloatField(db_column='RPRHSTMRGCNL', blank=True, null=True)  # Field name made lowercase.
    rprhstsupflx = models.FloatField(db_column='RPRHSTSUPFLX', blank=True, null=True)  # Field name made lowercase.
    rprhstdesfin = models.BigIntegerField(db_column='RPRHSTDESFIN', blank=True, null=True)  # Field name made lowercase.
    elasticidade = models.FloatField(db_column='Elasticidade', blank=True, null=True)  # Field name made lowercase.
    prdinelast = models.BigIntegerField(db_column='PRDINELAST', blank=True, null=True)  # Field name made lowercase.
    pcomed = models.FloatField(db_column='PCOMED', blank=True, null=True)  # Field name made lowercase.
    qtdmed = models.FloatField(db_column='QTDMED', blank=True, null=True)  # Field name made lowercase.
    pcomax = models.FloatField(db_column='PCOMAX', blank=True, null=True)  # Field name made lowercase.
    pcomin = models.FloatField(db_column='PCOMIN', blank=True, null=True)  # Field name made lowercase.
    vlrvolvndmed = models.FloatField(db_column='VLRVOLVNDMED', blank=True, null=True)  # Field name made lowercase.
    vlrpcosug = models.FloatField(db_column='VLRPCOSUG', blank=True, null=True)  # Field name made lowercase.
    qtdsug = models.FloatField(db_column='QTDSUG', blank=True, null=True)  # Field name made lowercase.
    vlrpcobasesug = models.FloatField(db_column='VLRPCOBASESUG', blank=True, null=True)  # Field name made lowercase.
    flex = models.BigIntegerField(db_column='FLEX', blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    pis_cofins = models.FloatField(db_column='PIS_COFINS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.FloatField(db_column='COMPLEMENTO', blank=True, null=True)  # Field name made lowercase.
    devolucao = models.FloatField(db_column='DEVOLUÇÃO', blank=True, null=True)  # Field name made lowercase.
    verbapco = models.BigIntegerField(db_column='VerbaPco', blank=True, null=True)  # Field name made lowercase.
    bonificado = models.BigIntegerField(db_column='Bonificado', blank=True, null=True)  # Field name made lowercase.
    rebate = models.BigIntegerField(db_column='Rebate', blank=True, null=True)  # Field name made lowercase.
    fundpco = models.BigIntegerField(db_column='FundPco', blank=True, null=True)  # Field name made lowercase.
    vlrflxsug = models.FloatField(db_column='VLRFLXSUG', blank=True, null=True)  # Field name made lowercase.
    vlrdevsug = models.FloatField(db_column='VLRDEVSUG', blank=True, null=True)  # Field name made lowercase.
    vlrpiscofsug = models.FloatField(db_column='VLRPISCOFSUG', blank=True, null=True)  # Field name made lowercase.
    vlricmssug = models.FloatField(db_column='VLRICMSSUG', blank=True, null=True)  # Field name made lowercase.
    vlrmrgbrtsug = models.FloatField(db_column='VLRMRGBRTSUG', blank=True, null=True)  # Field name made lowercase.
    vlrcmvpcosug = models.FloatField(db_column='VLRCMVPCOSUG', blank=True, null=True)  # Field name made lowercase.
    vlrcmvcmpatu = models.FloatField(db_column='VLRCMVCMPATU', blank=True, null=True)  # Field name made lowercase.
    vlrcmvpcoatu = models.FloatField(db_column='VLRCMVPCOATU', blank=True, null=True)  # Field name made lowercase.
    ftrcmvcmpcmvpco = models.FloatField(db_column='FTRCMVCMPCMVPCO', blank=True, null=True)  # Field name made lowercase.
    atumaiormeta = models.BigIntegerField(db_column='ATUMAIORMETA', blank=True, null=True)  # Field name made lowercase.
    vrbuntsugsug = models.BigIntegerField(db_column='VRBUNTSUGSUG', blank=True, null=True)  # Field name made lowercase.
    numanomes = models.BigIntegerField(db_column='NUMANOMES', blank=True, null=True)  # Field name made lowercase.
    vlrpcomrc = models.FloatField(db_column='VLRPCOMRC', blank=True, null=True)  # Field name made lowercase.
    vlrcompsug = models.FloatField(db_column='VLRCOMPSUG', blank=True, null=True)  # Field name made lowercase.
    volvndsugalc = models.FloatField(db_column='VOLVNDSUGALC', blank=True, null=True)  # Field name made lowercase.
    vndsugmaiorvndalc = models.FloatField(db_column='VNDSUGMAIORVNDALC', blank=True, null=True)  # Field name made lowercase.
    vlrimptotsug = models.FloatField(db_column='VLRIMPTOTSUG', blank=True, null=True)  # Field name made lowercase.
    vlrvrbplan = models.TextField(db_column='VLRVRBPLAN', blank=True, null=True)  # Field name made lowercase.
    vlrcmvcmppln = models.FloatField(db_column='VLRCMVCMPPLN', blank=True, null=True)  # Field name made lowercase.
    vlrbonpln = models.FloatField(db_column='VLRBONPLN', blank=True, null=True)  # Field name made lowercase.
    vlrvrbpln = models.FloatField(db_column='VLRVRBPLN', blank=True, null=True)  # Field name made lowercase.
    vlrvbapcopln = models.FloatField(db_column='VLRVBAPCOPLN', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperpln = models.FloatField(db_column='MRGBRTPERPLN', blank=True, null=True)  # Field name made lowercase.
    vlrcmvpcopln = models.FloatField(db_column='VLRCMVPCOPLN', blank=True, null=True)  # Field name made lowercase.
    vrbuntsugpln = models.FloatField(db_column='VRBUNTSUGPLN', blank=True, null=True)  # Field name made lowercase.
    vlrpcobasepln = models.FloatField(db_column='VLRPCOBASEPLN', blank=True, null=True)  # Field name made lowercase.
    vlrflxpln = models.FloatField(db_column='VLRFLXPLN', blank=True, null=True)  # Field name made lowercase.
    vlrdevpln = models.FloatField(db_column='VLRDEVPLN', blank=True, null=True)  # Field name made lowercase.
    vlrpiscofpln = models.FloatField(db_column='VLRPISCOFPLN', blank=True, null=True)  # Field name made lowercase.
    vlricmspln = models.FloatField(db_column='VLRICMSPLN', blank=True, null=True)  # Field name made lowercase.
    vlrmrgbrtpln = models.FloatField(db_column='VLRMRGBRTPLN', blank=True, null=True)  # Field name made lowercase.
    vlrpcopln = models.FloatField(db_column='VLRPCOPLN', blank=True, null=True)  # Field name made lowercase.
    volvndpln = models.FloatField(db_column='VOLVNDPLN', blank=True, null=True)  # Field name made lowercase.
    qtdpln = models.FloatField(db_column='QTDPLN', blank=True, null=True)  # Field name made lowercase.
    vlrcomppln = models.FloatField(db_column='VLRCOMPPLN', blank=True, null=True)  # Field name made lowercase.
    vlrimptotpln = models.FloatField(db_column='VLRIMPTOTPLN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OUTPUT_PLN'


class Prdsml(models.Model):
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    codsml = models.BigIntegerField(blank=True, null=True)
    dessml = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prdsml'

class DadosMestre_Verba(models.Model):
    """
        Modelo de Tabela Dados Mestre
    """

    class Meta:
        db_table = "mrt.MOVVBADISCAL"

    CODPRD = models.IntegerField()
    CODFILEPD = models.IntegerField()
    DATREF = models.IntegerField(blank=True, null=True)
    VLRSLDPCOMESANT = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRCRDPCO = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRDBTPCO = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRSLDMRGMESANT = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRCRDMRG = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRDBTMRG = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)

class Competitividade(models.Model):
    """
    Model for table COMPETITIVIDADE
    """

    class Meta:
        db_table = 'mrt.MOVPCOMCD'

    CODPRD = models.IntegerField()
    CODIDTCUR = models.CharField(primary_key=True, max_length=100)
    CODESTUNI = models.CharField(max_length=100, blank=True, null=True)
    NUMANO = models.IntegerField(blank=True, null=True)
    NUMANOMES = models.IntegerField(blank=True, null=True)
    NUMSMNANO = models.IntegerField(blank=True, null=True)
    NOMMES = models.CharField(max_length=20, blank=True, null=True)
    DATREF = models.CharField(max_length=20, blank=True, null=True)
    CODSML = models.IntegerField()
    DESGRPMERSMR = models.CharField(max_length=45, blank=True, null=True)
    CODTIPAPU = models.CharField(max_length=45, blank=True, null=True)
    VLRPCOMEDMCD = models.CharField(max_length=15)
    VLRPCOBSEMER = models.DecimalField(decimal_places=2, max_digits=10)
    CLFCRVABCMER = models.CharField(max_length=1, blank=True, null=True)

    

class Elasticidade(models.Model):
    """
    Model for table ELASTICIDADE
    """

    class Meta:
        db_table = 'mrt.MOVVARVNDPCO'

    CODPRD = models.IntegerField()
    CODESTUNI = models.CharField(max_length=2)
    CODFILEPD = models.IntegerField(default=1)
    CODFILFAT = models.IntegerField()
    VLRVARVNDPCO = models.DecimalField(decimal_places=2, max_digits=10)
    DESMER = models.CharField(max_length=45)
    CLFCRVABCMER = models.CharField(max_length=1) 
    CODGRPMERSMR = models.IntegerField()
    DESGRPMERSMR = models.CharField(max_length=45)
    DESFMLMER = models.IntegerField()
    DESCLSMER = models.CharField(max_length=45)
    DESDIVCMP = models.CharField(max_length=45)
    DESDRTCLLATU = models.CharField(max_length=150)

class VerbaeBC(models.Model):
    """
    Model for table VERBA_E_BC

    """

    class Meta:
        db_table = 'mrt.MOVVBAHST'

    CODPRD = models.IntegerField()
    CODFILEPD = models.IntegerField()
    CODFILFAT = models.IntegerField()
    CODCLI = models.IntegerField()
    CODESTCLI = models.IntegerField()
    NUMPED = models.IntegerField()
    NUMANOMESDIA = models.DateTimeField()
    QDEITEPED = models.IntegerField()
    VLRVNDLIQ = models.DecimalField(decimal_places=2, max_digits=10)
    VLRUNTCSTMER = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCSTMER = models.DecimalField(decimal_places=2, max_digits=10)
    VLRUNTFNDMER = models.DecimalField(decimal_places=2, max_digits=10)
    VLRFND = models.DecimalField(decimal_places=2, max_digits=10)
    QDEITEPMC = models.IntegerField()
    QDEITEBFC = models.IntegerField()
    VLRUNTFNDPMCVND = models.DecimalField(decimal_places=2, max_digits=10)
    VLRUNTDSCBFCITE = models.DecimalField(decimal_places=2, max_digits=10)
    VLRUNTFNDPCO = models.DecimalField(decimal_places=2, max_digits=10)
    VLRUNTFNDMRG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRRLZPMC = models.DecimalField(decimal_places=2, max_digits=10)
    VLRBFC = models.DecimalField(decimal_places=2, max_digits=10)
    VLRFNDPCOVND = models.DecimalField(decimal_places=2, max_digits=10)
    VLRFNDPCOCST = models.DecimalField(decimal_places=2, max_digits=10)
    VLRMNSFNDRCBFRN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRRBTCAL = models.DecimalField(decimal_places=2, max_digits=10)





class Vendas(models.Model):
    """
    Model for table VENDAS
    """

    class Meta:
        db_table = 'mrt.MOVVNDHSTCAL'

    CODPRD = models.IntegerField()
    CODFILEPD = models.IntegerField()
    CODFILFAT = models.IntegerField()
    CODESTCLI = models.CharField(max_length=2)
    CODREPCMC = models.IntegerField()
    NUMPED = models.IntegerField()
    NUMANOMESSMN = models.DateTimeField()
    NUMANOMESDIA = models.DateTimeField()
    VLRVNDLIQ = models.DecimalField(decimal_places=2, max_digits=10)
    QDEITE = models.IntegerField()
    VLRDSCFLXCNS = models.DecimalField(decimal_places=2, max_digits=10)
    VLRSUPFLX = models.DecimalField(decimal_places=2, max_digits=10)
    VLRIMPTOT = models.DecimalField(decimal_places=2, max_digits=10)
    VLRRCTLIQAPU = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCSTMEDPRD = models.DecimalField(decimal_places=2, max_digits=10)
    PERMRGADICNLVND = models.DecimalField(decimal_places=2, max_digits=10)
    VLRFND = models.DecimalField(decimal_places=2, max_digits=10)
    VLRMRGBRT = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCSTTRNTNLCUB = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCSTDTB = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCSTARG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRMRGCRB = models.DecimalField(decimal_places=2, max_digits=10)


class DadosMestre_ComposicaoPreco(models.Model):

    class Meta:
        db_table = "mrt.MOVPCOBSECAL"

    CODPRD = models.IntegerField()
    CODFILEPD = models.IntegerField(blank=True, null=True)
    CODFILFAT = models.IntegerField()
    DATREF = models.CharField(max_length=20, blank=True, null=True)
    CODESTUNI = models.CharField(max_length=2)
    TIPEDEREG = models.IntegerField()
    VLRMRGBRT = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRVBA = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRFND = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRFNDRBTITE = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRICM = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPIS = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRDVL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRUNTPCOALV = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRFLXCNS = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRCSTCAL = models.CharField(max_length=100, null=True)
    VLRBNF = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRCPLCSTPCO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPCOBSEMER = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    CODREGPCO = models.CharField(max_length=20, null=True)
    NUMRLCCIDGIR = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    TIPCALUTZPCOLIQ = models.CharField(max_length=100, null=True)
    
class DiretrizesEstrategica(models.Model):

    class Meta:
        db_table = "mrt.CADDTZETT"

    CODESTUNI = models.CharField(max_length=2)
    CODDIVFRN = models.IntegerField()
    DATREFPOD = models.CharField(max_length=20, blank=True, null=True)
    NOMMES = models.CharField(max_length=20, blank=True, null=True) 
    NOMSMS = models.CharField(max_length=150, blank=True, null=True) 
    NOMDIASMN = models.CharField(max_length=150, blank=True, null=True) 
    NOMSMSANO = models.CharField(max_length=150, blank=True, null=True) 
    CODCLLCMPATU = models.IntegerField()
    DESCLLCMPATU = models.CharField(max_length=50, blank=True, null=True)
    CODDRTCLLATU = models.IntegerField()
    DESDRTCLLATU = models.CharField(max_length=150)
    VLRVNDFATLIQ = models.CharField(max_length=45)
    VLRRCTLIQAPU = models.CharField(max_length=45)
    VLRMRGCRB = models.CharField(max_length=45)
    VLRMRGBRT = models.CharField(max_length=45)
    NOMCPR = models.CharField(max_length=45)
    CODFIL = models.IntegerField(blank=True, null=True)
    INDCTGTOP = models.TextField(blank=True, null=True)  # Field name made lowercase.
    CODGRPMER = models.IntegerField(blank=True, null=True)
    DESGRPMER = models.CharField(max_length=45)
    CODFMLMER = models.IntegerField(blank=True, null=True)
    DESFMLMER = models.CharField(max_length=45)
    CODCLSMER = models.IntegerField(blank=True, null=True)
    DESCLSMER = models.CharField(max_length=45)
    CODDRTCLLATU = models.IntegerField()
    CODGRPFRN = models.IntegerField()
    NOMGRPFRN = models.CharField(max_length=150)
    NOMFRN = models.CharField(max_length=150)

class PlanoCompras(models.Model):

    class Meta: 
        db_table = 'mrt.MOVPLNCMPCAL' 

    CODESTUNI = models.CharField(max_length=2)
    CODFILEPD = models.IntegerField()
    CODFILFAT = models.IntegerField()
    CODPRD = models.IntegerField()
    NUMANOMESSMN = models.CharField(max_length=50)
    MRGBRTOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    # VLRRCTLIQCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRCSTCMPMER = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRCSTCMPIDL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRCMVOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRCMVOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRCMVCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    # VLRVLDCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRFLXPLN = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRFLXSUG = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRICMOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRICMCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRIMPTOTOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRIMPTOTCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRMRGBRTOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRMRGBRTCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPCOBSECAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPCOBSEOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRMCDOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRMCDCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRDVLCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPISOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPISCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPCOMEDMCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRVNDLIQOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRVNDLIQCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRVNDPRVCTR = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPCOVNDLIQOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPCOVNDLIQCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRVBAOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRRBTCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRRBTOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRCMVPCOATU = models.DecimalField(decimal_places=2, max_digits=10, null=True)   
    VLRRCTLIQOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True) 
    VLRDVLOCD = models.DecimalField(decimal_places=2, max_digits=10, null=True) 
