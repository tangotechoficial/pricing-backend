from django.db import models


class DadosMestre_Verba(models.Model):
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

