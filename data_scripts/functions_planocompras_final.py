import pandas as pd
import time
import numpy as np
import sqlite3
import sqlalchemy


conn_string = 'postgres://postgres:Martins*2020@pricing-data-parsing.cq8kmgnsewpt.us-east-1.rds.amazonaws.com/pricing_analitica2'
db = sqlalchemy.create_engine(conn_string)


def get_last_twelve_months(month, year):
    
    '''
    Função que retorna uma lista de strings com os últimos 12 meses no
    formato 'AAAAMM'.
    
    INPUT:
        month: lista com mês/meses
        year: lista com ano/anos
    OUTPUT:
        lista com os últimos 12 meses como string.

    AUTOR: Maurício Reis do Nascimento
    DATA: 03/03/2020
    '''
    import datetime
    month = min([int(x) for x in month])
    curr_year = year[0]
    years = [str(curr_year)]*(month-1) + \
        [str(int(curr_year)-1)]*(12-month+1)

    months = ['0' + str(i) if i < 10 else str(i) for i in range(1, month)]\
        + ['0'+str(12-i) if i > 2 else str(12-i) for i in range(12-month+1)]

    interval = [years[i]+months[i] for i in range(len(years))]

    return interval


def get_complementary_infos(prd):
    '''
    Função provisória que acessa a base de mercadoria e, a partir do
    código do produto, devolve as informações de grupo do produto,
    categoria, subcategoria, fornecedor.

    INPUT: 
        prd: lista com o código do produto
    OUTPUT: 
        Códigos das informações como dicionário.

    AUTOR: Maurício Reis do Nascimento
    DATA: 03/03/2020
    '''
    query = '''
            SELECT "CODGRPPRD", "CODCTGPRD", "CODSUBCTGPRD", "CODDIVFRN"
            FROM "ETTPRD"
            WHERE "CODPRD" IN ({prd})
            '''.format(prd=','.join(prd))
            
    return pd.read_sql_query(
                             query, db
                             ).drop_duplicates().to_dict(orient='list')


def get_weekly_goals_subctg(df, month, year, divfrn, filepd,
                            est, grpprd, ctg, subctg):

    '''
    Busca as metas semanais dada uma subcategoria, estado, filial de expedição,
    filial de faturamento, fornecedor.

    INPUT:
        df: pandas DataFrame com informações do filtro
            month: lista de strings com número do mês (dois algarismos)
            divfrn: lista com código da divisão do fornecedor
            year: lista de strings com número do ano
            filepd: lista com o código da filial de expedição
            filfat: lista com o código da filial de faturamento
            est: lista de strings com a sigla do estado,
            grpprd: lista com o código do grupo de produto
            ctg: lista com o código da categoria
            subctg: lista com o código da subcategoria
    OUTPUT:
        df: pandas DataFrame de input com a coluna de metas semanais para a
            subcategoria adicionada.

    AUTOR: Maurício Reis do Nascimento
    DATA: 03/03/2020
    '''
    
    # Buscando as metas por subcategoria estado, fonrnecedor e filial
    query = '''
        SELECT    "NUMSMNANO" AS "WEEK", 
                  "QDEDIASMN",
                  EXTRACT(MONTH FROM TO_TIMESTAMP("DATINI", 'YYYY/MM/DD')) AS "MONTH",
                  EXTRACT(YEAR FROM TO_TIMESTAMP("DATINI", 'YYYY/MM/DD')) AS "YEAR",
                  "CODGRPPRD", "CODCTGPRD", "CODSUBCTGPRD", "CODFIL" AS "CODFILEPD",
                  "CODDIVFRN", "CODESTUNI", SUM("VLRVNDFATLIQ") AS "VOLVNDLIQSUBOCD",
                  SUM("VLRMRGBRT") AS "MRGBRTOCD", SUM("VLRRCTLIQAPU") AS "VLRRCTLIQOCD",
                  SUM("VLRMRGBRT")/SUM("VLRRCTLIQAPU")*100 AS "MRGBRTPEROCD"
               
        FROM  "METASDIARIAS"
        
        WHERE EXTRACT(MONTH FROM TO_TIMESTAMP("DATINI", 'YYYY/MM/DD')) IN ({month}) AND
              EXTRACT(YEAR FROM TO_TIMESTAMP("DATINI", 'YYYY/MM/DD'))  IN ({year}) AND
              "CODDIVFRN" IN ({divfrn}) AND "CODGRPPRD" IN ({grpprd}) AND
              "CODCTGPRD" IN ({ctg}) AND "CODSUBCTGPRD" IN ({subctg}) AND
              "CODESTUNI" IN ('{est}') AND
              "CODCNOOCD"='OCD'AND "CODFIL" IN ({filepd}) AND
              "DESTIPOPEVND" = 'VENDA'
              
        GROUP BY "CODGRPPRD", "CODCTGPRD", "CODSUBCTGPRD", "CODFIL", "CODDIVFRN",
                 "CODESTUNI", "WEEK", "QDEDIASMN", "YEAR", "MONTH"
        ORDER BY "CODESTUNI", "WEEK"


        '''.format(month="','".join(month),
                   year="','".join(year),
                   divfrn=','.join(divfrn),
                   grpprd=','.join(grpprd),
                   ctg=','.join(ctg),
                   subctg=','.join(subctg),
                   est="','".join(est),
                   filepd=','.join(filepd))
        
    query_result = pd.read_sql_query(query, db)

    for i in query_result.columns:
        try:
            df[i] = df[i].astype(query_result[i].dtypes)
        except:
            pass
    df['CODPRD'] = df['CODPRD'].astype('int')
    df['CODFILFAT'] = df['CODFILFAT'].astype('int')
    
    df =  pd.merge(df,
                    query_result[['WEEK', 'QDEDIASMN', 'CODFILEPD', 'CODESTUNI',
                                  'CODSUBCTGPRD', 'CODCTGPRD',
                                  'CODGRPPRD', 'CODDIVFRN',
                                  'VOLVNDLIQSUBOCD', 'MRGBRTOCD','VLRRCTLIQOCD',
                                  'MRGBRTPEROCD']],
                    on=['CODFILEPD', 'CODESTUNI', 'CODSUBCTGPRD',
                        'CODCTGPRD', 'CODGRPPRD', 'CODDIVFRN'])
    df['WEEK'] = '0' + (df['WEEK'].astype(int) - df['WEEK'].astype(int).min()).astype(str)
    
    return df


