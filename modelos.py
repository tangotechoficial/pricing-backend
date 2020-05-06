# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models





class Cadcndpcodin(models.Model):
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


class Caddtzett(models.Model):
    vlrvndfatliq = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    codidtcur = models.IntegerField(primary_key=True)
    codestuni = models.CharField(max_length=2)
    coddivfrn = models.IntegerField()
    datrefpod = models.DateField()
    codundngccli = models.IntegerField()
    codcllcmpatu = models.IntegerField()
    codsgmngccli = models.IntegerField()
    vlrrctliqapu = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrmrgbrt = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrmrgcrb = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    nommes = models.CharField(max_length=40, blank=True, null=True)
    nomsms = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caddtzett'
        unique_together = (('codidtcur', 'codestuni', 'coddivfrn', 'datrefpod', 'codundngccli', 'codcllcmpatu', 'codsgmngccli'),)


class Cadedefrmseqacs(models.Model):
    codcpofrmseqacs = models.CharField(primary_key=True, max_length=20)
    nomcpofrmseqacs = models.CharField(max_length=50)
    codfnc = models.IntegerField()
    datcad = models.DateField()
    datultatl = models.DateField()
    datdst = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadedefrmseqacs'


class Cadpcodin(models.Model):
    codchvpcodin = models.CharField(primary_key=True, max_length=20)
    datrefpcodin = models.DateField()
    codschcalpcodin = models.CharField(max_length=30)
    vlruntpco = models.DecimalField(max_digits=15, decimal_places=2)
    tipfrmcalpcodin = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'cadpcodin'


class Cadschcalpcodin(models.Model):
    codschcalpcodin = models.CharField(primary_key=True, max_length=30)
    tipschcalpcodin = models.CharField(max_length=4)
    codfnc = models.IntegerField()
    datcad = models.DateField()
    datultatl = models.DateField()
    datdst = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadschcalpcodin'


class Cadseqacspcodin(models.Model):
    codseqacspco = models.CharField(primary_key=True, max_length=20)
    nomseqacspco = models.CharField(max_length=150)
    codfnc = models.IntegerField()
    datcad = models.DateField()
    datultatl = models.DateField()
    datdst = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadseqacspcodin'


class Cadtipvlrcndpcodin(models.Model):
    codtipvlrpcodin = models.CharField(primary_key=True, max_length=20)
    nomtipvlrpcodin = models.CharField(max_length=60)
    codfnc = models.IntegerField()
    datcad = models.DateField()
    datultatl = models.DateField()
    datdst = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadtipvlrcndpcodin'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Movetqcal(models.Model):
    codfilepd = models.IntegerField(primary_key=True)
    codprd = models.IntegerField()
    datref = models.DateField()
    vlruntcstsco = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    qdeiteetq = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrvndpdafltetq = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    qdemedvndmnsmer = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    vlrcstcmpidl = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrmedpcocmp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    codstaprdetq = models.CharField(max_length=1, blank=True, null=True)
    numsmnano = models.IntegerField(blank=True, null=True)
    nomdiasmn = models.CharField(max_length=40, blank=True, null=True)
    nommesano = models.CharField(max_length=40, blank=True, null=True)
    nomsmsano = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movetqcal'
        unique_together = (('codfilepd', 'codprd', 'datref'),)


class Movpcobsecal(models.Model):
    codprd = models.IntegerField(primary_key=True)
    codfilepd = models.IntegerField()
    codfilfat = models.IntegerField()
    datref = models.DateField()
    codestuni = models.CharField(max_length=2)
    tipedereg = models.IntegerField()
    vlrmrgbrt = models.DecimalField(max_digits=15, decimal_places=4)
    vlrvba = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    vlrfnd = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrfndrbtite = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    vlricm = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrpis = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrdvl = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlruntpcoalv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrpcobsemer = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrcstliq = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrflxcns = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movpcobsecal'
        unique_together = (('codprd', 'codfilepd', 'codfilfat', 'datref', 'codestuni', 'tipedereg'),)


class Movvarvndpco(models.Model):
    codsmlpco = models.IntegerField(primary_key=True)
    codestuni = models.CharField(max_length=2)
    qdeite = models.IntegerField(blank=True, null=True)
    vlrpcomedvnd = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    vlrfnd = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrvba = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movvarvndpco'
        unique_together = (('codsmlpco', 'codestuni'),)


