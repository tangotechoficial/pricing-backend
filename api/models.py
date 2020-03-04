from django.db import models


class DadosMestre(models.Model):
    numanomes = models.IntegerField()
    codprd = models.IntegerField()
    desprd = models.CharField()
    codfilepd = models.IntegerField()
    coddivfrn = models.IntegerField()
    vlrprecosaldomesanterior = models.DecimalField()
    vlrprecocredito = models.DecimalField()
    vlrprecodebito = models.DecimalField()
    vlrmargemsaldomesanterior = models.DecimalField()
    vlrmargemcredito = models.DecimalField()
    vlrmargemdebito = models.DecimalField()