def add_prd_hst_rpr(
                    df, grpprd, ctg, subctg, prd, est, 
                    month, year, filepd, filfat, divfrn
                    ):
    '''
    Busca a representatividade histórica do produto nas vendas da subcategoria,
    dado uma filial de expedição, filial de faturamento, estado, fornecedor.
    INPUT:
        df: pandas DataFrame com informações do filtro
        grpprd: lista com o código do grupo de produto
        ctg: lista com o código da categoria
        subctg: lista com o código da subcategoria
        prd: lista com o código de produto,
        est: lista de strings com a sigla do estado,
        month: lista de strings com número do mês (dois algarismos)
        year: lista de strings com número do ano
        filepd: lista com o código da filial de expedição
        filfat: lista com o código da filial de faturamento
        divfrn: lista com código da divisão do fornecedor
    OUTPUT:
        df: pandas DataFrame de input com a coluna de representatividade
            histórica adicionada

    AUTOR: Maurício Reis do Nascimento
    DATA: 03/03/2020
    '''

    month_interval = get_last_twelve_months(month, year)

    # Buscando vendas na subcategoria
    query_vendas_subctg = '''
        SELECT  t1."CODFILEPD", t1."CODFILFAT", t1."CODESTCLI" AS "CODESTUNI",
        "CODGRPPRD", "CODCTGPRD", t2."CODDIVFRN",
        "CODSUBCTGPRD", SUM(t1."VLRVNDLIQ") AS "VLRHSTVNDLIQSUB"
        
        
        FROM "MOVVNDHSTFIM" AS t1
        
        LEFT JOIN (
                   SELECT DISTINCT "CODPRD", "CODDIVFRN"
                   FROM "ETTPRD"
                   ) AS t2
                   
        ON t1."CODMER" = t2."CODPRD"
        
        WHERE "CODSUBCTGPRD" IN ({subctg}) AND "CODCTGPRD" IN ({ctg})
              AND "CODGRPPRD" IN ({grpprd}) AND "NUMANOMES" IN
              ('{month_interval}') AND "CODESTCLI" IN ('{est}') AND
              "CODFILEPD" IN ({filepd}) AND "CODFILFAT" IN ({filfat})
              AND "CODDIVFRN" IN ({divfrn})
        
        GROUP BY t1."CODFILEPD", t1."CODFILFAT","CODESTUNI",
        "CODGRPPRD", "CODCTGPRD", t2."CODDIVFRN", "CODSUBCTGPRD"
        
        
        '''.format(subctg=','.join(subctg),
           ctg=','.join(ctg),
           grpprd=','.join(grpprd),
           month_interval="','".join(month_interval),
           est="','".join(est),
           filepd=','.join(filepd),
           filfat=','.join(filfat),
           divfrn=','.join(divfrn))

    vendas_subctg = pd.read_sql_query(query_vendas_subctg, db)

    df = pd.merge(df, vendas_subctg, how='left',
                  on=['CODGRPPRD', 'CODCTGPRD', 'CODSUBCTGPRD', 'CODFILEPD',
                      'CODFILFAT', 'CODDIVFRN', 'CODESTUNI'])

    # Buscando histórico de vendas do produto
    query_prd = '''
        SELECT   "CODFILEPD", "CODFILFAT", "CODESTCLI" AS "CODESTUNI",
                  "CODMER" AS "CODPRD", SUM("VLRVNDLIQ") as "VLRHSTVNDLIQPRD",
                  SUM("VLRRCTLIQ") AS "VLRHSTRCTLIQPRD" 
        FROM     "MOVVNDHSTFIM"
        WHERE    "CODMER" IN ({prod}) AND 
                 "NUMANOMES" IN ('{month_interval}') AND
                 "CODESTCLI" IN ('{est}') AND 
                 "CODFILEPD" IN ({filepd}) AND
                 "CODFILFAT" IN ({filfat})
        GROUP BY "CODFILEPD", "CODFILFAT", "CODESTUNI", "CODPRD"
        '''.format(prod=','.join(prd),
                   month_interval="','".join(month_interval),
                   est="','".join(est),
                   filepd=','.join(filepd),
                   filfat=','.join(filfat))

    vendas_prd = pd.read_sql_query(query_prd, db)

    df = pd.merge(df, vendas_prd, how='left', on=[
                    'CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'CODPRD'])

    # Calculando a representatividade histórica do produto
    df['RPRHST'] = df['VLRHSTVNDLIQPRD']/df['VLRHSTVNDLIQSUB']
    df['RPRRCTLIQ'] = df['VLRHSTRCTLIQPRD']/df['VLRHSTVNDLIQPRD']

    return df


def calculate_suggested_volume_of_sales(df):
    '''
    Função para cálculo do volume de vendas sugerido para o produto a partir
    do volume de vendas sugerido para subcategoria e representatividade
    histórica.

    INPUT:
        df: pandas DataFrame retornado pela função add_prd_hst_rpr
    OUTPUT:
        df: pandas DataFrame de input com coluna adicional de volume de vendas
            sugerido para o produto.
            
    AUTOR: Maurício Reis do Nascimento
    DATA: 03/03/2020
    '''
    df['VOLVNDSUG'] = df['RPRHST']*df['VOLVNDLIQSUBOCD']
    df['MRGBRTSUG'] = df['RPRHST']*df['MRGBRTOCD']
    df['VLRRCTLIQSUG'] = df['RPRHST']*df['VLRRCTLIQOCD']

    return df


def get_hst_rpr_desc(df, prd, filepd, filfat, month, year, est):
    '''
    Calcula a representatividade histórica dos descontos do preço de venda
    com relação ao preço base (benefício e flexível)

    INPUT:
        df: pandas DataFrame que vai receber as informações obtidas
        grpprd: lista com o código do grupo de produto
        ctg: lista com o código da categoria
        subctg: lista com o código da subcategoria
        prd: lista com o código de produto,
        est: lista de strings com a sigla do estado,
        month: lista de strings com número do mês (dois algarismos)
        year: lista de strings com número do ano
        filepd: lista com o código da filial de expedição
        filfat: lista com o código da filial de faturamento
        divfrn: lista com código da divisão do fornecedor
    OUTPUT:
        df: pandas DataFrame de input com as colunas de representatividade
            histórica do benefício e do flexível adicionadas

    AUTOR: Maurício Reis do Nascimento
    DATA: 03/03/2020
    '''
    month_interval = get_last_twelve_months(month, year)

    # Buscando representatividade histórica do benefício
    query_bnf = '''

        SELECT   t1."CODFILEPD", t1."CODFILFAT", t1."CODPRD", 
                 (SUM(t1."VALOR_TOTAL_BENEFICIO")/
                  SUM(t1."VALOR_TOTAL_VENDA_LIQUIDA")) AS "RPRHSTBNF"
                 
        FROM     "MOVVBS" as t1

        WHERE    substring(t1."NUMANOMESDIA" :: varchar(255), 1, 6) IN ('{month_interval}') AND
                 t1."CODFILEPD" IN ({filepd}) AND 
                 t1."CODFILFAT" IN ({filfat}) AND
                 t1."CODPRD" in ({prd})
               
        GROUP BY t1."CODFILEPD", t1."CODFILFAT", t1."CODPRD"
            
        '''.format(month_interval="','".join(month_interval),
                   filepd=','.join(filepd),
                   filfat=','.join(filfat),
                   prd=','.join(prd))

    rpr_bnf = pd.read_sql_query(query_bnf, db)

    df = pd.merge(df, rpr_bnf, how='left', on=[
                  'CODFILEPD', 'CODFILFAT', 'CODPRD'])

    # Buscando representatividade histórica do flexível
    query_flx = '''
            SELECT   "CODFILEPD", "CODFILFAT", "CODESTCLI" AS "CODESTUNI",
                     "CODMER" AS "CODPRD", 
                     SUM("VLRDSCFLXCNS")/SUM("VLRVNDLIQ") AS "RPRHSTFLX"
                     
            FROM     "MOVVNDHSTFIM"
            
            WHERE    "NUMANOMES" IN ('{month_interval}') AND
                     "CODFILEPD" IN ({filepd}) AND
                     "CODFILFAT" IN ({filfat}) AND
                     "CODESTCLI" IN ('{est}') AND
                     "CODMER" IN ({prd})
                     
            GROUP BY "CODFILEPD", "CODFILFAT", "CODESTUNI", "CODPRD"
            '''.format(month_interval="','".join(month_interval),
                       filepd=','.join(filepd),
                       filfat=','.join(filfat),
                       est="','".join(est),
                       prd=','.join(prd))

    rpr_flx = pd.read_sql_query(query_flx, db)

    df = pd.merge(df, rpr_flx, how='left', on=[
                  'CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'CODPRD'])

    return df


def get_hst_rpr_acr(df, prd, filepd, filfat, month, year, est):
    '''
    Calcula a representatividade histórica dos acréscimos do preço de venda
    com relação ao preço base (margem por canal, superflex, despesas
    financeiras).

    INPUT:
        df: pandas DataFrame que vai receber as informações obtidas
        prd: lista com o código de produto,
        filepd: lista com o código da filial de expedição,
        filfat: lista com o código da filial de faturamento,
        month: lista de strings com número do mês (dois algarismos),
        year: lista de strings com número do ano,
        est: lista de strings com a sigla do estado.
    OUTPUT:
        df: pandas DataFrame de input com as colunas de representatividade
            histórica do superflex, margem por canal e despesas financeiras.

    AUTOR: Maurício Reis do Nascimento
    DATA: 03/03/2020
    '''

    month_interval = get_last_twelve_months(month, year)

    # Buscando representatividade histórica da margem por canal
    query_mpc = '''
                SELECT   "CODFILEPD", 
                         "CODFILFAT",  
                         "CODESTCLI" AS "CODESTUNI", 
                         "CODMER" AS "CODPRD",
                         SUM("VLRVNDLIQ"*"PERMRGADICNLVND"/100)/SUM("VLRVNDLIQ")
                         AS "RPRHSTMRGCNL"
                        
                FROM     "MOVVNDHSTFIM"
                
                WHERE    "NUMANOMES" IN ('{month_interval}') AND
                         "CODFILEPD" IN ({filepd}) AND
                         "CODFILFAT" IN ({filfat}) AND
                         "CODESTCLI" IN ('{est}') AND
                         "CODMER" IN ({prd})
                        
                GROUP BY "CODFILEPD", "CODFILFAT", "CODESTUNI", "CODPRD"
                '''.format(month_interval="','".join(month_interval),
                           filepd=','.join(filepd),
                           filfat=','.join(filfat),
                           est="','".join(est),
                           prd=','.join(prd))

    rpr_mpc = pd.read_sql_query(query_mpc, db)
    df = pd.merge(df, rpr_mpc, how='left', on=[
                  'CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'CODPRD'])

    # Busncando representatividade histórica do superflex
    query_sfx = '''
                SELECT   "CODFILEPD", 
                         "CODFILFAT", 
                         "CODESTCLI" AS "CODESTUNI",
                         "CODMER" AS "CODPRD",
                         SUM("VLRSUPFLX")/SUM("VLRVNDLIQ") AS "RPRHSTSUPFLX"
                        
                FROM     "MOVVNDHSTFIM"
                
                WHERE    "NUMANOMES" IN ('{month_interval}') AND
                         "CODFILEPD" IN ({filepd}) AND
                         "CODFILFAT" IN ({filfat}) AND
                         "CODESTCLI" IN ('{est}') AND
                         "CODMER" IN ({prd})
                        
                GROUP BY "CODFILEPD", "CODFILFAT", "CODESTUNI", "CODPRD"
                '''.format(month_interval="','".join(month_interval),
                           filepd=','.join(filepd),
                           filfat=','.join(filfat),
                           est="','".join(est),
                           prd=','.join(prd))

    rpr_sfx = pd.read_sql_query(query_sfx, db)

    df = pd.merge(df, rpr_sfx, how='left', on=[
                  'CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'CODPRD'])

    # Pendente inserir query para obter a representatividade histórica
    # das despesas financeiras
    df['RPRHSTDESFIN'] = 0

    df.fillna(0, inplace=True)

    return df


def get_els_params(df, prd, filepd, filfat, est):

    '''
    Busca o parâmetro de elasticidade dado um código de produto e estado.
    
    INPUT:
        df: pandas DataFrame que vai receber as informações obtidas
        prd: lista com o código de produto,
        filepd: lista com o código da filial de expedição,
        filfat: lista com o código da filial de faturamento,
        est: lista de strings com a sigla do estado.
    OUTPUT:
        df: pandas DataFrame de input com a coluna de elasticidade.

    AUTOR: Maurício Reis do Nascimento
    DATA: 03/03/2020
    '''

    query_els = '''
            SELECT  "exp" AS "CODFILEPD", 
                    "filfat" AS "CODFILFAT", 
                    "codmer" as "CODPRD",
                    "uf" as "CODESTUNI", 
                    "elast_proposta" as "Elasticidade"

            FROM    "ELASTICIDADE_DEMANDA"

            WHERE   "uf" IN ('{est}') AND
                    "exp" IN ({filepd}) AND 
                    "filfat" IN ({filfat}) AND
                    "codmer" in ({prd})

            '''.format(est="','".join(est),
                       filepd=','.join(filepd),
                       filfat=','.join(filfat),
                       prd=','.join(prd))

    els = pd.read_sql_query(query_els, db)
    
    if not els.empty:

        df = pd.merge(df, els, how='left',
                        on=['CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'CODPRD'])
                
        for i in range(df.shape[0]):
            if df.loc[i, 'Elasticidade'] > -1:
                df['PRDINELAST'] = 1
            else:
                df['PRDINELAST'] = 0
        
        return df
        
    else:
    
        # Buscando parâmetros de elasticidade
        query_sml = '''
                SELECT  "CODPRD", 
                        "codsml"
                FROM    "prdsml"
                WHERE   "CODPRD" IN ({prd})
                '''.format(prd=','.join(prd))

        codsml = pd.read_sql_query(query_sml, db)

        codsml_as_str = [str(x) for x in codsml['codsml']]

        df = pd.merge(df, codsml, how='left', on=['CODPRD'])

        query_els = '''
                SELECT  "exp" AS "CODFILEPD", 
                        "filfat" AS "CODFILFAT", 
                        "codsml",
                        "uf" as "CODESTUNI", 
                        "elast_proposta" as "Elasticidade"

                FROM    "ELASTICIDADE_DEMANDA"
                WHERE   "uf" IN ('{est}') AND
                        "exp" IN ({filepd}) AND 
                        "filfat" IN ({filfat}) AND
                        "codsml" in ({sml})

                '''.format(est="','".join(est),
                           filepd=','.join(filepd),
                           filfat=','.join(filfat),
                           sml=','.join(codsml_as_str))

        els = pd.read_sql_query(query_els, db)
        els_result = els.iloc[[0]]
        els_result['Elasticidade'] = els['Elasticidade'].mean()
        
        df = pd.merge(df, els_result, how='left',
                on=['CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'codsml'])
        df.drop('codsml', axis=1, inplace=True)
        
        for i in range(df.shape[0]):
            if df.loc[i, 'Elasticidade'] > -1:
                df['PRDINELAST'] = 1
            else:
                df['PRDINELAST'] = 0
        
        return df


def get_mean_price_quantity(df, prd, filepd, filfat, est, month, year, last_n_weeks):
    '''
    Busca o preço médio praticado e quantidade média vendida nas últimas
    52 semanas. Parâmetros necessários para cálculo do preço de venda a partir
    do volume de vendas e vice-versa (elasticidade).
    
    INPUT:
        df: pandas DataFrame que vai receber as informações obtidas
        prd: lista com o código de produto,
        est: lista de strings com a sigla do estado.
    OUTPUT:
        df: pandas DataFrame de input com a coluna de elasticidade.

    AUTOR: Maurício Reis do Nascimento
    DATA: 03/03/2020
    '''

    def get_last_n_weeks(last_n_weeks):
        '''
        Retorna a data de 52 semanas atrás no formato 'AAAAMMS'

        INPUT:

        OUTPUT:
            week_interval: lista de strings referente à data de 52 semanas
                           atrás em formato 'AAAAMMS'.
        
        AUTOR: Maurício Reis do Nascimento
        DATA: 03/03/2020
        '''

        from math import ceil
        import datetime

        def week_of_month(dt):
            """
            Retorna a semana do mês para a data especificada.

            INPUT:
                dt: data em formato datetime.

            OUTPUT:
                int: semana do mês. 
            """

            first_day = dt.replace(day=1)

            dom = dt.day
            adjusted_dom = dom + first_day.weekday()

            return int(ceil(adjusted_dom/7.0))

        prev_date = datetime.datetime.today() - datetime.timedelta(days=(last_n_weeks+10)*7)
        prev_year = prev_date.year
        prev_month = prev_date.month
        prev_week = week_of_month(prev_date)

        week_interval = [str(prev_year)+str('0'+str(prev_month)
                        if prev_month < 10 else str(prev_month))+str(prev_week)]
        

        return week_interval

    week_interval = get_last_n_weeks(last_n_weeks)

    query = '''
         SELECT   "NUMANOMESSMN", 
                  "CODFILEPD", 
                  "CODFILFAT",
                  "CODESTCLI" AS "CODESTUNI",
                  "CODMER" AS "CODPRD",
                  SUM("VLRVNDLIQ") AS "VLRVNDLIQ",
                  SUM("VLRVNDLIQ")/SUM("QDEITE") AS "PCOMED",
                  SUM("QDEITE") AS "QTDMED"
         FROM     "MOVVNDHSTFIM"
         WHERE    "CODMER" IN ({prod}) AND 
                  "NUMANOMESSMN" >= '{week_interval}' AND 
                  "CODESTCLI" IN ('{est}') AND
                  "CODFILEPD" IN ({filepd}) AND 
                  "CODFILFAT" IN ({filfat}) AND 
                  "NUMANOMES" < {numanomes} AND
                  "VLRVNDLIQ" > 0
                  
         GROUP BY "CODFILEPD", "CODFILFAT", "CODESTUNI", "CODPRD", "NUMANOMESSMN"
         '''.format(prod=','.join(prd), week_interval=week_interval[0], est="','".join(est),
                    filepd=','.join(filepd), filfat=','.join(filfat), numanomes=year[0] + month[0])


    pco_qtd_med = pd.read_sql_query(query, db)
    pco_qtd_med = pco_qtd_med.sort_values(by='NUMANOMESSMN', ascending=False)
    pco_qtd_med = pco_qtd_med.iloc[:last_n_weeks]

    result = pco_qtd_med.iloc[[0]]

    result.drop(['NUMANOMESSMN', 'VLRVNDLIQ'], axis=1, inplace=True)

    result['PCOMED'] = pco_qtd_med['VLRVNDLIQ'].sum()/pco_qtd_med['QTDMED'].sum()

    result['QTDMED'] = pco_qtd_med['QTDMED'].mean()
    result['PCOMAX'] = pco_qtd_med['PCOMED'].max()
    result['PCOMIN'] = pco_qtd_med['PCOMED'].min()


    df = pd.merge(df, result, how='left', on=[
                  'CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'CODPRD'])

    df['VLRVOLVNDMED'] = df['PCOMED']*df['QTDMED']

    return df


def calculate_sug_price_opt(df, trava_pco_min, trava_pco_max):
    
    def calculate_sales_vol(df, x):
        vol = (
               x*(df['Elasticidade'] * df['QTDMED'] *(x - df['PCOMED'])/df['PCOMED']
               + df['QTDMED'])
               )*df['QDEDIASMN']/7.
        return vol

    def objective_function(x, df):

        MSE = sum((df['VOLVNDSUG'] - calculate_sales_vol(df, x))**2)

        return MSE

    bnds=[(df.loc[i, 'PCOMIN'] - trava_pco_min*df.loc[i, 'PCOMIN'],
           df.loc[i, 'PCOMAX'] + trava_pco_max*df.loc[i, 'PCOMAX'])
           for i in range(df.shape[0])]

    bnds

    initial = [0]*df.shape[0]

    from scipy import optimize
    res = optimize.minimize(objective_function, args=df, x0=initial, bounds=bnds, tol=1e-32)

    res

    df['VLRPCOSUG'] = res.x
    
    return df


def fix_sug_prc(df):
    
    for i in range(df.shape[0]):
        if df.loc[i, 'VOLVNDSUG'] < df.loc[i, 'VLRVOLVNDMED']*df['QDEDIASMN']/7:
            df.loc[i,'VLRPCOSUG'] = df.loc[i, 'PCOMED']
            df.loc[i, 'MEDIAMAIORMETA'] = 1
        else:
            df.loc[i, 'MEDIAMAIORMETA'] = 0
    
    return df

def calculate_suggested_quantity(df):
    df['QTDSUG'] = (df['Elasticidade']*df['QTDMED']*
                    (df['VLRPCOSUG']-df['PCOMED'])/df['PCOMED'] + 
                     df['QTDMED'])*df['QDEDIASMN']/7.

    return df


def calculate_base_price(df):
    # Cálculo do Preço Base a partir do preço de venda, descontando valor médio histórico com margem por canal,
    # SuperFlex e Despesas Financeiras e adicionando valor médio histórico de benefício e flexível.
    def base_price(df):
        pcobase = (
            df['VLRPCOSUG']
            + df['VLRPCOSUG']*df['RPRHSTBNF']
            + df['VLRPCOSUG']*df['RPRHSTFLX']
            - df['VLRPCOSUG']*df['RPRHSTMRGCNL']
            - df['VLRPCOSUG']*df['RPRHSTSUPFLX']
            - df['VLRPCOSUG']*df['RPRHSTDESFIN']
        )

        return pcobase

    df['VLRPCOBASESUG'] = df.apply(base_price, axis=1)

    return df


def price_decomposition(df, prd, est, filepd, filfat):

    def calculate_CMV(df):
        CMV = (
            (df['VLRPCOBASESUG']*(1-df['FLEX']/100) + df['COMPLEMENTO'])
            * (1 - df['ICMS']/100 - df['PIS_COFINS']/100*(1-df['ICMS']/100) - df['DEVOLUÇÃO']/100)
            * (1 - df['MRGBRTPEROCD']/100)
            + df['Rebate']
            + (df['VerbaPco']*df['FundPco']/100)
            - df['Bonificado']
        )
        return CMV

    # Buscando na matriz de preço alíquotas de impostos, flexível e devolução.
    query = '''
        SELECT   "CODFILEMP" AS "CODFILEPD", 
                 "CODFILEMPFAT" AS "CODFILFAT", 
                 "CODESTUNI", 
                 "CODMER" AS "CODPRD",
                 "FLEX", 
                 "ICMS", 
                 "PIS_COFINS", 
                 "COMPLEMENTO", 
                 "DEVOLUÇÃO"
                 
        FROM     "BASE_PRECO"
        WHERE    "CODFILEMP" IN ({filepd}) AND 
                 "CODFILEMPFAT" IN ({filfat}) AND 
                 "CODESTUNI" IN ('{est}') AND
                 "CODMER" IN ({prd}) AND 
                 "DATA_PREÇO" = (
                                                         SELECT MAX("DATA_PREÇO")
                                                         FROM "BASE_PRECO"
                                                         WHERE "CODFILEMP" IN ({filepd}) AND 
                                                                "CODFILEMPFAT" IN ({filfat}) AND
                                                                "CODESTUNI" IN ('{est}') AND 
                                                                "CODMER" IN ({prd})
                                                         )      
        '''.format(filepd=','.join(filepd), filfat=','.join(filfat), est="','".join(est), prd=','.join(prd))

    params_pco = pd.read_sql_query(query, db).loc[[0]]

    df = pd.merge(df, params_pco, how='left',
                  on=['CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'CODPRD'])

    # Consigo tirar essas verbas de algum lugar?
    df['VerbaPco'] = 0
    df['Bonificado'] = 0
    df['Rebate'] = 0
    df['FundPco'] = 100

    df['VLRFLXSUG'] = df['VLRPCOBASESUG']*df['FLEX']/100
    df['VLRDEVSUG'] = (df['VLRPCOBASESUG'] -
                       df['VLRFLXSUG'])*df['DEVOLUÇÃO']/100
    df['VLRPISCOFSUG'] = (df['VLRPCOBASESUG'] - df['VLRFLXSUG']) * \
        ((df['PIS_COFINS']/100)*(1-df['ICMS']/100))
    df['VLRICMSSUG'] = (df['VLRPCOBASESUG'] - df['VLRFLXSUG'])*df['ICMS']/100
    df['VLRMRGBRTSUG'] = ((df['VLRPCOBASESUG'] - df['VLRFLXSUG'] - df['VLRDEVSUG'] - df['VLRPISCOFSUG'] - df['VLRICMSSUG'])
                          * df['MRGBRTPEROCD']/100)

    df['VLRCMVPCOSUG'] = df.apply(calculate_CMV, axis=1)
    return df


def base_price_composition(df):

    def calculate_base_price_from_CMV(df):
        pco_base = (((df['VLRCMVPCOPLN']+df['VLRBONPLN']) - (df['VLRVBAPCOPLN']*df['FundPco']/100) - df['VLRVRBPLN'])
                    / ((1 - df['ICMS']/100 - df['PIS_COFINS']/100*(1-df['ICMS']/100) - df['DEVOLUÇÃO']/100)*(1-df['MRGBRTPERPLN']/100))
                    / (1 - df['FLEX']/100)
                    )
        return pco_base

    df['VLRPCOBASEPLN'] = df.apply(calculate_base_price_from_CMV, axis=1)

    df['VLRFLXPLN'] = df['VLRPCOBASEPLN']*df['FLEX']/100
    df['VLRDEVPLN'] = (df['VLRPCOBASEPLN'] -
                       df['VLRFLXPLN'])*df['DEVOLUÇÃO']/100
    df['VLRPISCOFPLN'] = (df['VLRPCOBASEPLN'] - df['VLRFLXPLN']) * \
        ((df['PIS_COFINS']/100)*(1-df['ICMS']/100))
    df['VLRICMSPLN'] = (df['VLRPCOBASEPLN'] - df['VLRFLXPLN'])*df['ICMS']/100
    df['VLRMRGBRTPLN'] = ((df['VLRPCOBASEPLN'] - df['VLRFLXPLN'] - df['VLRDEVPLN'] - df['VLRPISCOFPLN'] - df['VLRICMSPLN'])
                          * df['MRGBRTPERPLN']/100)

    return df


def base_price_to_sales_price(df):

    def calculate_sales_price(df):
        pco_venda = (df['VLRPCOBASEPLN'] /
                    (1 + df['RPRHSTBNF'] + df['RPRHSTFLX'] - df['RPRHSTMRGCNL'] - df['RPRHSTSUPFLX'] - df['RPRHSTDESFIN']))

        return pco_venda
    
    df['VLRPCOPLN'] = df.apply(calculate_sales_price, axis=1)

    return df


def sales_volume_from_price(df):

    def calculate_sales_volume(df):

        vol =  (df['VLRPCOPLN']*
               (df['Elasticidade']*df['QTDMED']*(df['VLRPCOPLN']-df['PCOMED'])/
                df['PCOMED'] + df['QTDMED']))*df['QDEDIASMN']/7
        
        if vol >=0:
            return vol
        else:
            return 0
    
    df['VOLVNDPLN'] = df.apply(calculate_sales_volume, axis=1)

    return df

def pln_qtt(df):
    
    def calculate_pln_qtt(df):

        qtt = df['VOLVNDPLN']/df['VLRPCOPLN']

        return qtt
    
    df['QTDPLN'] = df.apply(calculate_pln_qtt, axis=1)

    return df


def calculate_month_results(final):
    
    mes = final.iloc[[0]]

    mes['WEEK'] = 'MÊS'

    mes['VOLVNDSUG'] = final['VOLVNDSUG'].sum()

    mes['VOLVNDSUGALC'] = final['VOLVNDSUGALC'].sum()

    mes['VLRPCOSUG'] = sum(final['VLRPCOSUG']*final['QTDSUG'])/final['QTDSUG'].sum()

    mes['VLRPCOBASESUG'] = sum(final['VLRPCOBASESUG']*final['QTDSUG'])/final['QTDSUG'].sum()

    mes['VLRIMPTOTSUG'] = sum(final['VLRIMPTOTSUG']*final['QTDSUG'])/final['QTDSUG'].sum()
    mes['VLRICMSSUG'] = sum(final['VLRICMSSUG']*final['QTDSUG'])/final['QTDSUG'].sum()
    mes['VLRPISCOFSUG'] = sum(final['VLRPISCOFSUG']*final['QTDSUG'])/final['QTDSUG'].sum()
    mes['VLRDEVSUG'] = sum(final['VLRDEVSUG']*final['QTDSUG'])/final['QTDSUG'].sum()
    mes['VLRFLXSUG'] = sum(final['VLRFLXSUG']*final['QTDSUG'])/final['QTDSUG'].sum()
    mes['VRBUNTSUGSUG'] = sum(final['VRBUNTSUGSUG']*final['QTDSUG'])/final['QTDSUG'].sum()

    mes['VLRCMVPCOSUG'] = sum(final['VOLVNDSUG']*final['VLRCMVPCOSUG'])/final['VOLVNDSUG'].sum()
    
    mes['VOLVNDPLN'] = final['VOLVNDPLN'].sum()

    mes['VLRPCOPLN'] = sum(final['VLRPCOPLN']*final['QTDPLN'])/final['QTDPLN'].sum()

    mes['VLRPCOBASEPLN'] = sum(final['VLRPCOBASEPLN']*final['QTDPLN'])/final['QTDPLN'].sum()

    mes['VLRIMPTOTPLN'] = sum(final['VLRIMPTOTPLN']*final['QTDPLN'])/final['QTDPLN'].sum()
    mes['VLRICMSPLN'] = sum(final['VLRICMSPLN']*final['QTDPLN'])/final['QTDPLN'].sum()
    mes['VLRPISCOFPLN'] = sum(final['VLRPISCOFPLN']*final['QTDPLN'])/final['QTDPLN'].sum()

    mes['VLRDEVPLN'] = sum(final['VLRDEVPLN']*final['QTDPLN'])/final['QTDPLN'].sum()
    mes['VLRFLXPLN'] = sum(final['VLRFLXPLN']*final['QTDPLN'])/final['QTDPLN'].sum()
    mes['VLRVRBPLN'] = sum(final['VLRVRBPLN']*final['QTDPLN'])/final['QTDPLN'].sum()
    mes['VLRCMVPCOPLN'] = sum(final['VLRCMVPCOPLN']*final['QTDPLN'])/final['QTDPLN'].sum()

    final = pd.concat([final, mes], axis=0, ignore_index=True)
    
    return final

def calculate_month_results_sug(final):
    
    mes = final.iloc[[0]]

    mes['WEEK'] = 'MÊS'

    mes['VOLVNDSUG'] = final['VOLVNDSUG'].sum()

    mes['VOLVNDSUGALC'] = final['VOLVNDSUGALC'].sum()

    mes['VLRPCOSUG'] = sum(final['VLRPCOSUG']*final['QTDSUG'])/final['QTDSUG'].sum()

    mes['VLRPCOBASESUG'] = sum(final['VLRPCOBASESUG']*final['QTDSUG'])/final['QTDSUG'].sum()

    mes['VLRIMPTOTSUG'] = sum(final['VLRIMPTOTSUG']*final['QTDSUG'])/final['QTDSUG'].sum()
    mes['VLRICMSSUG'] = sum(final['VLRICMSSUG']*final['QTDSUG'])/final['QTDSUG'].sum()
    mes['VLRPISCOFSUG'] = sum(final['VLRPISCOFSUG']*final['QTDSUG'])/final['QTDSUG'].sum()
    mes['VLRDEVSUG'] = sum(final['VLRDEVSUG']*final['QTDSUG'])/final['QTDSUG'].sum()
    mes['VLRFLXSUG'] = sum(final['VLRFLXSUG']*final['QTDSUG'])/final['QTDSUG'].sum()
    mes['VRBUNTSUGSUG'] = sum(final['VRBUNTSUGSUG']*final['QTDSUG'])/final['QTDSUG'].sum()

    mes['VLRCMVPCOSUG'] = sum(final['VOLVNDSUG']*final['VLRCMVPCOSUG'])/final['VOLVNDSUG'].sum()

    final = pd.concat([final, mes], axis=0, ignore_index=True)
    
    return final

def calculate_month_results_pln(final):
    
    mes = final.iloc[[0]]

    mes['WEEK'] = 'MÊS'

    mes['VOLVNDPLN'] = final['VOLVNDPLN'].sum()

    mes['VLRPCOPLN'] = sum(final['VLRPCOPLN']*final['QTDPLN'])/final['QTDPLN'].sum()

    mes['VLRPCOBASEPLN'] = sum(final['VLRPCOBASEPLN']*final['QTDPLN'])/final['QTDPLN'].sum()

    mes['VLRIMPTOTPLN'] = sum(final['VLRIMPTOTPLN']*final['QTDPLN'])/final['QTDPLN'].sum()
    mes['VLRICMSPLN'] = sum(final['VLRICMSPLN']*final['QTDPLN'])/final['QTDPLN'].sum()
    mes['VLRPISCOFPLN'] = sum(final['VLRPISCOFPLN']*final['QTDPLN'])/final['QTDPLN'].sum()

    mes['VLRDEVPLN'] = sum(final['VLRDEVPLN']*final['QTDPLN'])/final['QTDPLN'].sum()
    mes['VLRFLXPLN'] = sum(final['VLRFLXPLN']*final['QTDPLN'])/final['QTDPLN'].sum()
    mes['VLRVRBPLN'] = sum(final['VLRVRBPLN']*final['QTDPLN'])/final['QTDPLN'].sum()
    mes['VLRCMVPCOPLN'] = sum(final['VLRCMVPCOPLN']*final['QTDPLN'])/final['QTDPLN'].sum()

    final = pd.concat([final, mes], axis=0, ignore_index=True)
    
    return final


def calculate_sug_competitivity(df, prd, divfrn, est, month, year):
    
    numanomes = (year[0] + str(int(month[0])-1) if int(month[0]) > 1
                 else str(int(year[0])-1) + '12')
    
    query = '''
            SELECT   "CODPRD", 
                     "UF_Destino" AS "CODESTUNI", 
                     "codfrn" AS "CODDIVFRN", 
                     "pc_psq" AS "VLRPCOMRC"
            FROM     "COMPETITIVIDADE"
            
            WHERE    "CODPRD" IN ({prd}) AND 
                     "codfrn" IN ({divfrn}) AND
                     "UF_Destino" IN ('{est}') AND 
                     "NUMANOMES" = {numanomes}
            '''.format(prd=','.join(prd),
                       divfrn=','.join(divfrn),
                       est="','".join(est),
                       numanomes=numanomes)

    query_result = pd.read_sql_query(query, db)
    
    
    if query_result.empty:
        
        # print('Competitividade: mês em questão, retornou vazio. Pegando último mês disponível na base.')
        
        query = '''
                SELECT   "NUMANOMES", 
                         "CODPRD", 
                         "UF_Destino" AS "CODESTUNI", 
                         "codfrn" AS "CODDIVFRN", 
                         "pc_psq" AS "VLRPCOMRC"
                         
                FROM     "COMPETITIVIDADE"
                WHERE    "CODPRD" IN ({prd}) AND 
                         "codfrn" IN ({divfrn}) AND
                         "UF_Destino" IN ('{est}') AND 
                         "NUMANOMES" = (
                                                                 SELECT "NUMANOMES"
                                                                 FROM "COMPETITIVIDADE"
                                                                 WHERE "CODPRD" IN ({prd}) AND 
                                                                       "codfrn" IN ({divfrn}) AND
                                                                       "UF_Destino" IN ('{est}')
                                                                 ORDER BY "NUMANOMES" DESC
                                                                 LIMIT 1
                                                                 )
                '''.format(prd=','.join(prd),
                           divfrn=','.join(divfrn),
                           est="','".join(est))
        
        query_result = pd.read_sql_query(query, db)
    
    if not query_result.empty:
        comp = query_result.iloc[[0]]

        comp['VLRPCOMRC'] = query_result['VLRPCOMRC'].mean()

        df = pd.merge(df, comp, on=['CODPRD', 'CODESTUNI', 'CODDIVFRN'], how='left')

        df['VLRCOMPSUG'] = df['VLRPCOSUG']/df['VLRPCOMRC']*100
    
    else:
        df['VLRPCOMRC'] = 0
        df['VLRCOMPSUG'] = 0

    return df

def cmv_etq(df, prd, filepd, divfrn):

    query = '''
            SELECT   "CODPRD", 
                     "CODDIVFRN", 
                     "CODFIL" AS "CODFILEPD",
                     "VLRDIRCSTMEDMER" AS "VLRCMVCMPATU"
            FROM     "MOVETQ"
            WHERE    "CODPRD" IN ({prd}) AND 
                     "CODFIL" IN ({filepd}) AND
                     "CODDIVFRN" IN ({divfrn}) AND
                     "VLRDIRCSTMEDMER" != 0
            ORDER BY "DATINI" DESC
            LIMIT 1
            '''.format(prd=','.join(prd),
                       filepd=','.join(filepd),
                       divfrn=','.join(divfrn))

    query_result = pd.read_sql_query(query, db)

    df = pd.merge(df, query_result, on=['CODDIVFRN', 'CODPRD', 'CODFILEPD'], how='left')
    
    return df


def get_current_etq_prc_cmv(df, prd, filepd, filfat):
    
    query = '''
            SELECT   "DATA_PREÇO", 
                     "CODFILEMP" AS "CODFILEPD",
                     "CODFILEMPFAT" AS "CODFILFAT", 
                     "CODMER" AS "CODPRD",
                     "CUSTO" AS "VLRCMVPCOATU"
            FROM     "BASE_PRECO"
            WHERE    "CODMER" IN ({prd}) AND 
                     "CODFILEMP" IN ({filepd})
            '''.format(prd=','.join(prd),
                       filepd=','.join(filepd))

    base_preco = pd.read_sql_query(query, db)

    base_preco = base_preco.loc[base_preco['DATA_PREÇO']==base_preco['DATA_PREÇO'].value_counts().index[0]]

    result = base_preco.loc[base_preco['CODFILFAT']==int(filfat[0])].iloc[[0]]
    
    result.drop('DATA_PREÇO', axis=1, inplace=True)

    result['FTRCMVCMPCMVPCO'] = result['VLRCMVPCOATU']/base_preco['VLRCMVPCOATU'].value_counts().index[0]

    df = pd.merge(df, result, on=['CODFILEPD', 'CODFILFAT', 'CODPRD'], how='left')
    
    df['VLRCMVPCOATU'] = df['VLRCMVCMPATU'] * df['FTRCMVCMPCMVPCO']
    
    return df


def price_decomposition_without_query(df):

    def calculate_CMV(df):
        CMV = (
            (df['VLRPCOBASESUG']*(1-df['FLEX']/100) + df['COMPLEMENTO'])
            * (1 - df['ICMS']/100 - df['PIS_COFINS']/100*(1-df['ICMS']/100) - df['DEVOLUÇÃO']/100)
            * (1 - df['MRGBRTPEROCD']/100)
            + df['Rebate']
            + (df['VerbaPco']*df['FundPco']/100)
            - df['Bonificado']
        )
        return CMV

    # Consigo tirar essas verbas de algum lugar?
    df['VerbaPco'] = 0
    df['Bonificado'] = 0
    df['Rebate'] = 0
    df['FundPco'] = 100

    df['VLRFLXSUG'] = df['VLRPCOBASESUG']*df['FLEX']/100
    df['VLRDEVSUG'] = (df['VLRPCOBASESUG'] -
                       df['VLRFLXSUG'])*df['DEVOLUÇÃO']/100
    df['VLRPISCOFSUG'] = (df['VLRPCOBASESUG'] - df['VLRFLXSUG']) * \
        ((df['PIS_COFINS']/100)*(1-df['ICMS']/100))
    df['VLRICMSSUG'] = (df['VLRPCOBASESUG'] - df['VLRFLXSUG'])*df['ICMS']/100
    df['VLRMRGBRTSUG'] = ((df['VLRPCOBASESUG'] - df['VLRFLXSUG'] - df['VLRDEVSUG'] - df['VLRPISCOFSUG'] - df['VLRICMSSUG'])
                          * df['MRGBRTPEROCD']/100)

    df['VLRCMVPCOSUG'] = df.apply(calculate_CMV, axis=1)
    return df


def compare_sug_atu(df):
    counter = 0
    
    check = df.copy()

    for i in range(check.shape[0]):
        check.loc[i, 'VLRCMVCMPPLN'] = check.loc[i, 'VLRCMVCMPATU']
        check.loc[i, 'VLRBONPLN'] = check.loc[i, 'Bonificado']
        check.loc[i, 'VLRVRBPLN'] = 0
        check.loc[i, 'VLRVBAPCOPLN'] = check.loc[i, 'VerbaPco']
        check.loc[i, 'MRGBRTPERPLN'] = check.loc[i, 'MRGBRTPEROCD']

    check = etqcmv_to_prccmv(check)
    check = base_price_composition(check)
    check = base_price_to_sales_price(check)
    check = sales_volume_from_price(check)

    df['ATUMAIORMETA'] = 0

    for i in range(df.shape[0]):
        if df.loc[i, 'VOLVNDSUG'] < check.loc[i, 'VOLVNDPLN']:
            df.loc[i, 'VLRPCOSUG'] = check.loc[i, 'VLRPCOPLN']
            df.loc[i, 'ATUMAIORMETA'] = 1
            counter = 1
            
    if counter == 1:
        df = calculate_suggested_quantity(df)
        df = calculate_base_price(df)
        df = price_decomposition_without_query(df)
    
    return df


def suggested_funding_sug(df):
    
    def calculate_suggested_funding(df):
        if df['VLRCMVPCOATU'] > df['VLRCMVPCOSUG']:
            return df['VLRCMVPCOATU'] - df['VLRCMVPCOSUG']
        else:
            return 0
    
    df['VRBUNTSUGSUG'] = df.apply(calculate_suggested_funding, axis=1)
    
    return df


def calculate_accomplished_volume_of_sales(df):
    
    df['VOLVNDSUGALC'] = df['VLRPCOSUG']*df['QTDSUG']
    
    for i in range(df.shape[0]):
        if df.loc[i, 'VOLVNDSUG'] > df.loc[i, 'VOLVNDSUGALC']:
            df.loc[i, 'VNDSUGMAIORVNDALC'] = 1
        else:
            df.loc[i, 'VNDSUGMAIORVNDALC'] = 0
    
    return df


def etqcmv_to_prccmv(df):
    
    df['VLRCMVPCOPLN'] = df['VLRCMVCMPPLN']*df['FTRCMVCMPCMVPCO']
    
    return df


def suggested_funding_pln(df):
    
    def calculate_suggested_funding(df):
        if df['VLRCMVPCOPLN'] > df['VLRCMVPCOSUG']:
            return df['VLRCMVPCOPLN'] - df['VLRCMVPCOSUG']
        else:
            return 0
    
    df['VRBUNTSUGPLN'] = df.apply(calculate_suggested_funding, axis=1)
    
    return df

def calculate_pln_competitivity(df):
    if df['VLRPCOMRC'].sum() != 0:

        df['VLRCOMPPLN'] = df['VLRPCOPLN']/df['VLRPCOMRC']*100
    else:
        df['VLRCOMPPLN'] = 0

    return df


def compare_pln_sug(df):
    for i in range(df.shape[0]):
        if df.loc[i, 'VOLVNDPLN'] >= df.loc[i, 'VOLVNDSUG']:
            df.loc[i, 'VRBUNTSUGPLN'] = 0
            
    return df