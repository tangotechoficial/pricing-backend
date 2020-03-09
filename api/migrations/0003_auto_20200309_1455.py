# Generated by Django 3.0.4 on 2020-03-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200309_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='BONIFICADO',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='CMV',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='COMPLEMENTO',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='DEVOLUCAO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='FUND_PRECO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='ICMS',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='MB',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='MB_CALCULADA',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='PIS_COFINS',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='PRECOBASE',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='PRECO_LIVRO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='REBATE',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='TARGET',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmestre_composicaopreco',
            name='VERBA_PRECO',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
