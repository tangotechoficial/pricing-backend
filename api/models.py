from django.db import models

class Fornecedor(models.Model):
    """

    Model for table FORNECEDOR

    """

    class Meta:
        db_table = "fornecedor"

    CODFRN = models.IntegerField(primary_key=True)
    NOMFRN = models.CharField(max_length=45)
    CODGRPFRN = models.IntegerField()
    NOMGRPFRN = models.CharField(max_length=45)

class Comprador(models.Model):
    """

    Model for table COMPRADOR

    """

    class Meta:
        db_table = "comprador"

    CODCPR = models.IntegerField(primary_key=True)
    NOMCPR = models.CharField(max_length=45)
    CODDIVCMP = models.IntegerField()
    DESDIVCMP = models.CharField(max_length=45)
    CODDRTCLLATU = models.IntegerField()
    DESDRTCLLATU = models.CharField(max_length=45)


class RelacionamentoFilialRegiao(models.Model):
    """
    Model for table RELACIONAMENTO_FILIAL_REGIAO
    """

    class Meta:
        db_table = 'relacionamento_filial_regiao'

    CODFILEPD = models.IntegerField(primary_key=True)
    NOMFILEPD = models.CharField(max_length=45)
    CODFILFAT = models.IntegerField()
    NOMFILFAT = models.CharField(max_length=45)
    TIPEDEREG = models.IntegerField()
    CODESTUNI = models.CharField(max_length=2)
    CODEDEREG = models.IntegerField()        


class Mercadoria(models.Model):
    """
    Model for table MERCADORIA
    """

    class Meta:
        db_table = "mercadoria"

    CODMER = models.IntegerField(primary_key=True)
    DESMER = models.CharField(max_length=45)
    CODFRNPCPMER = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    CODCPRATU = models.ForeignKey(Comprador, on_delete=models.DO_NOTHING)
    CODGRPMERSMR = models.IntegerField()
    DESGRPMERSMR = models.CharField(max_length=45)
    CLFCRVABCMER = models.CharField(max_length=1)

class TabAuxGrp(models.Model):
    """
    
    Model for table TAB_AUX_GRP
    """

    class Meta:
        db_table = "tab_aux_grp"

    Id_Aux = models.IntegerField(primary_key=True)
    CODMER = models.ForeignKey(Mercadoria, on_delete=models.DO_NOTHING)
    CODCLSMER = models.IntegerField()
    DESCLSMER = models.CharField(max_length=45)
    CODFMLMER = models.IntegerField()
    DESFMLMER = models.CharField(max_length=45)
    CODGRPMER = models.IntegerField()
    DESGRPMER = models.CharField(max_length=45)

class Representante(models.Model):
    """
    Model for table REPRESENTANTE
    """

    class Meta:
        db_table = 'representante'
    
    CODREPCMC = models.IntegerField(primary_key=True)
    NOMREPCMC = models.CharField(max_length=45)
    DATCADREPCMC = models.DateTimeField()

class Vendas(models.Model):
    """
    Model for table VENDAS
    """

    class Meta:
        db_table = 'vendas'

    CODPRD = models.ForeignKey(Mercadoria, on_delete=models.DO_NOTHING, db_column="CODMER")
    CODFILEPD = models.IntegerField()
    CODFILFAT = models.IntegerField()
    CODESTCLI = models.CharField(max_length=2)
    CODREPCMC = models.ForeignKey(Representante, on_delete=models.DO_NOTHING)
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


class VerbaeBC(models.Model):
    """
    Model for table VERBA_E_BC

    """

    class Meta:
        db_table = 'verba_e_bc'

    CODPRD = models.ForeignKey(Mercadoria, on_delete=models.DO_NOTHING)
    CODFILEPD = models.ForeignKey(RelacionamentoFilialRegiao, on_delete=models.DO_NOTHING)
    CODFILFAT = models.IntegerField()
    CODCLI = models.IntegerField()
    CODESTCLI = models.IntegerField()
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

