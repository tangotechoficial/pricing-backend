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
    DESGRPMER = models.CharField(max_length=45)
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
    CODFILEPD = models.ForeignKey(RelacionamentoFilialRegiao, on_delete=models.DO_NOTHING)
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
    DESFMLMER = models.CharField(max_length=45)
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

    CODPRD = models.ForeignKey(Mercadoria, on_delete=models.DO_NOTHING)
    CODSMLPCO = models.IntegerField()
    CODFILEPD = models.ForeignKey(RelacionamentoFilialRegiao, on_delete=models.DO_NOTHING)
    DATREF = models.DateTimeField()
    VLRSLDPCOMESANT = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCRDPCO = models.DecimalField(decimal_places=2, max_digits=10)
    VLRDBTPCO = models.DecimalField(decimal_places=2, max_digits=10)
    VLRSLDMRGMESANT = models.DecimalField(decimal_places=2, max_digits=10)
    VLRCRDMRG = models.DecimalField(decimal_places=2, max_digits=10)
    VLRDBTMRG = models.DecimalField(decimal_places=2, max_digits=10)

class DadosMestre_VerbaCSV(models.Model):
    import_date = models.DateTimeField(auto_now=True)
    csvfile = models.FileField()

class DadosMestre_ComposicaoPreco(models.Model):

    class Meta:
        db_table = "composicao_preco"

    CODPRD = models.ForeignKey(Mercadoria, on_delete=models.DO_NOTHING)
    CODFILEPD = models.ForeignKey(RelacionamentoFilialRegiao, on_delete=models.DO_NOTHING)
    CODFILFAT = models.IntegerField()
    DATREF = models.DateTimeField()
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
    VLRCSTCAL = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRBNF = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRCPLCSTPCO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRPCOBSEMER = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    CODREGPCO = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    NUMRLCCIDGIR = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    TIPCALUTZPCOLIQ = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    
    """
    codereg = verificar

    """

    
    


class DadosMestre_ComposicaoPrecoCSV(models.Model):
    import_date = models.DateTimeField(auto_now=True)
    csvfile = models.FileField()

class DiretrizesEstrategica(models.Model):

    class Meta:
        db_table = "diretriz_estrategica"

    CODESTUNI = models.ForeignKey(RelacionamentoFilialRegiao, on_delete=models.DO_NOTHING)
    CODDIVFRN = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    DATREFPOD = models.DateTimeField()
    NOMMES = models.DateTimeField() 
    NOMSMS = models.DateTimeField() 
    NOMDIASMN = models.DateTimeField() 
    NOMSMSANO = models.DateTimeField() 
    CODUNDNGCCLI = models.IntegerField()
    CODCLLCMPATU = models.IntegerField()
    DESDRTCLLATU = models.CharField(max_length=150)
    CODSGMNGCCLI = models.IntegerField()
    VLRVNDFATLIQ = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRRCTLIQAPU = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRMRGCRB = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    VLRMRGBRT = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    NOMCPR = models.CharField(max_length=45)
    CODFIL = models.IntegerField()
    CODCLSMER = models.IntegerField()
    DESCLSMER = models.CharField(max_length=45)
    CODFMLMER = models.IntegerField()
    DESGRPMER = models.CharField(max_length=45)
    CODGRPMER = models.IntegerField()
    DESGRPMER = models.CharField(max_length=45)



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
    MRGBRTPEROCD = models.DecimalField(decimal_places=2, max_digits=10)
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
    VLRVBA = models.DecimalField(decimal_places=2, max_digits=10)
    VLRVBADIS = models.DecimalField(decimal_places=2, max_digits=10)
    VLRVBAINP = models.DecimalField(decimal_places=2, max_digits=10)
    VLRVBACAL = models.DecimalField(decimal_places=2, max_digits=10)
    VLRVBADEM = models.DecimalField(decimal_places=2, max_digits=10)
