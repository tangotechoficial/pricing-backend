# Generated by Django 3.0.4 on 2020-04-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing_parsing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosMestre_Verba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODPRD', models.IntegerField()),
                ('CODSMLPCO', models.IntegerField(blank=True, null=True)),
                ('CODFILEPD', models.IntegerField()),
                ('DATREF', models.DateTimeField(blank=True, null=True)),
                ('VLRSLDPCOMESANT', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('VLRCRDPCO', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('VLRDBTPCO', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('VLRSLDMRGMESANT', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('VLRCRDMRG', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('VLRDBTMRG', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'mrt.MOVVBADISCAL',
            },
        ),
        migrations.CreateModel(
            name='Elasticidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODPRD', models.IntegerField()),
                ('CODESTUNI', models.CharField(max_length=2)),
                ('CODFILEPD', models.IntegerField(default=1)),
                ('CODFILFAT', models.IntegerField()),
                ('VLRVARVNDPCO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('DESMER', models.CharField(max_length=45)),
                ('CLFCRVABCMER', models.CharField(max_length=1)),
                ('CODGRPMERSMR', models.IntegerField()),
                ('DESGRPMERSMR', models.CharField(max_length=45)),
                ('DESFMLMER', models.IntegerField()),
                ('DESCLSMER', models.CharField(max_length=45)),
                ('DESDIVCMP', models.CharField(max_length=45)),
                ('DESDRTCLLATU', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'mrt.MOVVARVNDPCO',
            },
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODPRD', models.IntegerField()),
                ('CODFILEPD', models.IntegerField()),
                ('CODFILFAT', models.IntegerField()),
                ('CODESTCLI', models.CharField(max_length=2)),
                ('CODREPCMC', models.IntegerField()),
                ('NUMPED', models.IntegerField()),
                ('NUMANOMESSMN', models.DateTimeField()),
                ('NUMANOMESDIA', models.DateTimeField()),
                ('VLRVNDLIQ', models.DecimalField(decimal_places=2, max_digits=10)),
                ('QDEITE', models.IntegerField()),
                ('VLRDSCFLXCNS', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRSUPFLX', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRIMPTOT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRRCTLIQAPU', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRCSTMEDPRD', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PERMRGADICNLVND', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRFND', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRMRGBRT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRCSTTRNTNLCUB', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRCSTDTB', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRCSTARG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRMRGCRB', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'mrt.MOVVNDHSTCAL',
            },
        ),
        migrations.CreateModel(
            name='VerbaeBC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODPRD', models.IntegerField()),
                ('CODFILEPD', models.IntegerField()),
                ('CODFILFAT', models.IntegerField()),
                ('CODCLI', models.IntegerField()),
                ('CODESTCLI', models.IntegerField()),
                ('NUMPED', models.IntegerField()),
                ('NUMANOMESDIA', models.DateTimeField()),
                ('QDEITEPED', models.IntegerField()),
                ('VLRVNDLIQ', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRUNTCSTMER', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRCSTMER', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRUNTFNDMER', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRFND', models.DecimalField(decimal_places=2, max_digits=10)),
                ('QDEITEPMC', models.IntegerField()),
                ('QDEITEBFC', models.IntegerField()),
                ('VLRUNTFNDPMCVND', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRUNTDSCBFCITE', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRUNTFNDPCO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRUNTFNDMRG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRRLZPMC', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRBFC', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRFNDPCOVND', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRFNDPCOCST', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRMNSFNDRCBFRN', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRRBTCAL', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'mrt.MOVVBAHST',
            },
        ),
        migrations.AlterModelOptions(
            name='competitividade',
            options={},
        ),
    ]