class Elasticidade(models.Model):
    """
    Model for table ELASTICIDADE
    """

    class Meta:
        db_table = 'elasticidade'

    CODPRD = models.ForeignKey(Mercadoria, on_delete=models.DO_NOTHING)
    CODESTUNI = models.CharField(max_length=2)
    CODFILEPD = models.ForeignKey(RelacionamentoFilialRegiao, on_delete=models.DO_NOTHING)
    CODFILFAT = models.IntegerField()
    VLRVARVNDPCO = models.DecimalField(decimal_places=2, max_digits=10)
    DESMER = models.CharField(max_length=45)
    CLFCRVABCMER = models.CharField(max_length=1) 
    CODGRPMERSMR = models.IntegerField()
    DESGRPMERSMR = models.CharField(max_length=45)
    DESFMLMER = models.IntegerField()
    DESCLSMER = models.CharField(max_length=45)
    DESDIVCMP = models.CharField(max_length=45)
    # DESDRTCLLATU

class Estoque(models.Model):
    """
    Model for table ESTOQUE
    """

    class Meta:
        db_table = 'estoque'

    CODPRD = models.ForeignKey(Mercadoria, on_delete=models.DO_NOTHING)
    CODFILEPD = models.ForeignKey(RelacionamentoFilialRegiao, on_delete=models.DO_NOTHING)
    DATREF = models.DateTimeField()
    NUMSMNANO = models.DateTimeField()
    NOMDIASMN = models.DateTimeField()
    NOMMESANO = models.DateTimeField()
    NOMSMSANO = models.DateTimeField()
    VLRUNTCSTSCO = models.DecimalField(decimal_places=2, max_digits=10)
    QDEITEETQ = models.IntegerField()
    VLRVNDPDAFLTETQ = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCSTCMPIDL = models.DecimalField(decimal_places=2, max_digits=10)
    VLRMEDPCOCMP = models.DecimalField(decimal_places=2, max_digits=10)
    CODSTAPRDETQ = models.IntegerField()

class Competitividade(models.Model):
    """
    Model for table COMPETITIVIDADE
    """

    class Meta:
        db_table = 'competitividade'

    CODPRD = models.ForeignKey(Mercadoria, on_delete=models.DO_NOTHING)
    CODIDTCUR = models.IntegerField(primary_key=True)
    CODESTUNI = models.CharField(max_length=2)
    CODESTUNIORI = models.CharField(max_length=2)
    CODESTUNIDSN = models.CharField(max_length=2)
    NUMANO = models.DateTimeField()
    NUMANOMES = models.DateTimeField()
    NUMSMNANO = models.DateTimeField()
    NOMMES = models.DateTimeField()
    DATREF = models.DateTimeField()
    CODSML = models.IntegerField()
    DESGRPMERSMR = models.CharField(max_length=45)
    CODTIPAPU = models.CharField(max_length=45)
    VLRPCOMEDMCD = models.DecimalField(decimal_places=2, max_digits=10)
    VLRPCOBSEMER = models.DecimalField(decimal_places=2, max_digits=10)
    CLFCRVABCMER = models.CharField(max_length=1)
    CODDIVFRN = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)

class DadosMestre_Verba(models.Model):
    """
        Modelo de Tabela Dados Mestre
    """

    class Meta:
        db_table = "verba_disponivel"

    NUMANOMES = models.IntegerField(blank=True, null=True)
    CODPRD = models.IntegerField(blank=True, null=True)
    DESPRD = models.CharField(max_length=150, blank=True, null=True)
    CODFILEPD = models.IntegerField()
    CODDIVFRN = models.IntegerField(null=True)
    VLRPRECOSALDOMESANTERIOR = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPRECOCREDITO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPRECODEBITO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRMARGEMSALDOMESANTERIOR = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRMARGEMCREDITO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRMARGEMDEBITO = models.DecimalField(decimal_places=2, max_digits=10, null=True)

class DadosMestre_VerbaCSV(models.Model):
    import_date = models.DateTimeField(auto_now=True)
    csvfile = models.FileField()

class DadosMestre_ComposicaoPreco(models.Model):

    class Meta:
        db_table = "composicao_preco"

    codprd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    desprd = models.CharField(max_length=45, blank=True, null=True)
    abc = models.CharField(max_length=45, blank=True, null=True)
    sensivel_rebate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipedereg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    codedereg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    codfilemp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    codfilfat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mb = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mb_calculada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    verba_preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fund_preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rebate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    icms = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pis_cofins = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    devolucao = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    target = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    flex = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cmv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bonificado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    complemento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precobase = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    codestuni = models.TextField(blank=True, null=True)
    preco_livro = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    """
    codereg = verificar

    """

    
    


