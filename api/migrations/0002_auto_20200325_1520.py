# Generated by Django 3.0.4 on 2020-03-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planocompras',
            name='CMV_REALIZADO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planocompras',
            name='COMPETITIVIDADE_REALIZADO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planocompras',
            name='FUNDING_REALIZADO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planocompras',
            name='MARGEM_BRUTA_REALIZADO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planocompras',
            name='META_VENDA_REALIZADO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planocompras',
            name='PRECO_BASE_REALIZADO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planocompras',
            name='PRECO_VENDA_BRUTA_REALIZADO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planocompras',
            name='PRECO_VENDA_LIQUIDO_REALIZADO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planocompras',
            name='REBATE_REALIZADO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planocompras',
            name='VERBA_REALIZADO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