class Movvbadiscal(models.Model):
    codprd = models.IntegerField(primary_key=True)
    codsmlpco = models.IntegerField()
    codfilepd = models.IntegerField()
    datref = models.DateField()
    vlrsldpcomesant = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrcrdpco = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrdbtpco = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrsldmrgmesant = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrcrdmrg = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrdbtmrg = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movvbadiscal'
        unique_together = (('codprd', 'codsmlpco', 'codfilepd', 'datref'),)


class Movvbahst(models.Model):
    qdeiteped = models.IntegerField(blank=True, null=True)
    codprd = models.IntegerField(primary_key=True)
    codfilepd = models.IntegerField()
    codfilfat = models.IntegerField()
    codestcli = models.CharField(max_length=2)
    codcli = models.IntegerField()
    numanomesdia = models.IntegerField()
    vlrvndliq = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlruntvndliq = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlruntcstmer = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrcstmer = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlruntfndmer = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrfnd = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    qdeitepmc = models.DecimalField(max_digits=7, decimal_places=2)
    qdeitebfc = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    vlruntdscbfcite = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlruntfndpco = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlruntfndmrg = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrrlzpmc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrbfc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrfndpcovnd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrfndpcocst = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlruntfndpmcvnd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrmnsfndrcbfrn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vlrrbtcal = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movvbahst'
        unique_together = (('codprd', 'codfilepd', 'codfilfat', 'codestcli', 'codcli', 'numanomesdia'),)


class Movvlrpcomcd(models.Model):
    clfcrvabcmer = models.CharField(max_length=1, blank=True, null=True)
    datref = models.DateField(primary_key=True)
    codprd = models.IntegerField()
    codestuni = models.CharField(max_length=2)
    numanomes = models.IntegerField()
    numsmnmes = models.IntegerField()
    numsmnano = models.IntegerField()
    codidtcur = models.IntegerField()
    vlrpcobsemer = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    codestunidsn = models.CharField(max_length=2, blank=True, null=True)
    codtipapu = models.CharField(max_length=1)
    destipapu = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'movvlrpcomcd'
        unique_together = (('datref', 'codprd', 'codestuni', 'codidtcur'),)


class Movvndhstcal(models.Model):
    codprd = models.IntegerField(primary_key=True)
    codfilepd = models.IntegerField()
    codfilfat = models.IntegerField()
    codestcli = models.CharField(max_length=2)
    codcliend = models.IntegerField()
    codrepcmc = models.IntegerField()
    numped = models.IntegerField()
    numanomessmn = models.IntegerField()
    numanomesdia = models.IntegerField()
    vlrvndliq = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    qdeite = models.IntegerField(blank=True, null=True)
    vlrmrgcrb = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrmrgbrt = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrrctliqapu = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrimptot = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrcstarg = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrcstrepfnc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrcstvnd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrcsttrntnlcub = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vlrfnd = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrdscflxcns = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrsupflx = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    permrgadicnlvnd = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vlrcstdtb = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    vlrcstmedprd = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movvndhstcal'
        unique_together = (('codprd', 'codfilepd', 'codfilfat', 'codestcli', 'codcliend', 'codrepcmc', 'numped', 'numanomesdia'),)


class Rlccamcndpcodin(models.Model):
    codcampcodin = models.CharField(primary_key=True, max_length=20)
    codcndpcodin = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rlccamcndpcodin'
        unique_together = (('codcampcodin', 'codcndpcodin'),)


class Rlccndcamschpcodin(models.Model):
    codcndpcodin = models.CharField(primary_key=True, max_length=20)
    codcampcodin = models.CharField(max_length=20)
    codschcalpcodin = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'rlccndcamschpcodin'
        unique_together = (('codcndpcodin', 'codcampcodin', 'codschcalpcodin'),)


class Rlcschcalchvpcodin(models.Model):
    codschcalpcodin = models.CharField(primary_key=True, max_length=30)
    codchvpcodin = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rlcschcalchvpcodin'
        unique_together = (('codschcalpcodin', 'codchvpcodin'),)


class Rlcschcndcampcodin(models.Model):
    codschcalpcodin = models.CharField(primary_key=True, max_length=30)
    codcndpcodin = models.CharField(max_length=20)
    codcampcodin = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rlcschcndcampcodin'
        unique_together = (('codschcalpcodin', 'codcndpcodin', 'codcampcodin'),)


class Rlcseqacscndpco(models.Model):
    codseqacspco = models.CharField(primary_key=True, max_length=20)
    codcndpcodin = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rlcseqacscndpco'
        unique_together = (('codseqacspco', 'codcndpcodin'),)
