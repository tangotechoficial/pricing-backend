from django.db import models


class Fornecedor(models.Model):
    """
    Model for table FORNECEDOR
    """

    class Meta:
        db_table = "FORNECEDOR"

    CODDIVFRN = models.IntegerField(primary_key=True)
    DESDIVFRN = models.CharField(max_length=45)
    CODGRPECOFRN = models.IntegerField()
    NOMGRPECOFRN = models.CharField(max_length=45)

class Comprador(models.Model):
    """
    Model for table COMPRADOR
    """

    class Meta:
        db_table = "COMPRADOR"

    CODCPRATU = models.IntegerField(primary_key=True)
    NOMCPRATU = models.CharField(max_length=45)
    CODCLLCMPATU = models.IntegerField()
    DESCLLCMPATU = models.CharField(max_length=45)
    CODDRTCLLATU = models.IntegerField()
    DESDRTCLLATU = models.CharField(max_length=45)

class TabAuxGrp(models.Model):
    """
    Model for table TAB_AUX_GRP
    """

    class Meta:
        db_table = "TAB_AUX_GRP"

    Id_Aux = models.IntegerField(primary_key=True)
    CODSUBCTGPRD = models.IntegerField()
    DESSUBCTGPRD = models.CharField(max_length=45)
    CODCTGPRD = models.IntegerField()
    DESCTGPRD = models.CharField(max_length=45)
    CODGRPPRD = models.IntegerField()
    DESGRPPRD = models.CharField(max_length=45)
    Linha_de_negocio = models.CharField(max_length=45)

class RelacionamentoFilialRegiao(models.Model):
    """
    Model for table RELACIONAMENTO_FILIAL_REGIAO
    """

    class Meta:
        db_table = 'RELACIONAMENTO_FILIAL_REGIAO'

    CODFILEPD = models.IntegerField(primary_key=True)
    NOMFILEPD = models.CharField(max_length=45)
    CODFILFAT = models.IntegerField()
    NOMFILFAT = models.CharField(max_length=45)
    CODESTUNI = models.CharField(max_length=2)
    NOMESTUNI = models.CharField(max_length=45)
    TIPEDEREG = models.IntegerField()
    CODEDEREG = models.IntegerField()


class Mercadoria(models.Model):
    """
    Model for table MERCADORIA
    """

    class Meta:
        db_table = "MERCADORIA"

    CODPRD = models.IntegerField(primary_key=True)
    Id_Aux = models.ManyToManyField(TabAuxGrp)
    DESPRD = models.CharField(max_length=45)
    CODDIVFRN = models.ForeignKey(Fornecedor)
    CODCPRATU = models.ForeignKey(Comprador)
    CODFIL = models.ForeignKey(RelacionamentoFilialRegiao)
    CODSML = models.IntegerField()
    dessml = models.CharField(max_length=45)
    ABC = models.CharField(max_length=1)

class Representante(models.Model):
    """
    Model for table REPRESENTANTE
    """

    class Meta:
        db_table = 'REPRESENTANTE'
    
    CODREPCMC = models.IntegerField(primary_key=True)
    NOMREPCMC = models.CharField(max_length=45)
    DATCADREPCMC = models.DateTimeField()

class Vendas(models.Model):
    """
    Model for table VENDAS
    """

    class Meta:
        db_table = 'VENDAS'

    CODPRD = models.ForeignKey(Mercadoria)
    CODFILEPD = models.ForeignKey(RelacionamentoFilialRegiao)
    CODFILFAT = models.IntegerField()
    CODESTCLI = models.IntegerField()
    CODREPCMC = models.ForeignKey(Representante)
    NUMPED = models.IntegerField()
    NUMANOMESSMN = models.DateTimeField()
    NUMANOMESDIA = models.DateTimeField()
    CMV = models.DecimalField(decimal_places=2, max_digits=10)
    QDEITE = models.DecimalField(decimal_places=2, max_digits=10)
    VLRVNDLIQ = models.DecimalField(decimal_places=2, max_digits=10)
    MARGEM_CONTRIBUICAO = models.DecimalField(decimal_places=2, max_digits=10)
    MARGEM_BRUTA = models.DecimalField(decimal_places=2, max_digits=10)
    VLRRCTLIQ = models.DecimalField(decimal_places=2, max_digits=10)
    VLRIMPTOT = models.DecimalField(decimal_places=2, max_digits=10)
    TRANSFERENCIA = models.DecimalField(decimal_places=2, max_digits=10)
    DISTRIBUICAO = models.DecimalField(decimal_places=2, max_digits=10)
    ARMAZENAGEM = models.DecimalField(decimal_places=2, max_digits=10)
    FUNDING = models.DecimalField(decimal_places=2, max_digits=10)
    VLRSUPFLX = models.DecimalField(decimal_places=2, max_digits=10)
    VLRDSCFLXCNS = models.DecimalField(decimal_places=2, max_digits=10)
    Despesas_Financeiras = models.DecimalField(decimal_places=2, max_digits=10)
    Margem_por_Segmento = models.DecimalField(decimal_places=2, max_digits=10)

