# Generated by Django 3.0.4 on 2020-04-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing_parsing', '0011_diretrizesestrategica_indctgtop'),
    ]

    operations = [
        migrations.AddField(
            model_name='diretrizesestrategica',
            name='CODGRPFRN',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diretrizesestrategica',
            name='DATREFPOD',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='diretrizesestrategica',
            name='NOMDIASMN',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='diretrizesestrategica',
            name='NOMMES',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='diretrizesestrategica',
            name='NOMSMS',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='diretrizesestrategica',
            name='NOMSMSANO',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
