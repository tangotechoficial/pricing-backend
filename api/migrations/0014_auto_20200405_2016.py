# Generated by Django 3.0.4 on 2020-04-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200405_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diretrizesestrategica',
            name='CODFMLMER',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diretrizesestrategica',
            name='CODGRPMER',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