class DadosMestre_ComposicaoPrecoCSV(models.Model):
    import_date = models.DateTimeField(auto_now=True)
    csvfile = models.FileField()

class DiretrizesEstrategica(models.Model):

    class Meta:
        db_table = "diretriz_estrategica"

    datini = models.CharField(max_length=45, blank=True, null=True)
    coddrtcllatu = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    desdrtcllatu = models.CharField(max_length=150, blank=True, null=True)
    codcllcmpatu = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descllcmpatu = models.CharField(max_length=45, blank=True, null=True)
    nomfnccpratu = models.CharField(max_length=120, blank=True, null=True)
    codgrpprd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    desgrpprd = models.CharField(max_length=45, blank=True, null=True)
    codctgprd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    desctgprd = models.CharField(max_length=150, blank=True, null=True)
    codsubctgprd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dessubctgprd = models.CharField(max_length=45, blank=True, null=True)
    codgrpecofrn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nomgrpecofrn = models.CharField(max_length=45, blank=True, null=True)
    coddivfrn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    desdivfrn = models.CharField(max_length=150, blank=True, null=True)
    codestuni = models.CharField(max_length=45, blank=True, null=True)
    nomestuni = models.CharField(max_length=100, blank=True, null=True)
    vlrvndfatliq = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vlrrctliqapu = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vlrmrgcrb = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vlrmrgbrt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nomreggeo = models.CharField(max_length=45, blank=True, null=True)



class DiretrizesEstrategicaCSV(models.Model):
    import_date = models.DateTimeField(auto_now=True)
    csvfile = models.FileField()

class PlanoCompras(models.Model):

    class Meta:
        db_table = "planocompras"

    CODPRD = models.ForeignKey(Mercadoria, on_delete=models.DO_NOTHING)
    CODFILEPD = models.ForeignKey(RelacionamentoFilialRegiao, on_delete=models.DO_NOTHING)
    CODFILFAT = models.IntegerField()
    CODESTUNI = models.CharField(max_length=2)
    MONTH = models.CharField(max_length=10)
    YEAR = models.CharField(max_length=10)
    WEEK = models.CharField(max_length=10)
    VOLVNDSUG = models.DecimalField(decimal_places=2, max_digits=10)
    VOLVNDSUGALC = models.DecimalField(decimal_places=2, max_digits=10)
    MRGBRTPEROCD = models.DecimalField(decimal_places=2, max_digits=10)
    VLRPCOSUG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRPCOBASESUG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRIMPTOTSUG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRICMSSUG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRPISCOFSUG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRDEVSUG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRFLXSUG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRMRGBRTSUG = models.DecimalField(decimal_places=2, max_digits=10)
    VRBUNTSUGSUG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRVRBPLAN   = models.CharField(max_length=10)
    VLRCMVPCOSUG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCMVPCOATU = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCMVCMPATU = models.CharField(max_length=10)
    VOLVNDPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRPCOPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRPCOBASEPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRIMPTOTPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRICMSPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRPISCOFPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRDEVPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRFLXPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRMRGBRTPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VRBUNTSUGPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRVRBPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCMVPCOPLN = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCMVCMPPLN = models.DecimalField(decimal_places=2, max_digits=10)


class Otimizador(models.Model):
    """
        Model for table Otimizador
    """

    class Meta: 
        db_table= "otimizador"

    DATREF = models.DateTimeField()
    CODPRD = models.ForeignKey(Mercadoria, on_delete=models.DO_NOTHING)
    CODFILEPD = models.ForeignKey(RelacionamentoFilialRegiao, on_delete=models.DO_NOTHING)
    CODFILFAT = models.IntegerField()
    VLRVBA = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRVBADIS = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRVBAINP = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRVBACAL = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRVBADEM = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRCSTMERVND = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    CODESTUNI = models.CharField(max_length=2, null=True)
    VLRMRGBRTCAL = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRMRGBRTOCD = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRMRGBRTRLZ = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRRCTLIQAPUCAL = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRRCTLIQAPUOCD = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRRCTLIQAPURLZ = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRCMVCAL = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRMCDCAL = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRMCDOCD = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRPCOBSECAL = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRPCOBSEOCD = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRPCOBSEMER = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRVNDLIQOCD = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRVNDLIQCAL = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VLRVNDLIQRLZ = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
