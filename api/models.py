from django.db import models


class DadosMestre(models.Model):
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

class DadosMestreCSV(models.Model):
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