class VerbaeBC(models.Model):
    """
    Model for table VERBA_E_BC
    """

    class Meta:
        db_table = 'VERBA_E_BC'

    CODPRD = models.ForeignKey(Mercadoria)
    CODFILEPD = models.ForeignKey(RelacionamentoFilialRegiao)
    CODFILFAT = models.IntegerField()
    CODESTCLI = models.IntegerField()
    NUMANOMESDIA = models.DateTimeField()
    QUANTIDADE_ITENS_PEDIDO = models.IntegerField()
    VALOR_TOTAL_VENDA_LIQUIDA = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_UNITARIO_CMV = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_TOTAL_CMV = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_UNITARIO_FUNDING = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_TOTAL_FUNDING = models.DecimalField(decimal_places=2, max_digits=10)
    QUANTIDADE_ITENS_PROMOCAO = models.IntegerField()
    QUANTIDADE_ITENS_BENEFICIO = models.IntegerField()
    VALOR_UNITARIO_PROMOCAO = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_UNITARIO_BENEFICIO = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_UNITARIO_FUNDING_PRECO = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_UNITARIO_FUNDING_MARGEM = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_TOTAL_PROMOCAO = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_TOTAL_BENEFICIO = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_TOTAL_FUNDING_PRECO = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_TOTAL_FUNDING_MARGEM = models.DecimalField(decimal_places=2, max_digits=10)
    VALOR_TOTAL_DMS_SANSUNG = models.DecimalField(decimal_places=2, max_digits=10)
    REBATE = models.DecimalField(decimal_places=2, max_digits=10)

class Elasticidade(models.Model):
    """
    Model for table ELASTICIDADE
    """

    class Meta:
        db_table = 'ELASTICIDADE'

    codsml = models.ForeignKey(Mercadoria)

    uf = models.CharField(max_length=2)
    Elasticidade = models.DecimalField(decimal_places=2, max_digits=10)
    qt = models.IntegerField()
    pcmed = models.DecimalField(decimal_places=2, max_digits=10)
    unitfnd = models.DecimalField(decimal_places=2, max_digits=10)
    verba = models.DecimalField(decimal_places=2, max_digits=10)

class Estoque(models.Model):
    """
    Model for table ESTOQUE
    """

    class Meta:
        db_table = 'ESTOQUE'

    CODPRD = models.ForeignKey(Mercadoria)
    CODFIL = models.ForeignKey(RelacionamentoFilialRegiao)
    DATINI = models.DateTimeField()
    NUMSMNANO = models.DateTimeField()
    NOMSMSANO = models.DateTimeField()
    NOMDIASMN = models.DateTimeField()
    NUMDIASMN = models.DateTimeField()
    NOMABVMESANO = models.CharField(max_length=45)
    VLRUNTCSTSCO = models.DecimalField(decimal_places=2, max_digits=10)
    QDEITEETQ = models.IntegerField()
    VLRVNDPDAFLTETQ = models.DecimalField(decimal_places=2, max_digits=10)
    QDEMEDVNDMNSMER = models.IntegerField()
    VLRCSTCMPIDL = models.DecimalField(decimal_places=2, max_digits=10)
    VLRMEDPCOCMP = models.DecimalField(decimal_places=2, max_digits=10)
    CODSTAPRDETQ = models.IntegerField()
    DESSTAPRDETQ = models.CharField(max_length=45)
    CODUNDREG = models.IntegerField()
    DESUNDREG = models.CharField(max_length=45)
    FLGUNDREG = models.CharField(max_length=45)

class Competitividade(models.Model):
    """
    Model for table COMPETITIVIDADE
    """

    class Meta:
        db_table = 'COMPETITIVIDADE'

    CODPRD = models.ForeignKey(Mercadoria)
    estado = models.CharField(max_length=2)
    NUMANOMES = models.DateTimeField()
    NUMSMNANO = models.DateTimeField()
    Id = models.IntegerField()
    data_emissao = models.DateTimeField()
    TipoPesquisa = models.CharField(max_length=45)
    pc_mrt = models.DecimalField(decimal_places=2, max_digits=10)
    pc_psq = models.DecimalField(decimal_places=2, max_digits=10)
    Comp = models.DecimalField(decimal_places=2, max_digits=10)
    pc_psq_pond = models.DecimalField(decimal_places=2, max_digits=10)
    pc_mrt_pond = models.DecimalField(decimal_places=2, max_digits=10)
    regiao = models.CharField(max_length=45)
    Uf_Destino = models.CharField(max_length=2)
    ABC = models.CharField(max_length=1)

