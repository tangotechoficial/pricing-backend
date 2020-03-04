from django.db import models


class DadosMestre(models.Model):
    numanomes = models.IntegerField()
    codprd = models.IntegerField()
    desprd = models.CharField(max_length=150)
    codfilepd = models.IntegerField()
    coddivfrn = models.IntegerField()
    vlrprecosaldomesanterior = models.DecimalField(decimal_places=2, max_digits=10)
    vlrprecocredito = models.DecimalField(decimal_places=2, max_digits=10)
    vlrprecodebito = models.DecimalField(decimal_places=2, max_digits=10)
    vlrmargemsaldomesanterior = models.DecimalField(decimal_places=2, max_digits=10)
    vlrmargemcredito = models.DecimalField(decimal_places=2, max_digits=10)
    vlrmargemdebito = models.DecimalField(decimal_places=2, max_digits=10)

class DadosMestreCSV(models.Model):
    import_date = models.DateTimeField(auto_now=True)
    csvfile = models.FileField()


