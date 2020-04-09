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
    verba_preço = models.FloatField(db_column='VERBA_PREÇO', blank=True, null=True)  # Field name made lowercase.
    fund_preço = models.BigIntegerField(db_column='FUND_PREÇO', blank=True, null=True)  # Field name made lowercase.
    rebate = models.FloatField(db_column='REBATE', blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    pis_cofins = models.FloatField(db_column='PIS_COFINS', blank=True, null=True)  # Field name made lowercase.
    devolução = models.FloatField(db_column='DEVOLUÇÃO', blank=True, null=True)  # Field name made lowercase.
    target = models.FloatField(db_column='TARGET', blank=True, null=True)  # Field name made lowercase.
    flex = models.BigIntegerField(db_column='FLEX', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='CUSTO', blank=True, null=True)  # Field name made lowercase.
    numrlccidgir = models.BigIntegerField(db_column='NUMRLCCIDGIR', blank=True, null=True)  # Field name made lowercase.
    bonificado = models.FloatField(db_column='BONIFICADO', blank=True, null=True)  # Field name made lowercase.
    complemento = models.FloatField(db_column='COMPLEMENTO', blank=True, null=True)  # Field name made lowercase.
    precobase = models.BigIntegerField(db_column='PRECOBASE', blank=True, null=True)  # Field name made lowercase.
    data_preço = models.TextField(db_column='DATA_PREÇO', blank=True, null=True)  # Field name made lowercase.
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
    nomeregião = models.TextField(db_column='NOMEREGIÃO', blank=True, null=True)  # Field name made lowercase.
    tipo_calculo_preço = models.TextField(db_column='TIPO_CALCULO_PREÇO', blank=True, null=True)  # Field name made lowercase.
    preço_livro = models.FloatField(db_column='PREÇO_LIVRO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BASE_PRECO'


class Campo(models.Model):
    cod_campo = models.CharField(primary_key=True, max_length=10)
    nome_campo = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'CAMPO'


class Competitividade(models.Model):
    id = models.TextField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    chave = models.TextField(blank=True, null=True)
    data_emissao = models.TextField(blank=True, null=True)
    natop = models.TextField(db_column='natOp', blank=True, null=True)  # Field name made lowercase.
    cfop = models.FloatField(blank=True, null=True)
    opcao = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    cnpj_emitente = models.FloatField(db_column='CNPJ_Emitente', blank=True, null=True)  # Field name made lowercase.
    xnome_emitente = models.TextField(db_column='xNome_Emitente', blank=True, null=True)  # Field name made lowercase.
    uf_emitente_emitente = models.TextField(db_column='UF_Emitente_Emitente', blank=True, null=True)  # Field name made lowercase.
    uf_destino = models.TextField(db_column='UF_Destino', blank=True, null=True)  # Field name made lowercase.
    cprod = models.TextField(db_column='cProd', blank=True, null=True)  # Field name made lowercase.
    xprod = models.TextField(db_column='xProd', blank=True, null=True)  # Field name made lowercase.
    ncm = models.FloatField(db_column='NCM', blank=True, null=True)  # Field name made lowercase.
    ceantrib = models.BigIntegerField(db_column='cEANTrib', blank=True, null=True)  # Field name made lowercase.
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    codsml = models.BigIntegerField(db_column='CODSML', blank=True, null=True)  # Field name made lowercase.
    unicx = models.FloatField(blank=True, null=True)
    embcxa = models.FloatField(db_column='EmbCxa', blank=True, null=True)  # Field name made lowercase.
    mrt_unidvda = models.BigIntegerField(db_column='mrt_unidVda', blank=True, null=True)  # Field name made lowercase.
    mrt_unidcxfrn = models.BigIntegerField(db_column='mrt_unidCxFrn', blank=True, null=True)  # Field name made lowercase.
    qtrib = models.FloatField(db_column='qTrib', blank=True, null=True)  # Field name made lowercase.
    vuntrib = models.TextField(db_column='vUnTrib', blank=True, null=True)  # Field name made lowercase.
    pc_mrt = models.TextField(blank=True, null=True)
    pc_psq = models.FloatField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    diretoria_compras = models.TextField(blank=True, null=True)
    celula = models.TextField(blank=True, null=True)
    codfrn = models.BigIntegerField(blank=True, null=True)
    fornecedor = models.TextField(blank=True, null=True)
    grupo_produto = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    subcategoria = models.TextField(blank=True, null=True)
    produto = models.TextField(blank=True, null=True)
    descricao_similar = models.TextField(blank=True, null=True)
    mix = models.TextField(db_column='Mix', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    regiao = models.TextField(blank=True, null=True)
    pc_psq_pond = models.FloatField(blank=True, null=True)
    pc_mrt_pond = models.FloatField(blank=True, null=True)
    abc = models.TextField(db_column='ABC', blank=True, null=True)  # Field name made lowercase.
    categorizado = models.TextField(blank=True, null=True)
    status_fornecedor = models.TextField(db_column='Status_Fornecedor', blank=True, null=True)  # Field name made lowercase.
    comp = models.FloatField(db_column='Comp', blank=True, null=True)  # Field name made lowercase.
    tipopesquisa = models.TextField(db_column='TipoPesquisa', blank=True, null=True)  # Field name made lowercase.
    numano = models.BigIntegerField(db_column='NUMANO', blank=True, null=True)  # Field name made lowercase.
    numanomes = models.BigIntegerField(db_column='NUMANOMES', blank=True, null=True)  # Field name made lowercase.
    numsmnano = models.BigIntegerField(db_column='NUMSMNANO', blank=True, null=True)  # Field name made lowercase.
    nommes = models.TextField(db_column='NOMMES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMPETITIVIDADE'


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
    codstaprdetq = models.CharField(db_column='CODSTAPRDETQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
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


class Movplncmpcal1(models.Model):
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
    vrbuntsugsug = models.FloatField(db_column='VRBUNTSUGSUG', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'MOVPLNCMPCAL1'


class Movvbaprecal1(models.Model):
    cmvreal = models.FloatField(db_column='CMVREAL', blank=True, null=True)  # Field name made lowercase.
    codctgprd = models.BigIntegerField(db_column='CODCTGPRD', blank=True, null=True)  # Field name made lowercase.
    coddivfrn = models.BigIntegerField(db_column='CODDIVFRN', blank=True, null=True)  # Field name made lowercase.
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
    codfilepd = models.BigIntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.BigIntegerField(db_column='CODFILFAT', blank=True, null=True)  # Field name made lowercase.
    codgrpprd = models.BigIntegerField(db_column='CODGRPPRD', blank=True, null=True)  # Field name made lowercase.
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    codsubctgprd = models.BigIntegerField(db_column='CODSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    datref = models.DateTimeField(db_column='DATREF', blank=True, null=True)  # Field name made lowercase.
    fundingmedreal = models.FloatField(db_column='FUNDINGMEDREAL', blank=True, null=True)  # Field name made lowercase.
    month = models.FloatField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperotm = models.FloatField(db_column='MRGBRTPEROTM', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperpln = models.FloatField(db_column='MRGBRTPERPLN', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperreal = models.FloatField(db_column='MRGBRTPERREAL', blank=True, null=True)  # Field name made lowercase.
    qdediasmn = models.BigIntegerField(db_column='QDEDIASMN', blank=True, null=True)  # Field name made lowercase.
    vlrcmvpcopln = models.FloatField(db_column='VLRCMVPCOPLN', blank=True, null=True)  # Field name made lowercase.
    vlrcompreal = models.FloatField(db_column='VLRCOMPREAL', blank=True, null=True)  # Field name made lowercase.
    vlrcompotm = models.FloatField(db_column='VLRCOMPOTM', blank=True, null=True)  # Field name made lowercase.
    vlrcomppln = models.FloatField(db_column='VLRCOMPPLN', blank=True, null=True)  # Field name made lowercase.
    vlrpcootm = models.FloatField(db_column='VLRPCOOTM', blank=True, null=True)  # Field name made lowercase.
    vlrpcopln = models.FloatField(db_column='VLRPCOPLN', blank=True, null=True)  # Field name made lowercase.
    vlrpcoreal = models.FloatField(db_column='VLRPCOREAL', blank=True, null=True)  # Field name made lowercase.
    vlrvrbnsc = models.FloatField(db_column='VLRVRBNSC', blank=True, null=True)  # Field name made lowercase.
    vlrvrbpln = models.FloatField(db_column='VLRVRBPLN', blank=True, null=True)  # Field name made lowercase.
    vlrvrbtotnsc = models.FloatField(db_column='VLRVRBTOTNSC', blank=True, null=True)  # Field name made lowercase.
    volvndotm = models.FloatField(db_column='VOLVNDOTM', blank=True, null=True)  # Field name made lowercase.
    volvndpln = models.FloatField(db_column='VOLVNDPLN', blank=True, null=True)  # Field name made lowercase.
    volvndreal = models.FloatField(db_column='VOLVNDREAL', blank=True, null=True)  # Field name made lowercase.
    week = models.TextField(db_column='WEEK', blank=True, null=True)  # Field name made lowercase.
    year = models.FloatField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVVBAPRECAL1'


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
    valor_unitario_promoção = models.FloatField(db_column='VALOR_UNITARIO_PROMOÇÃO', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_beneficio = models.FloatField(db_column='VALOR_UNITARIO_BENEFICIO', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_funding_preco = models.FloatField(db_column='VALOR_UNITARIO_FUNDING_PRECO', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_funding_margem = models.FloatField(db_column='VALOR_UNITARIO_FUNDING_MARGEM', blank=True, null=True)  # Field name made lowercase.
    valor_total_promoção = models.FloatField(db_column='VALOR_TOTAL_PROMOÇÃO', blank=True, null=True)  # Field name made lowercase.
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


class OutputOtm(models.Model):
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
    devolução = models.FloatField(db_column='DEVOLUÇÃO', blank=True, null=True)  # Field name made lowercase.
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
    numanomes = models.FloatField(db_column='NUMANOMES', blank=True, null=True)  # Field name made lowercase.
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
    vlrrctliqpln = models.FloatField(db_column='VLRRCTLIQPLN', blank=True, null=True)  # Field name made lowercase.
    mrgbrtpln = models.FloatField(db_column='MRGBRTPLN', blank=True, null=True)  # Field name made lowercase.
    volvndreal = models.FloatField(db_column='VOLVNDREAL', blank=True, null=True)  # Field name made lowercase.
    vlrrctliqreal = models.FloatField(db_column='VLRRCTLIQREAL', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperreal = models.FloatField(db_column='MRGBRTPERREAL', blank=True, null=True)  # Field name made lowercase.
    mrgbrtreal = models.FloatField(db_column='MRGBRTREAL', blank=True, null=True)  # Field name made lowercase.
    vlrpcoreal = models.FloatField(db_column='VLRPCOREAL', blank=True, null=True)  # Field name made lowercase.
    qdtreal = models.FloatField(db_column='QDTREAL', blank=True, null=True)  # Field name made lowercase.
    cmvreal = models.FloatField(db_column='CMVREAL', blank=True, null=True)  # Field name made lowercase.
    fundingmedreal = models.FloatField(db_column='FUNDINGMEDREAL', blank=True, null=True)  # Field name made lowercase.
    datref = models.DateTimeField(db_column='DATREF', blank=True, null=True)  # Field name made lowercase.
    volvndgap = models.FloatField(db_column='VOLVNDGAP', blank=True, null=True)  # Field name made lowercase.
    mrgbrtgap = models.FloatField(db_column='MRGBRTGAP', blank=True, null=True)  # Field name made lowercase.
    vlrrctliqgap = models.FloatField(db_column='VLRRCTLIQGAP', blank=True, null=True)  # Field name made lowercase.
    mrgbrtpergap = models.FloatField(db_column='MRGBRTPERGAP', blank=True, null=True)  # Field name made lowercase.
    need_funding = models.BigIntegerField(db_column='NEED_FUNDING', blank=True, null=True)  # Field name made lowercase.
    volvndotm = models.FloatField(db_column='VOLVNDOTM', blank=True, null=True)  # Field name made lowercase.
    mrgbrtotm = models.FloatField(db_column='MRGBRTOTM', blank=True, null=True)  # Field name made lowercase.
    vlrpcootm = models.FloatField(db_column='VLRPCOOTM', blank=True, null=True)  # Field name made lowercase.
    rctliqotm = models.FloatField(db_column='RCTLIQOTM', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperotm = models.FloatField(db_column='MRGBRTPEROTM', blank=True, null=True)  # Field name made lowercase.
    vlrvrbnsc = models.FloatField(db_column='VLRVRBNSC', blank=True, null=True)  # Field name made lowercase.
    vlrvrbtotnsc = models.FloatField(db_column='VLRVRBTOTNSC', blank=True, null=True)  # Field name made lowercase.
    rprvrb = models.BigIntegerField(db_column='RPRVRB', blank=True, null=True)  # Field name made lowercase.
    vlrcompotm = models.FloatField(db_column='VLRCOMPOTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OUTPUT_OTM'


class OutputOtm1(models.Model):
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
    devolução = models.FloatField(db_column='DEVOLUÇÃO', blank=True, null=True)  # Field name made lowercase.
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
    numanomes = models.FloatField(db_column='NUMANOMES', blank=True, null=True)  # Field name made lowercase.
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
    vlrrctliqpln = models.FloatField(db_column='VLRRCTLIQPLN', blank=True, null=True)  # Field name made lowercase.
    mrgbrtpln = models.FloatField(db_column='MRGBRTPLN', blank=True, null=True)  # Field name made lowercase.
    volvndreal = models.FloatField(db_column='VOLVNDREAL', blank=True, null=True)  # Field name made lowercase.
    vlrrctliqreal = models.FloatField(db_column='VLRRCTLIQREAL', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperreal = models.FloatField(db_column='MRGBRTPERREAL', blank=True, null=True)  # Field name made lowercase.
    mrgbrtreal = models.FloatField(db_column='MRGBRTREAL', blank=True, null=True)  # Field name made lowercase.
    vlrpcoreal = models.FloatField(db_column='VLRPCOREAL', blank=True, null=True)  # Field name made lowercase.
    qdtreal = models.FloatField(db_column='QDTREAL', blank=True, null=True)  # Field name made lowercase.
    cmvreal = models.FloatField(db_column='CMVREAL', blank=True, null=True)  # Field name made lowercase.
    fundingmedreal = models.FloatField(db_column='FUNDINGMEDREAL', blank=True, null=True)  # Field name made lowercase.
    datref = models.DateTimeField(db_column='DATREF', blank=True, null=True)  # Field name made lowercase.
    vlrcompreal = models.FloatField(db_column='VLRCOMPREAL', blank=True, null=True)  # Field name made lowercase.
    volvndgap = models.FloatField(db_column='VOLVNDGAP', blank=True, null=True)  # Field name made lowercase.
    mrgbrtgap = models.FloatField(db_column='MRGBRTGAP', blank=True, null=True)  # Field name made lowercase.
    vlrrctliqgap = models.FloatField(db_column='VLRRCTLIQGAP', blank=True, null=True)  # Field name made lowercase.
    mrgbrtpergap = models.FloatField(db_column='MRGBRTPERGAP', blank=True, null=True)  # Field name made lowercase.
    need_funding = models.BigIntegerField(db_column='NEED_FUNDING', blank=True, null=True)  # Field name made lowercase.
    volvndotm = models.FloatField(db_column='VOLVNDOTM', blank=True, null=True)  # Field name made lowercase.
    mrgbrtotm = models.FloatField(db_column='MRGBRTOTM', blank=True, null=True)  # Field name made lowercase.
    vlrpcootm = models.FloatField(db_column='VLRPCOOTM', blank=True, null=True)  # Field name made lowercase.
    rctliqotm = models.FloatField(db_column='RCTLIQOTM', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperotm = models.FloatField(db_column='MRGBRTPEROTM', blank=True, null=True)  # Field name made lowercase.
    vlrvrbnsc = models.FloatField(db_column='VLRVRBNSC', blank=True, null=True)  # Field name made lowercase.
    vlrvrbtotnsc = models.FloatField(db_column='VLRVRBTOTNSC', blank=True, null=True)  # Field name made lowercase.
    rprvrb = models.FloatField(db_column='RPRVRB', blank=True, null=True)  # Field name made lowercase.
    vlrcompotm = models.FloatField(db_column='VLRCOMPOTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OUTPUT_OTM1'


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
    devolução = models.FloatField(db_column='DEVOLUÇÃO', blank=True, null=True)  # Field name made lowercase.
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


class OutputPln1(models.Model):
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
    flex = models.FloatField(db_column='FLEX', blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    pis_cofins = models.FloatField(db_column='PIS_COFINS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.FloatField(db_column='COMPLEMENTO', blank=True, null=True)  # Field name made lowercase.
    devolução = models.FloatField(db_column='DEVOLUÇÃO', blank=True, null=True)  # Field name made lowercase.
    verbapco = models.FloatField(db_column='VerbaPco', blank=True, null=True)  # Field name made lowercase.
    bonificado = models.FloatField(db_column='Bonificado', blank=True, null=True)  # Field name made lowercase.
    rebate = models.FloatField(db_column='Rebate', blank=True, null=True)  # Field name made lowercase.
    fundpco = models.FloatField(db_column='FundPco', blank=True, null=True)  # Field name made lowercase.
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
    vrbuntsugsug = models.FloatField(db_column='VRBUNTSUGSUG', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'OUTPUT_PLN1'


class OutputPln2(models.Model):
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    codfilepd = models.BigIntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.BigIntegerField(db_column='CODFILFAT', blank=True, null=True)  # Field name made lowercase.
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
    codsubctgprd = models.BigIntegerField(db_column='CODSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codctgprd = models.BigIntegerField(db_column='CODCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codgrpprd = models.BigIntegerField(db_column='CODGRPPRD', blank=True, null=True)  # Field name made lowercase.
    coddivfrn = models.BigIntegerField(db_column='CODDIVFRN', blank=True, null=True)  # Field name made lowercase.
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
    flex = models.FloatField(db_column='FLEX', blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    pis_cofins = models.FloatField(db_column='PIS_COFINS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.FloatField(db_column='COMPLEMENTO', blank=True, null=True)  # Field name made lowercase.
    devolução = models.FloatField(db_column='DEVOLUÇÃO', blank=True, null=True)  # Field name made lowercase.
    verbapco = models.FloatField(db_column='VerbaPco', blank=True, null=True)  # Field name made lowercase.
    bonificado = models.FloatField(db_column='Bonificado', blank=True, null=True)  # Field name made lowercase.
    rebate = models.FloatField(db_column='Rebate', blank=True, null=True)  # Field name made lowercase.
    fundpco = models.FloatField(db_column='FundPco', blank=True, null=True)  # Field name made lowercase.
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
    vrbuntsugsug = models.FloatField(db_column='VRBUNTSUGSUG', blank=True, null=True)  # Field name made lowercase.
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
    numanomessmn = models.TextField(db_column='NUMANOMESSMN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OUTPUT_PLN2'


class OutputPln3(models.Model):
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    codfilepd = models.BigIntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.BigIntegerField(db_column='CODFILFAT', blank=True, null=True)  # Field name made lowercase.
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
    codsubctgprd = models.BigIntegerField(db_column='CODSUBCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codctgprd = models.BigIntegerField(db_column='CODCTGPRD', blank=True, null=True)  # Field name made lowercase.
    codgrpprd = models.BigIntegerField(db_column='CODGRPPRD', blank=True, null=True)  # Field name made lowercase.
    coddivfrn = models.BigIntegerField(db_column='CODDIVFRN', blank=True, null=True)  # Field name made lowercase.
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
    flex = models.FloatField(db_column='FLEX', blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    pis_cofins = models.FloatField(db_column='PIS_COFINS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.FloatField(db_column='COMPLEMENTO', blank=True, null=True)  # Field name made lowercase.
    devolução = models.FloatField(db_column='DEVOLUÇÃO', blank=True, null=True)  # Field name made lowercase.
    verbapco = models.FloatField(db_column='VerbaPco', blank=True, null=True)  # Field name made lowercase.
    bonificado = models.FloatField(db_column='Bonificado', blank=True, null=True)  # Field name made lowercase.
    rebate = models.FloatField(db_column='Rebate', blank=True, null=True)  # Field name made lowercase.
    fundpco = models.FloatField(db_column='FundPco', blank=True, null=True)  # Field name made lowercase.
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
    vrbuntsugsug = models.FloatField(db_column='VRBUNTSUGSUG', blank=True, null=True)  # Field name made lowercase.
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
    numanomessmn = models.TextField(db_column='NUMANOMESSMN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OUTPUT_PLN3'


class ResultPln(models.Model):
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    codfilepd = models.BigIntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.BigIntegerField(db_column='CODFILFAT', blank=True, null=True)  # Field name made lowercase.
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
    numanomessmn = models.TextField(db_column='NUMANOMESSMN', blank=True, null=True)  # Field name made lowercase.
    volvndsug = models.FloatField(db_column='VOLVNDSUG', blank=True, null=True)  # Field name made lowercase.
    volvndsugalc = models.FloatField(db_column='VOLVNDSUGALC', blank=True, null=True)  # Field name made lowercase.
    mrgbrtocd = models.FloatField(db_column='MRGBRTOCD', blank=True, null=True)  # Field name made lowercase.
    vlrrctliqocd = models.FloatField(db_column='VLRRCTLIQOCD', blank=True, null=True)  # Field name made lowercase.
    mrgbrtperocd = models.FloatField(db_column='MRGBRTPEROCD', blank=True, null=True)  # Field name made lowercase.
    vlrpcosug = models.FloatField(db_column='VLRPCOSUG', blank=True, null=True)  # Field name made lowercase.
    vlrpcobasesug = models.FloatField(db_column='VLRPCOBASESUG', blank=True, null=True)  # Field name made lowercase.
    vlrimptotsug = models.FloatField(db_column='VLRIMPTOTSUG', blank=True, null=True)  # Field name made lowercase.
    vlricmssug = models.FloatField(db_column='VLRICMSSUG', blank=True, null=True)  # Field name made lowercase.
    vlrpiscofsug = models.FloatField(db_column='VLRPISCOFSUG', blank=True, null=True)  # Field name made lowercase.
    vlrdevsug = models.FloatField(db_column='VLRDEVSUG', blank=True, null=True)  # Field name made lowercase.
    vlrflxsug = models.FloatField(db_column='VLRFLXSUG', blank=True, null=True)  # Field name made lowercase.
    vlrmrgbrtsug = models.FloatField(db_column='VLRMRGBRTSUG', blank=True, null=True)  # Field name made lowercase.
    vrbuntsugsug = models.FloatField(db_column='VRBUNTSUGSUG', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'RESULT_PLN'


class ResultPln3(models.Model):
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    codfilepd = models.BigIntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.BigIntegerField(db_column='CODFILFAT', blank=True, null=True)  # Field name made lowercase.
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
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
    vrbuntsugsug = models.FloatField(db_column='VRBUNTSUGSUG', blank=True, null=True)  # Field name made lowercase.
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
    numanomessmn = models.TextField(db_column='NUMANOMESSMN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESULT_PLN3'


class ComposicaoPreco(models.Model):
    codprd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    desprd = models.TextField(blank=True, null=True)
    abc = models.TextField(blank=True, null=True)
    sensivel_rebate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipedereg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    codedereg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    codfilemp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    codfilfat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mb_calculada = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verba_preco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fund_preco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rebate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    icms = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pis_cofins = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    devolucao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    target = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    flex = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cmv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bonificado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    complemento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    precobase = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_preco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    codestuni = models.TextField(blank=True, null=True)
    preco_livro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'composicao_preco'


class DiretrizEstrategica(models.Model):
    datini = models.TextField(blank=True, null=True)
    coddrtcllatu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    desdrtcllatu = models.TextField(blank=True, null=True)
    codcllcmpatu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    descllcmpatu = models.TextField(blank=True, null=True)
    nomfnccpratu = models.TextField(blank=True, null=True)
    codgrpprd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    desgrpprd = models.TextField(blank=True, null=True)
    codctgprd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    desctgprd = models.TextField(blank=True, null=True)
    codsubctgprd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dessubctgprd = models.TextField(blank=True, null=True)
    codgrpecofrn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nomgrpecofrn = models.TextField(blank=True, null=True)
    coddivfrn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    desdivfrn = models.TextField(blank=True, null=True)
    codestuni = models.TextField(blank=True, null=True)
    nomestuni = models.TextField(blank=True, null=True)
    vlrvndfatliq = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vlrrctliqapu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vlrmrgcrb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vlrmrgbrt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nomreggeo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diretriz_estrategica'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class MrtCaddtzett(models.Model):
    codestuni = models.CharField(db_column='CODESTUNI', max_length=2)  # Field name made lowercase.
    coddivfrn = models.IntegerField(db_column='CODDIVFRN')  # Field name made lowercase.
    datrefpod = models.CharField(db_column='DATREFPOD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nommes = models.CharField(db_column='NOMMES', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nomsms = models.CharField(db_column='NOMSMS', max_length=150, blank=True, null=True)  # Field name made lowercase.
    nomdiasmn = models.CharField(db_column='NOMDIASMN', max_length=150, blank=True, null=True)  # Field name made lowercase.
    nomsmsano = models.CharField(db_column='NOMSMSANO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    codcllcmpatu = models.IntegerField(db_column='CODCLLCMPATU')  # Field name made lowercase.
    descllcmpatu = models.CharField(db_column='DESCLLCMPATU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    desdrtcllatu = models.CharField(db_column='DESDRTCLLATU', max_length=150)  # Field name made lowercase.
    vlrvndfatliq = models.CharField(db_column='VLRVNDFATLIQ', max_length=45)  # Field name made lowercase.
    vlrrctliqapu = models.CharField(db_column='VLRRCTLIQAPU', max_length=45)  # Field name made lowercase.
    vlrmrgcrb = models.CharField(db_column='VLRMRGCRB', max_length=45)  # Field name made lowercase.
    vlrmrgbrt = models.CharField(db_column='VLRMRGBRT', max_length=45)  # Field name made lowercase.
    nomcpr = models.CharField(db_column='NOMCPR', max_length=45)  # Field name made lowercase.
    codfil = models.IntegerField(db_column='CODFIL', blank=True, null=True)  # Field name made lowercase.
    codgrpmer = models.IntegerField(db_column='CODGRPMER', blank=True, null=True)  # Field name made lowercase.
    desgrpmer = models.CharField(db_column='DESGRPMER', max_length=45)  # Field name made lowercase.
    codfmlmer = models.IntegerField(db_column='CODFMLMER', blank=True, null=True)  # Field name made lowercase.
    desfmlmer = models.CharField(db_column='DESFMLMER', max_length=45)  # Field name made lowercase.
    codclsmer = models.IntegerField(db_column='CODCLSMER', blank=True, null=True)  # Field name made lowercase.
    desclsmer = models.CharField(db_column='DESCLSMER', max_length=45)  # Field name made lowercase.
    coddrtcllatu = models.IntegerField(db_column='CODDRTCLLATU')  # Field name made lowercase.
    nomgrpfrn = models.CharField(db_column='NOMGRPFRN', max_length=150)  # Field name made lowercase.
    nomfrn = models.CharField(db_column='NOMFRN', max_length=150)  # Field name made lowercase.
    indctgtop = models.TextField(db_column='INDCTGTOP', blank=True, null=True)  # Field name made lowercase.
    codgrpfrn = models.IntegerField(db_column='CODGRPFRN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mrt.CADDTZETT'


class MrtMovpcobsecal(models.Model):
    codprd = models.IntegerField(db_column='CODPRD')  # Field name made lowercase.
    codfilepd = models.IntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.IntegerField(db_column='CODFILFAT')  # Field name made lowercase.
    datref = models.CharField(db_column='DATREF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codestuni = models.CharField(db_column='CODESTUNI', max_length=2)  # Field name made lowercase.
    tipedereg = models.IntegerField(db_column='TIPEDEREG')  # Field name made lowercase.
    vlrmrgbrt = models.DecimalField(db_column='VLRMRGBRT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrvba = models.DecimalField(db_column='VLRVBA', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrfnd = models.DecimalField(db_column='VLRFND', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrfndrbtite = models.DecimalField(db_column='VLRFNDRBTITE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlricm = models.DecimalField(db_column='VLRICM', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrpis = models.DecimalField(db_column='VLRPIS', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrdvl = models.DecimalField(db_column='VLRDVL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlruntpcoalv = models.DecimalField(db_column='VLRUNTPCOALV', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrflxcns = models.DecimalField(db_column='VLRFLXCNS', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrcstcal = models.CharField(db_column='VLRCSTCAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vlrbnf = models.DecimalField(db_column='VLRBNF', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrcplcstpco = models.DecimalField(db_column='VLRCPLCSTPCO', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrpcobsemer = models.DecimalField(db_column='VLRPCOBSEMER', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    codregpco = models.CharField(db_column='CODREGPCO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numrlccidgir = models.DecimalField(db_column='NUMRLCCIDGIR', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipcalutzpcoliq = models.CharField(db_column='TIPCALUTZPCOLIQ', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mrt.MOVPCOBSECAL'


class MrtMovpcomcd(models.Model):
    codprd = models.IntegerField(db_column='CODPRD')  # Field name made lowercase.
    codidtcur = models.IntegerField(db_column='CODIDTCUR', primary_key=True)  # Field name made lowercase.
    codestuni = models.CharField(db_column='CODESTUNI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numano = models.DateTimeField(db_column='NUMANO')  # Field name made lowercase.
    numanomes = models.DateTimeField(db_column='NUMANOMES')  # Field name made lowercase.
    numsmnano = models.DateTimeField(db_column='NUMSMNANO')  # Field name made lowercase.
    nommes = models.DateTimeField(db_column='NOMMES')  # Field name made lowercase.
    datref = models.DateTimeField(db_column='DATREF')  # Field name made lowercase.
    codsml = models.IntegerField(db_column='CODSML')  # Field name made lowercase.
    desgrpmersmr = models.CharField(db_column='DESGRPMERSMR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    codtipapu = models.CharField(db_column='CODTIPAPU', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vlrpcomedmcd = models.DecimalField(db_column='VLRPCOMEDMCD', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrpcobsemer = models.DecimalField(db_column='VLRPCOBSEMER', max_digits=10, decimal_places=2)  # Field name made lowercase.
    clfcrvabcmer = models.CharField(db_column='CLFCRVABCMER', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mrt.MOVPCOMCD'


class MrtMovplncmpcal(models.Model):
    codestuni = models.TextField(db_column='CODESTUNI', blank=True, null=True)  # Field name made lowercase.
    codfilepd = models.BigIntegerField(db_column='CODFILEPD', blank=True, null=True)  # Field name made lowercase.
    codfilfat = models.BigIntegerField(db_column='CODFILFAT', blank=True, null=True)  # Field name made lowercase.
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    numanomessmn = models.TextField(db_column='NUMANOMESSMN', blank=True, null=True)  # Field name made lowercase.
    mrgbrtocd = models.FloatField(db_column='MRGBRTOCD', blank=True, null=True)  # Field name made lowercase.
    vlrrctliqcal = models.FloatField(db_column='VLRRCTLIQCAL', blank=True, null=True)  # Field name made lowercase.
    vlrcstcmpmer = models.FloatField(db_column='VLRCSTCMPMER', blank=True, null=True)  # Field name made lowercase.
    vlrcstcmpidl = models.FloatField(db_column='VLRCSTCMPIDL', blank=True, null=True)  # Field name made lowercase.
    vlrcmvocd = models.FloatField(db_column='VLRCMVOCD', blank=True, null=True)  # Field name made lowercase.
    vlrcmvcal = models.FloatField(db_column='VLRCMVCAL', blank=True, null=True)  # Field name made lowercase.
    vlrmcdocd = models.FloatField(db_column='VLRMCDOCD', blank=True, null=True)  # Field name made lowercase.
    vlrmcdcal = models.FloatField(db_column='VLRMCDCAL', blank=True, null=True)  # Field name made lowercase.
    vlrdvlocd = models.FloatField(db_column='VLRDVLOCD', blank=True, null=True)  # Field name made lowercase.
    vlrvldcal = models.FloatField(db_column='VLRVLDCAL', blank=True, null=True)  # Field name made lowercase.
    vlrflxpln = models.FloatField(db_column='VLRFLXPLN', blank=True, null=True)  # Field name made lowercase.
    vlrflxsug = models.FloatField(db_column='VLRFLXSUG', blank=True, null=True)  # Field name made lowercase.
    vlricmocd = models.FloatField(db_column='VLRICMOCD', blank=True, null=True)  # Field name made lowercase.
    vlricmcal = models.FloatField(db_column='VLRICMCAL', blank=True, null=True)  # Field name made lowercase.
    vlrimptotocd = models.FloatField(db_column='VLRIMPTOTOCD', blank=True, null=True)  # Field name made lowercase.
    vlrimptotcal = models.FloatField(db_column='VLRIMPTOTCAL', blank=True, null=True)  # Field name made lowercase.
    vlrmrgbrtocd = models.FloatField(db_column='VLRMRGBRTOCD', blank=True, null=True)  # Field name made lowercase.
    vlrmrgbrtcal = models.FloatField(db_column='VLRMRGBRTCAL', blank=True, null=True)  # Field name made lowercase.
    vlrpcobseocd = models.FloatField(db_column='VLRPCOBSEOCD', blank=True, null=True)  # Field name made lowercase.
    vlrpcobsecal = models.FloatField(db_column='VLRPCOBSECAL', blank=True, null=True)  # Field name made lowercase.
    vlrpcomedmcd = models.FloatField(db_column='VLRPCOMEDMCD', blank=True, null=True)  # Field name made lowercase.
    vlrpcovndliqocd = models.FloatField(db_column='VLRPCOVNDLIQOCD', blank=True, null=True)  # Field name made lowercase.
    vlrpcovndliqcal = models.FloatField(db_column='VLRPCOVNDLIQCAL', blank=True, null=True)  # Field name made lowercase.
    vlrpisocd = models.FloatField(db_column='VLRPISOCD', blank=True, null=True)  # Field name made lowercase.
    vlrpiscal = models.FloatField(db_column='VLRPISCAL', blank=True, null=True)  # Field name made lowercase.
    vlrvbaocd = models.FloatField(db_column='VLRVBAOCD', blank=True, null=True)  # Field name made lowercase.
    vlrvndliqocd = models.FloatField(db_column='VLRVNDLIQOCD', blank=True, null=True)  # Field name made lowercase.
    vlrvndliqcal = models.FloatField(db_column='VLRVNDLIQCAL', blank=True, null=True)  # Field name made lowercase.
    vlrvndprvctr = models.FloatField(db_column='VLRVNDPRVCTR', blank=True, null=True)  # Field name made lowercase.
    vlrrbtcal = models.FloatField(db_column='VLRRBTCAL', blank=True, null=True)  # Field name made lowercase.
    vlrrbtocd = models.FloatField(db_column='VLRRBTOCD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mrt.MOVPLNCMPCAL'


class MrtMovvarvndpco(models.Model):
    codprd = models.IntegerField(db_column='CODPRD')  # Field name made lowercase.
    codestuni = models.CharField(db_column='CODESTUNI', max_length=2)  # Field name made lowercase.
    codfilepd = models.IntegerField(db_column='CODFILEPD')  # Field name made lowercase.
    codfilfat = models.IntegerField(db_column='CODFILFAT')  # Field name made lowercase.
    vlrvarvndpco = models.DecimalField(db_column='VLRVARVNDPCO', max_digits=10, decimal_places=2)  # Field name made lowercase.
    desmer = models.CharField(db_column='DESMER', max_length=45)  # Field name made lowercase.
    clfcrvabcmer = models.CharField(db_column='CLFCRVABCMER', max_length=1)  # Field name made lowercase.
    codgrpmersmr = models.IntegerField(db_column='CODGRPMERSMR')  # Field name made lowercase.
    desgrpmersmr = models.CharField(db_column='DESGRPMERSMR', max_length=45)  # Field name made lowercase.
    desfmlmer = models.IntegerField(db_column='DESFMLMER')  # Field name made lowercase.
    desclsmer = models.CharField(db_column='DESCLSMER', max_length=45)  # Field name made lowercase.
    desdivcmp = models.CharField(db_column='DESDIVCMP', max_length=45)  # Field name made lowercase.
    desdrtcllatu = models.CharField(db_column='DESDRTCLLATU', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mrt.MOVVARVNDPCO'


class MrtMovvbadiscal(models.Model):
    codprd = models.IntegerField(db_column='CODPRD')  # Field name made lowercase.
    codfilepd = models.IntegerField(db_column='CODFILEPD')  # Field name made lowercase.
    vlrsldpcomesant = models.DecimalField(db_column='VLRSLDPCOMESANT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrcrdpco = models.DecimalField(db_column='VLRCRDPCO', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrdbtpco = models.DecimalField(db_column='VLRDBTPCO', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrsldmrgmesant = models.DecimalField(db_column='VLRSLDMRGMESANT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrcrdmrg = models.DecimalField(db_column='VLRCRDMRG', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrdbtmrg = models.DecimalField(db_column='VLRDBTMRG', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    datref = models.IntegerField(db_column='DATREF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mrt.MOVVBADISCAL'


class MrtMovvbahst(models.Model):
    codprd = models.IntegerField(db_column='CODPRD')  # Field name made lowercase.
    codfilepd = models.IntegerField(db_column='CODFILEPD')  # Field name made lowercase.
    codfilfat = models.IntegerField(db_column='CODFILFAT')  # Field name made lowercase.
    codcli = models.IntegerField(db_column='CODCLI')  # Field name made lowercase.
    codestcli = models.IntegerField(db_column='CODESTCLI')  # Field name made lowercase.
    numped = models.IntegerField(db_column='NUMPED')  # Field name made lowercase.
    numanomesdia = models.DateTimeField(db_column='NUMANOMESDIA')  # Field name made lowercase.
    qdeiteped = models.IntegerField(db_column='QDEITEPED')  # Field name made lowercase.
    vlrvndliq = models.DecimalField(db_column='VLRVNDLIQ', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlruntcstmer = models.DecimalField(db_column='VLRUNTCSTMER', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrcstmer = models.DecimalField(db_column='VLRCSTMER', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlruntfndmer = models.DecimalField(db_column='VLRUNTFNDMER', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrfnd = models.DecimalField(db_column='VLRFND', max_digits=10, decimal_places=2)  # Field name made lowercase.
    qdeitepmc = models.IntegerField(db_column='QDEITEPMC')  # Field name made lowercase.
    qdeitebfc = models.IntegerField(db_column='QDEITEBFC')  # Field name made lowercase.
    vlruntfndpmcvnd = models.DecimalField(db_column='VLRUNTFNDPMCVND', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlruntdscbfcite = models.DecimalField(db_column='VLRUNTDSCBFCITE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlruntfndpco = models.DecimalField(db_column='VLRUNTFNDPCO', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlruntfndmrg = models.DecimalField(db_column='VLRUNTFNDMRG', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrrlzpmc = models.DecimalField(db_column='VLRRLZPMC', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrbfc = models.DecimalField(db_column='VLRBFC', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrfndpcovnd = models.DecimalField(db_column='VLRFNDPCOVND', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrfndpcocst = models.DecimalField(db_column='VLRFNDPCOCST', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrmnsfndrcbfrn = models.DecimalField(db_column='VLRMNSFNDRCBFRN', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrrbtcal = models.DecimalField(db_column='VLRRBTCAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mrt.MOVVBAHST'


class MrtMovvndhstcal(models.Model):
    codprd = models.IntegerField(db_column='CODPRD')  # Field name made lowercase.
    codfilepd = models.IntegerField(db_column='CODFILEPD')  # Field name made lowercase.
    codfilfat = models.IntegerField(db_column='CODFILFAT')  # Field name made lowercase.
    codestcli = models.CharField(db_column='CODESTCLI', max_length=2)  # Field name made lowercase.
    codrepcmc = models.IntegerField(db_column='CODREPCMC')  # Field name made lowercase.
    numped = models.IntegerField(db_column='NUMPED')  # Field name made lowercase.
    numanomessmn = models.DateTimeField(db_column='NUMANOMESSMN')  # Field name made lowercase.
    numanomesdia = models.DateTimeField(db_column='NUMANOMESDIA')  # Field name made lowercase.
    vlrvndliq = models.DecimalField(db_column='VLRVNDLIQ', max_digits=10, decimal_places=2)  # Field name made lowercase.
    qdeite = models.IntegerField(db_column='QDEITE')  # Field name made lowercase.
    vlrdscflxcns = models.DecimalField(db_column='VLRDSCFLXCNS', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrsupflx = models.DecimalField(db_column='VLRSUPFLX', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrimptot = models.DecimalField(db_column='VLRIMPTOT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrrctliqapu = models.DecimalField(db_column='VLRRCTLIQAPU', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrcstmedprd = models.DecimalField(db_column='VLRCSTMEDPRD', max_digits=10, decimal_places=2)  # Field name made lowercase.
    permrgadicnlvnd = models.DecimalField(db_column='PERMRGADICNLVND', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrfnd = models.DecimalField(db_column='VLRFND', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrmrgbrt = models.DecimalField(db_column='VLRMRGBRT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrcsttrntnlcub = models.DecimalField(db_column='VLRCSTTRNTNLCUB', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrcstdtb = models.DecimalField(db_column='VLRCSTDTB', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrcstarg = models.DecimalField(db_column='VLRCSTARG', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vlrmrgcrb = models.DecimalField(db_column='VLRMRGCRB', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mrt.MOVVNDHSTCAL'


class Prdsml(models.Model):
    codprd = models.BigIntegerField(db_column='CODPRD', blank=True, null=True)  # Field name made lowercase.
    codsml = models.BigIntegerField(blank=True, null=True)
    dessml = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prdsml'


class PricingParsingPlanocompras(models.Model):
    codestuni = models.IntegerField(db_column='CODESTUNI')  # Field name made lowercase.
    codfilepd = models.IntegerField(db_column='CODFILEPD')  # Field name made lowercase.
    codfilfat = models.IntegerField(db_column='CODFILFAT')  # Field name made lowercase.
    codprd = models.IntegerField(db_column='CODPRD')  # Field name made lowercase.
    numanomessmn = models.CharField(db_column='NUMANOMESSMN', max_length=50)  # Field name made lowercase.
    mrgbrtocd = models.TextField(db_column='MRGBRTOCD')  # Field name made lowercase.
    vlrrctliqcal = models.DecimalField(db_column='VLRRCTLIQCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrcstcmpmer = models.DecimalField(db_column='VLRCSTCMPMER', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrcstcmpidl = models.DecimalField(db_column='VLRCSTCMPIDL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrcmvocd = models.DecimalField(db_column='VLRCMVOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrcmvcal = models.DecimalField(db_column='VLRCMVCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrdvlocd = models.DecimalField(db_column='VLRDVLOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrvldcal = models.DecimalField(db_column='VLRVLDCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrflxpln = models.DecimalField(db_column='VLRFLXPLN', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrflxsug = models.DecimalField(db_column='VLRFLXSUG', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlricmocd = models.DecimalField(db_column='VLRICMOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlricmcal = models.DecimalField(db_column='VLRICMCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrimptotocd = models.DecimalField(db_column='VLRIMPTOTOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrimptotcal = models.DecimalField(db_column='VLRIMPTOTCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrmrgbrtocd = models.DecimalField(db_column='VLRMRGBRTOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrmrgbrtcal = models.DecimalField(db_column='VLRMRGBRTCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrpcobseocd = models.DecimalField(db_column='VLRPCOBSEOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrpcobsecal = models.DecimalField(db_column='VLRPCOBSECAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrmcdocd = models.DecimalField(db_column='VLRMCDOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrmcdcal = models.DecimalField(db_column='VLRMCDCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrdvlcal = models.DecimalField(db_column='VLRDVLCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrpisocd = models.DecimalField(db_column='VLRPISOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrpiscal = models.DecimalField(db_column='VLRPISCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrpcomedmcd = models.DecimalField(db_column='VLRPCOMEDMCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrvndliqocd = models.DecimalField(db_column='VLRVNDLIQOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrvndliqcal = models.DecimalField(db_column='VLRVNDLIQCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrvndprvctr = models.DecimalField(db_column='VLRVNDPRVCTR', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrpcovndliqocd = models.DecimalField(db_column='VLRPCOVNDLIQOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrpcovndliqcal = models.DecimalField(db_column='VLRPCOVNDLIQCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrvbaocd = models.DecimalField(db_column='VLRVBAOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrrbtcal = models.DecimalField(db_column='VLRRBTCAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlrrbtocd = models.DecimalField(db_column='VLRRBTOCD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pricing_parsing_planocompras'