class DadosMestre_Verba(models.Model):
    """
        Modelo de Tabela Dados Mestre
    """

    class Meta:
        db_table = "VERBA_DISPONIVEL"

    NUMANOMES = models.IntegerField()
    CODPRD = models.IntegerField()
    DESPRD = models.CharField(max_length=150)
    CODFILEPD = models.IntegerField()
    CODDIVFRN = models.IntegerField()
    VLRPRECOSALDOMESANTERIOR = models.DecimalField(decimal_places=2, max_digits=10)
    VLRPRECOCREDITO = models.DecimalField(decimal_places=2, max_digits=10)
    VLRPRECODEBITO = models.DecimalField(decimal_places=2, max_digits=10)
    VLRMARGEMSALDOMESANTERIOR = models.DecimalField(decimal_places=2, max_digits=10)
    VLRMARGEMCREDITO = models.DecimalField(decimal_places=2, max_digits=10)
    VLRMARGEMDEBITO = models.DecimalField(decimal_places=2, max_digits=10)

class DadosMestre_VerbaCSV(models.Model):
    import_date = models.DateTimeField(auto_now=True)
    csvfile = models.FileField()

class DadosMestre_ComposicaoPreco(models.Model):

    class Meta:
        db_table = "COMPOSICAO_PRECO"

    CODPRD = models.IntegerField()
    DESPRD = models.CharField(max_length=150)
    ABC = models.CharField(max_length=1)
    SENSIVEL_REBATE = models.SmallIntegerField()
    TIPEDEREG = models.IntegerField()
    CODEDEREG = models.IntegerField()
    CODFILEMP = models.IntegerField()
    CODFILFAT = models.IntegerField()
    MB = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    MB_CALCULADA = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VERBA_PRECO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    FUND_PRECO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    REBATE = models.DecimalField(decimal_places=6, max_digits=10, null=True)
    ICMS = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    PIS_COFINS = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    DEVOLUCAO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    TARGET = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    FLEX = models.IntegerField()
    CMV = models.DecimalField(decimal_places=3, max_digits=15, null=True)
    BONIFICADO = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    COMPLEMENTO = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    PRECOBASE = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    DATA_PRECO = models.DateTimeField()
    CODESTUNI = models.CharField(max_length=2)
    PRECO_LIVRO = models.DecimalField(decimal_places=2, max_digits=10, null=True)

class DadosMestre_ComposicaoPrecoCSV(models.Model):
    import_date = models.DateTimeField(auto_now=True)
    csvfile = models.FileField()

class DiretrizesEstrategica(models.Model):

    class Meta:
        db_table = "DIRETRIZ_ESTRATEGICA"

    Id_Aux = models.ForeignKey(TabAuxGrp)
    DATINI = models.DateTimeField()
    CODDRTCLLATU = models.IntegerField()
    DESDRTCLLATU = models.CharField(max_length=150)
    CODCLLCMPATU = models.IntegerField()
    DESCLLCMPATU = models.CharField(max_length=150)
    NOMFNCCPRATU = models.CharField(max_length=150)
    CODGRPPRD = models.IntegerField()
    DESGRPPRD = models.CharField(max_length=150)
    CODCTGPRD = models.IntegerField()
    DESCTGPRD = models.CharField(max_length=150)
    CODSUBCTGPRD = models.IntegerField()
    DESSUBCTGPRD = models.CharField(max_length=150)
    CODGRPECOFRN = models.IntegerField()
    NOMGRPECOFRN = models.CharField(max_length=150)
    CODDIVFRN = models.IntegerField()
    DESDIVFRN = models.CharField(max_length=150)
    CODESTUNI = models.CharField(max_length=3)
    NOMESTUNI = models.CharField(max_length=100)
    VLRVNDFATLIQ = models.CharField(max_length=100)
    VLRMRGBRT = models.CharField(max_length=100)
    NOMREGGEO = models.CharField(max_length=100)


class DiretrizesEstrategicaCSV(models.Model):
    import_date = models.DateTimeField(auto_now=True)
    csvfile = models.FileField()

class PlanoCompras(models.Model):

    class Meta:
        db_table = "PLANOCOMPRAS"

    CODPRD = models.IntegerField()
    CODFILEMP = models.IntegerField()
    CODFILFAT = models.IntegerField()
    DATA_PRECO = models.DateTimeField()
    CODESTUNI = models.IntegerField()
    META_VENDA_SUGERIDO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    META_VENDA_PLANEJADO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    PRECO_VENDA_LIQUIDO_SUGERIDO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    PRECO_VENDA_LIQUIDO_PLANEJADO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    COMPETITIVIDADE_SUGERIDO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    COMPETITIVIDADE_PLANEJADO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    PRECO_VENDA_BRUTA_SUGERIDO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    PRECO_VENDA_BRUTA_PLANEJADO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    PRECO_BASE_SUGERIDO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    PRECO_BASE_PLANEJADO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    REBATE_PLANEJADO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    FUNDING_PLANEJADO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VERBA_PLANEJADO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    MARGEM_BRUTA_PLANEJADO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    CMV_SUGERIDO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    CMV_PLANEJADO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    SENSIVEL_REBATE = models.CharField(max_length=1)


