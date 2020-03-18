# Generated by Django 3.0.4 on 2020-03-18 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('CODCPRATU', models.IntegerField(primary_key=True, serialize=False)),
                ('NOMCPRATU', models.CharField(max_length=45)),
                ('CODCLLCMPATU', models.IntegerField()),
                ('DESCLLCMPATU', models.CharField(max_length=45)),
                ('CODDRTCLLATU', models.IntegerField()),
                ('DESDRTCLLATU', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'COMPRADOR',
            },
        ),
        migrations.CreateModel(
            name='DadosMestre_ComposicaoPrecoCSV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_date', models.DateTimeField(auto_now=True)),
                ('csvfile', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='DadosMestre_VerbaCSV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_date', models.DateTimeField(auto_now=True)),
                ('csvfile', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='DiretrizesEstrategicaCSV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_date', models.DateTimeField(auto_now=True)),
                ('csvfile', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('CODDIVFRN', models.IntegerField(primary_key=True, serialize=False)),
                ('DESDIVFRN', models.CharField(max_length=45)),
                ('CODGRPECOFRN', models.IntegerField()),
                ('NOMGRPECOFRN', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'FORNECEDOR',
            },
        ),
        migrations.CreateModel(
            name='Mercadoria',
            fields=[
                ('CODPRD', models.IntegerField(primary_key=True, serialize=False)),
                ('DESPRD', models.CharField(max_length=45)),
                ('CODSML', models.IntegerField()),
                ('dessml', models.CharField(max_length=45)),
                ('ABC', models.CharField(max_length=1)),
                ('CODCPRATU', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Comprador')),
                ('CODDIVFRN', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Fornecedor')),
            ],
            options={
                'db_table': 'MERCADORIA',
            },
        ),
        migrations.CreateModel(
            name='RelacionamentoFilialRegiao',
            fields=[
                ('CODFILEPD', models.IntegerField(primary_key=True, serialize=False)),
                ('NOMFILEPD', models.CharField(max_length=45)),
                ('CODFILFAT', models.IntegerField()),
                ('NOMFILFAT', models.CharField(max_length=45)),
                ('CODESTUNI', models.CharField(max_length=2)),
                ('NOMESTUNI', models.CharField(max_length=45)),
                ('TIPEDEREG', models.IntegerField()),
                ('CODEDEREG', models.IntegerField()),
            ],
            options={
                'db_table': 'RELACIONAMENTO_FILIAL_REGIAO',
            },
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('CODREPCMC', models.IntegerField(primary_key=True, serialize=False)),
                ('NOMREPCMC', models.CharField(max_length=45)),
                ('DATCADREPCMC', models.DateTimeField()),
            ],
            options={
                'db_table': 'REPRESENTANTE',
            },
        ),
        migrations.CreateModel(
            name='TabAuxGrp',
            fields=[
                ('Id_Aux', models.IntegerField(primary_key=True, serialize=False)),
                ('CODSUBCTGPRD', models.IntegerField()),
                ('DESSUBCTGPRD', models.CharField(max_length=45)),
                ('CODCTGPRD', models.IntegerField()),
                ('DESCTGPRD', models.CharField(max_length=45)),
                ('CODGRPPRD', models.IntegerField()),
                ('DESGRPPRD', models.CharField(max_length=45)),
                ('Linha_de_negocio', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'TAB_AUX_GRP',
            },
        ),
        migrations.CreateModel(
            name='VerbaeBC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODFILFAT', models.IntegerField()),
                ('CODESTCLI', models.IntegerField()),
                ('NUMANOMESDIA', models.DateTimeField()),
                ('QUANTIDADE_ITENS_PEDIDO', models.IntegerField()),
                ('VALOR_TOTAL_VENDA_LIQUIDA', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_UNITARIO_CMV', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_TOTAL_CMV', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_UNITARIO_FUNDING', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_TOTAL_FUNDING', models.DecimalField(decimal_places=2, max_digits=10)),
                ('QUANTIDADE_ITENS_PROMOCAO', models.IntegerField()),
                ('QUANTIDADE_ITENS_BENEFICIO', models.IntegerField()),
                ('VALOR_UNITARIO_PROMOCAO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_UNITARIO_BENEFICIO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_UNITARIO_FUNDING_PRECO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_UNITARIO_FUNDING_MARGEM', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_TOTAL_PROMOCAO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_TOTAL_BENEFICIO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_TOTAL_FUNDING_PRECO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_TOTAL_FUNDING_MARGEM', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VALOR_TOTAL_DMS_SANSUNG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('REBATE', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CODFILEPD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.RelacionamentoFilialRegiao')),
                ('CODPRD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mercadoria')),
            ],
            options={
                'db_table': 'VERBA_E_BC',
            },
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODFILFAT', models.IntegerField()),
                ('CODESTCLI', models.IntegerField()),
                ('NUMPED', models.IntegerField()),
                ('NUMANOMESSMN', models.DateTimeField()),
                ('NUMANOMESDIA', models.DateTimeField()),
                ('CMV', models.DecimalField(decimal_places=2, max_digits=10)),
                ('QDEITE', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRVNDLIQ', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MARGEM_CONTRIBUICAO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MARGEM_BRUTA', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRRCTLIQ', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRIMPTOT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TRANSFERENCIA', models.DecimalField(decimal_places=2, max_digits=10)),
                ('DISTRIBUICAO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ARMAZENAGEM', models.DecimalField(decimal_places=2, max_digits=10)),
                ('FUNDING', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRSUPFLX', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRDSCFLXCNS', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Despesas_Financeiras', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Margem_por_Segmento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CODFILEPD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.RelacionamentoFilialRegiao')),
                ('CODPRD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mercadoria')),
                ('CODREPCMC', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Representante')),
            ],
            options={
                'db_table': 'VENDAS',
            },
        ),
        migrations.CreateModel(
            name='PlanoCompras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODFILFAT', models.IntegerField()),
                ('DATA_PRECO', models.DateTimeField()),
                ('CODESTUNI', models.IntegerField()),
                ('META_VENDA_SUGERIDO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('META_VENDA_PLANEJADO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('PRECO_VENDA_LIQUIDO_SUGERIDO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('PRECO_VENDA_LIQUIDO_PLANEJADO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('COMPETITIVIDADE_SUGERIDO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('COMPETITIVIDADE_PLANEJADO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('PRECO_VENDA_BRUTA_SUGERIDO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('PRECO_VENDA_BRUTA_PLANEJADO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('PRECO_BASE_SUGERIDO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('PRECO_BASE_PLANEJADO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('REBATE_PLANEJADO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('FUNDING_PLANEJADO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('VERBA_PLANEJADO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('MARGEM_BRUTA_PLANEJADO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('CMV_SUGERIDO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('CMV_PLANEJADO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('SENSIVEL_REBATE', models.CharField(max_length=1)),
                ('SEMANA', models.IntegerField()),
                ('CODFILEMP', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.RelacionamentoFilialRegiao')),
                ('CODPRD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mercadoria')),
            ],
            options={
                'db_table': 'PLANOCOMPRAS',
            },
        ),
        migrations.CreateModel(
            name='Otimizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATA_PRECO', models.DateTimeField()),
                ('CODFILFAT', models.IntegerField()),
                ('CODESTUNI', models.IntegerField()),
                ('VERBA_OTIMIZADA', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VERBA_INPUT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VERBA_NECESSARIA', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VERBA_DISPONIVEL', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CODFILEMP', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.RelacionamentoFilialRegiao')),
                ('CODPRD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mercadoria')),
            ],
            options={
                'db_table': 'OTIMIZADOR',
            },
        ),
        migrations.AddField(
            model_name='mercadoria',
            name='CODFIL',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.RelacionamentoFilialRegiao'),
        ),
        migrations.AddField(
            model_name='mercadoria',
            name='Id_Aux',
            field=models.ManyToManyField(to='api.TabAuxGrp'),
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATINI', models.DateTimeField()),
                ('NUMSMNANO', models.DateTimeField()),
                ('NOMSMSANO', models.DateTimeField()),
                ('NOMDIASMN', models.DateTimeField()),
                ('NUMDIASMN', models.DateTimeField()),
                ('NOMABVMESANO', models.CharField(max_length=45)),
                ('VLRUNTCSTSCO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('QDEITEETQ', models.IntegerField()),
                ('VLRVNDPDAFLTETQ', models.DecimalField(decimal_places=2, max_digits=10)),
                ('QDEMEDVNDMNSMER', models.IntegerField()),
                ('VLRCSTCMPIDL', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRMEDPCOCMP', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CODSTAPRDETQ', models.IntegerField()),
                ('DESSTAPRDETQ', models.CharField(max_length=45)),
                ('CODUNDREG', models.IntegerField()),
                ('DESUNDREG', models.CharField(max_length=45)),
                ('FLGUNDREG', models.CharField(max_length=45)),
                ('CODFIL', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.RelacionamentoFilialRegiao')),
                ('CODPRD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mercadoria')),
            ],
            options={
                'db_table': 'ESTOQUE',
            },
        ),
        migrations.CreateModel(
            name='Elasticidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf', models.CharField(max_length=2)),
                ('Elasticidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qt', models.IntegerField()),
                ('pcmed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unitfnd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('verba', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codsml', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mercadoria')),
            ],
            options={
                'db_table': 'ELASTICIDADE',
            },
        ),
        migrations.CreateModel(
            name='DiretrizesEstrategica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATINI', models.DateTimeField()),
                ('CODDRTCLLATU', models.IntegerField()),
                ('DESDRTCLLATU', models.CharField(max_length=150)),
                ('CODCLLCMPATU', models.IntegerField()),
                ('DESCLLCMPATU', models.CharField(max_length=150)),
                ('NOMFNCCPRATU', models.CharField(max_length=150)),
                ('CODGRPPRD', models.IntegerField()),
                ('DESGRPPRD', models.CharField(max_length=150)),
                ('CODCTGPRD', models.IntegerField()),
                ('DESCTGPRD', models.CharField(max_length=150)),
                ('CODSUBCTGPRD', models.IntegerField()),
                ('DESSUBCTGPRD', models.CharField(max_length=150)),
                ('CODGRPECOFRN', models.IntegerField()),
                ('NOMGRPECOFRN', models.CharField(max_length=150)),
                ('CODDIVFRN', models.IntegerField()),
                ('DESDIVFRN', models.CharField(max_length=150)),
                ('CODESTUNI', models.CharField(max_length=3)),
                ('NOMESTUNI', models.CharField(max_length=100)),
                ('VLRVNDFATLIQ', models.CharField(max_length=100)),
                ('VLRMRGBRT', models.CharField(max_length=100)),
                ('NOMREGGEO', models.CharField(max_length=100)),
                ('Id_Aux', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.TabAuxGrp')),
            ],
            options={
                'db_table': 'DIRETRIZ_ESTRATEGICA',
            },
        ),
        migrations.CreateModel(
            name='DadosMestre_Verba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NUMANOMES', models.IntegerField()),
                ('DESPRD', models.CharField(max_length=150)),
                ('CODDIVFRN', models.IntegerField()),
                ('VLRPRECOSALDOMESANTERIOR', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRPRECOCREDITO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRPRECODEBITO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRMARGEMSALDOMESANTERIOR', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRMARGEMCREDITO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VLRMARGEMDEBITO', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CODFILEPD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.RelacionamentoFilialRegiao')),
                ('CODPRD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mercadoria')),
            ],
            options={
                'db_table': 'VERBA_DISPONIVEL',
            },
        ),
        migrations.CreateModel(
            name='DadosMestre_ComposicaoPreco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DESPRD', models.CharField(max_length=150)),
                ('ABC', models.CharField(max_length=1)),
                ('SENSIVEL_REBATE', models.SmallIntegerField()),
                ('TIPEDEREG', models.IntegerField()),
                ('CODEDEREG', models.IntegerField()),
                ('CODFILFAT', models.IntegerField()),
                ('MB', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('MB_CALCULADA', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('VERBA_PRECO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('FUND_PRECO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('REBATE', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('ICMS', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('PIS_COFINS', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('DEVOLUCAO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('TARGET', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('FLEX', models.IntegerField()),
                ('CMV', models.DecimalField(decimal_places=3, max_digits=15, null=True)),
                ('BONIFICADO', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('COMPLEMENTO', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('PRECOBASE', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('DATA_PRECO', models.DateTimeField()),
                ('CODESTUNI', models.CharField(max_length=2)),
                ('PRECO_LIVRO', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('CODFILEMP', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.RelacionamentoFilialRegiao')),
                ('CODPRD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mercadoria')),
            ],
            options={
                'db_table': 'COMPOSICAO_PRECO',
            },
        ),
        migrations.CreateModel(
            name='Competitividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=2)),
                ('NUMANOMES', models.DateTimeField()),
                ('NUMSMNANO', models.DateTimeField()),
                ('data_emissao', models.DateTimeField()),
                ('TipoPesquisa', models.CharField(max_length=45)),
                ('pc_mrt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pc_psq', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Comp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pc_psq_pond', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pc_mrt_pond', models.DecimalField(decimal_places=2, max_digits=10)),
                ('regiao', models.CharField(max_length=45)),
                ('Uf_Destino', models.CharField(max_length=2)),
                ('ABC', models.CharField(max_length=1)),
                ('CODPRD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mercadoria')),
            ],
            options={
                'db_table': 'COMPETITIVIDADE',
            },
        ),
    ]
