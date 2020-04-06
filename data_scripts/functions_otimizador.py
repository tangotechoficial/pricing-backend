import pandas as pd
import time
import numpy as np
import sqlalchemy


conn_string = 'postgres://postgres:Martins*2020@pricing-data-parsing.cq8kmgnsewpt.us-east-1.rds.amazonaws.com/pricing_analitica2'
db = sqlalchemy.create_engine(conn_string)

def etqcmv_to_prccmv(df):
    
    df['VLRCMVPCOPLN'] = df['VLRCMVCMPPLN']*df['FTRCMVCMPCMVPCO']
    
    return df
    

def base_price_composition_opt(df):

    df['VLRBONPLN'] = df['Bonificado']
    df['VLRVBAPCOPLN'] = df['VerbaPco']

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
        
        if vol >= 0:
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

def sales_vol_from_cmv(fund, df_nesc, df_base, week, opt):
    
    df_nesc = df_nesc.copy()
    df_base = df_base.copy()
    
        
    df_nesc = etqcmv_to_prccmv(df_nesc)
        
    if opt != 0:
        df_nesc['MRGBRTPERPLN'] = df_nesc['MRGBRTPERGAP']
    else:
        df_nesc['MRGBRTPERPLN'] = df_nesc['MRGBRTPEROCD']
    
    df_nesc['VLRVRBPLN'] = df_nesc['VLRVRBPLN'] + fund

    df_nesc = base_price_composition_opt(df_nesc)

    df_nesc = base_price_to_sales_price(df_nesc)

    df_nesc = sales_volume_from_price(df_nesc)

    df_nesc['VOLVNDSUGALC'] = df_nesc['VOLVNDPLN']
    
    df_nesc['VLRPCOSUGALC'] = df_nesc['VLRPCOPLN']
    
    df_nesc['QTDOTM'] = df_nesc['VOLVNDSUGALC']/df_nesc['VLRPCOSUGALC']

    # for i in range(df.shape[0]):
    #     if df.loc[i, 'VOLVNDSUGALC'] < df.loc[i, 'VOLVNDPLN']:
    #         df.loc[i, 'VLRPCOPLN'] = df.loc[i, 'VLRPCOPLN']
    #         df.loc[i, 'QTDPLN'] = df.loc[i, 'QTDPLN']
    #         df.loc[i, 'VOLVNDSUGALC'] = df.loc[i, 'VOLVNDPLN']

    # verba_necessaria = df_nesc['VLRTOTVRBPLN'] = df_nesc['VRBUNTSUGPLN']*df_nesc['QTDPLN']
    
    if opt != 0:
        df_nesc['MRGBRTSUGALC'] = df_nesc['VOLVNDSUGALC']*df_nesc['RPRRCTLIQ']*df_nesc['MRGBRTPERGAP']/100
    else:
        df_nesc['MRGBRTSUGALC'] = df_nesc['VOLVNDSUGALC']*df_nesc['RPRRCTLIQ']*df_nesc['MRGBRTPEROCD']/100

    mask1 = df_base['WEEK'].astype(int) >= week-1
    mask2 = df_base['NEED_FUNDING']==1

    if opt == 1:
        df_base.loc[~mask1, 'VOLVNDOTM'] = df_base.loc[~mask1, 'VOLVNDREAL']
        df_base.loc[(mask1) & (mask2), 'VOLVNDOTM'] = df_nesc['VOLVNDSUGALC'].values
        df_base.loc[(mask1) & (~mask2), 'VOLVNDOTM'] = df_base.loc[(mask1) & (~mask2), 'VOLVNDPLN']
        df_base.loc[~mask1, 'VLRPCOOTM'] = df_base.loc[~mask1, 'VLRPCOREAL']
        df_base.loc[(mask1) & (mask2), 'VLRPCOOTM'] = df_nesc['VLRPCOSUGALC'].values
        df_base.loc[(mask1) & (~mask2), 'VLRPCOOTM'] = df_base.loc[(mask1) & (~mask2), 'VLRPCOPLN']



      
    else:
        df_base.loc[~mask1, 'VOLVNDOTM'] = df_base.loc[~mask1, 'VOLVNDREAL']
        df_base.loc[~mask1, 'MRGBRTOTM'] = df_base.loc[~mask1, 'MRGBRTREAL']
        df_base.loc[~mask1, 'VLRPCOOTM'] = df_base.loc[~mask1, 'VLRPCOREAL']

        df_base.loc[(mask1) & (mask2), 'VOLVNDOTM'] = df_nesc['VOLVNDSUGALC'].values
        df_base.loc[(mask1) & (mask2), 'MRGBRTOTM'] = df_nesc['MRGBRTSUGALC'].values
        df_base.loc[(mask1) & (mask2), 'VLRPCOOTM'] = df_nesc['VLRPCOSUGALC'].values

        df_base.loc[(mask1) & (~mask2), 'VOLVNDOTM'] = df_base.loc[(mask1) & (~mask2), 'VOLVNDPLN']
        df_base.loc[(mask1) & (~mask2), 'MRGBRTOTM'] = df_base.loc[(mask1) & (~mask2), 'MRGBRTPLN']
        df_base.loc[(mask1) & (~mask2), 'VLRPCOOTM'] = df_base.loc[(mask1) & (~mask2), 'VLRPCOPLN']

        df_base['RCTLIQOTM'] = df_base['VOLVNDOTM']*df_base['RPRRCTLIQ']
    
    if opt != 1:
        for prd in df_base['CODPRD'].unique():
            mask = df_base['CODPRD'] == prd
            
            for i in df_base.loc[mask].index:
                if df_base.loc[i, 'RCTLIQOTM'] == 0:
                    df_base.loc[i, 'MRGBRTPEROTM'] = 0
                else:
                    df_base.loc[i, 'MRGBRTPEROTM'] = df_base.loc[i, 'MRGBRTOTM']/df_base.loc[i, 'RCTLIQOTM']
        df_base['MRGBRTPEROTM'].fillna(0, inplace=True)
    
    if opt == 1:
        return df_base, df_nesc['QTDOTM']
    else:
        return df_base
    
def optimize_nesc_funding(df_base, df_nesc, week, initial):
    
    def objective_function(x, df_base, df_nesc):
        
        vol, qtd = sales_vol_from_cmv(x, df_nesc, df_base, week, opt=1)
        df1 = df_base.groupby('CODESTUNI', as_index=False)[['VOLVNDPLN']].sum()
        df2 = vol.groupby('CODESTUNI', as_index=False)[['VOLVNDOTM']].sum()
        return sum((df1['VOLVNDPLN'] - df2['VOLVNDOTM'])**2)

    
    bnds = [(0, None)]*df_nesc.shape[0]
    
    from scipy import optimize
    res = optimize.minimize(objective_function, args=(df_base, df_nesc) , x0=initial, bounds=bnds, tol=1e-16)
    
    return res.x


def get_pln_results(filt):

    query = '''
            SELECT   *
            FROM     "OUTPUT_PLN"
            WHERE    "CODSUBCTGPRD"={subctg} AND 
                     "CODCTGPRD"={ctg} AND 
                     "CODGRPPRD"={grpprd} AND
                     "CODFILEPD"={filepd} AND 
                     "CODFILFAT"={filfat} AND 
                     "CODDIVFRN"={divfrn}
            '''.format(subctg=filt['subctg'],
                       ctg=filt['ctg'],
                       grpprd=filt['grpprd'],
                       filepd=filt['filepd'],
                       filfat=filt['filfat'],
                       divfrn=filt['divfrn'])

    planejado = pd.read_sql_query(query, db)

    planejado

    planejado['VLRRCTLIQPLN'] = planejado['VOLVNDPLN']*planejado['RPRRCTLIQ']
    planejado['MRGBRTPLN'] = planejado['VLRRCTLIQPLN']*planejado['MRGBRTPEROCD']/100

    return planejado


def get_exec_results(filt, planejado):

    def week_of_month(dt):
        from math import ceil
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


    week = week_of_month(filt['date'])
    
    lista_semana = list(range(1, week+1))
    lista_semana = [str(x) for x in lista_semana]

    month = filt['date'].month if filt['date'].month >= 10 else '0'+str(filt['date'].month) 
    year = str(filt['date'].year)

    prds = [str(x) for x in planejado['CODPRD'].unique()]

    venda = '''
    SELECT DISTINCT  t1."CODMER" AS "CODPRD",  
                     SUBSTRING(t1."NUMANOMESDIA" :: varchar(255),1,4) AS "YEAR", 
                     SUBSTRING(t1."NUMANOMESDIA" :: varchar(255),5,2) AS "MONTH",
                     SUBSTRING(t1."NUMANOMESSMN" :: varchar(255),7,7) AS "WEEK", 
                     t1."CODFILEPD", 
                     t1."CODFILFAT",
                     t1."CODESTCLI" AS "CODESTUNI",
                     SUM(t1."VLRVNDLIQ") as "VOLVNDREAL",
                     SUM(t1."VLRRCTLIQ") AS "VLRRCTLIQREAL", 
                     SUM(t1."MARGEM_BRUTA")/SUM(t1."VLRRCTLIQ")*100 AS "MRGBRTPERREAL", 
                     SUM(t1."MARGEM_BRUTA") AS "MRGBRTREAL",
                     SUM(t1."VLRVNDLIQ")/SUM("QDEITE") AS "VLRPCOREAL",
                     SUM(t1."QDEITE") AS "QDTREAL", 
                     SUM(t1."CMV")/SUM(t1."QDEITE") AS "CMVREAL",
                     SUM(t1."FUNDING")/SUM(t1."QDEITE") AS "FUNDINGMEDREAL"
          FROM "MOVVNDHSTFIM" t1
          
          WHERE SUBSTRING(t1."NUMANOMESDIA" :: varchar(255),1,4) IN ('{year}') and 
                SUBSTRING(t1."NUMANOMESDIA" :: varchar(255),5,2) IN ('{month}')  and 
                SUBSTRING(t1."NUMANOMESSMN" :: varchar(255),7,1) IN ('{lista_semana}') and
                "CODMER" IN ({prds}) and
                "CODFILEPD" = {filepd} and
                "CODFILFAT" = {filfat}

          GROUP BY "WEEK",
                   "MONTH",
                   "YEAR",
                   t1."CODMER",
                   t1."CODFILEPD",
                   t1."CODFILFAT",
                   t1."CODESTCLI"   
    '''.format(lista_semana = "','".join(lista_semana),
               month = month,
               year = year,
               prds=','.join(prds),
               filepd=filt['filepd'],
               filfat=filt['filfat'])

    
    realizado = pd.read_sql_query(venda, db)

    realizado['WEEK'] = '0' + (realizado['WEEK'].astype(int) -1).astype(str)

    return realizado, week


def create_opt_base(planejado, realizado):
    for col in ['CODPRD', 'CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'WEEK', 'MONTH', 'YEAR']:
        realizado[col] = realizado[col].astype(str(planejado[col].dtypes))
        
    return pd.merge(planejado, realizado, how='left',
                    on=['CODPRD', 'CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'WEEK', 'MONTH', 'YEAR'])


def distribute_gap(base, week):
    weeks_remaining = base['WEEK'].astype(int).max() - (week-2)
    base.loc[(base['WEEK'].astype(int) < week-1)] = base.loc[(base['WEEK'].astype(int) < week-1)].fillna(0)

    for prd in base['CODPRD'].unique():

        mask1 = base['CODPRD'] == prd

        prod = base.loc[(mask1)]

        prod_prev_weeks = prod.loc[prod['WEEK'].astype(int) < week-1]
        
        if prod_prev_weeks['VOLVNDPLN'].sum() > prod_prev_weeks['VOLVNDREAL'].sum():
            gap_vendas = (prod_prev_weeks['VOLVNDPLN'].sum() - prod_prev_weeks['VOLVNDREAL'].sum())/weeks_remaining
            base.loc[(base['CODPRD']==prd) & (base['WEEK'].astype(int)>=week-1), 'VOLVNDGAP'] = prod.loc[prod['WEEK'].astype(int)>=week-1, 'VOLVNDPLN'] + gap_vendas

        else:
            base.loc[(base['CODPRD']==prd) & (base['WEEK'].astype(int)>=week-1), 'VOLVNDGAP'] = prod.loc[prod['WEEK'].astype(int)>=week-1, 'VOLVNDPLN']

        if prod_prev_weeks['MRGBRTPLN'].sum() > prod_prev_weeks['MRGBRTREAL'].sum():
            gap_margem = (prod_prev_weeks['MRGBRTPLN'].sum() - prod_prev_weeks['MRGBRTREAL'].sum())/weeks_remaining
            base.loc[(base['CODPRD']==prd) & (base['WEEK'].astype(int)>=week-1), 'MRGBRTGAP'] = prod.loc[prod['WEEK'].astype(int)>=week-1, 'MRGBRTPLN'] + gap_margem
        else:
            base.loc[(base['CODPRD']==prd) & (base['WEEK'].astype(int)>=week-1), 'MRGBRTGAP'] = prod.loc[prod['WEEK'].astype(int)>=week-1, 'MRGBRTPLN']
    
    base.loc[base['WEEK'].astype(int) == week-1, 'VOLVNDGAP'] = base.loc[base['WEEK'].astype(int) == week-1, 'VOLVNDGAP'] - base.loc[base['WEEK'].astype(int) == week-1, 'VOLVNDREAL']
    base['VLRRCTLIQGAP'] = base['VOLVNDGAP']*base['RPRRCTLIQ']

    base['MRGBRTPERGAP'] = base['MRGBRTGAP']/(base['VLRRCTLIQGAP'])*100

    base['NEED_FUNDING'] = base.apply(lambda x: 1 if x['VOLVNDGAP'] > x['VOLVNDPLN'] else 0, axis=1)

    return base


def create_opt_df(base, week):
    nesc = base[base['WEEK'].astype(int) >= week-1].copy()

    nesc = nesc[nesc['NEED_FUNDING'] == 1]

    cols = (nesc.columns.tolist()[:12] +
            ['RPRRCTLIQ', 'MRGBRTPEROCD'] +
            nesc.columns.tolist()[22:35] +
            ['FundPco'] + 
            nesc.columns.tolist()[39:46] +
            ['VOLVNDSUG', 'VLRPCOSUG', 'QTDSUG', 'VLRCMVCMPPLN', 'FTRCMVCMPCMVPCO',
             'VLRVRBPLN', 'VLRCMVPCOSUG', 'VOLVNDGAP', 'MRGBRTPERGAP']
           )

    nesc = nesc[cols]
    
    return nesc


def calculate_nesc_funding(base, nesc, week):
    
    def calculate_tot_fund(base):
        for i in base.index:
            if base.loc[i, 'VLRPCOOTM'] == 0:
                base.loc[i, 'VLRVRBTOTNSC'] = 0
            else:
                base.loc[i, 'VLRVRBTOTNSC'] = base.loc[i, 'VLRVRBNSC']*base.loc[i, 'VOLVNDOTM']/base.loc[i, 'VLRPCOOTM']
                
        return base

    test = sales_vol_from_cmv(fund=[0]*nesc.shape[0], df_nesc=nesc, df_base=base, week=week, opt=0)
    cond1 = test['VOLVNDOTM'].sum() > test['VOLVNDPLN'].sum()
    cond2 = (test['MRGBRTOTM'].sum()/test['RCTLIQOTM'].sum() >
             test['MRGBRTPLN'].sum()/test['VLRRCTLIQPLN'].sum())

    if (cond1) & (cond2):
        base = test.copy()
        base['VLRVRBNSC'] = 0
        print('Não precisa de otimização')
        base = calculate_tot_fund(base)
        base['RPRVRB'] = 0
        
        return base, [0]*nesc.shape[0]
        
    else:
        funding_unt = {}
        funding_tot = {}
        result = {}
        
        for param in [0.1, 0.3, 0.5]:            
            initial = param*nesc['VLRCMVCMPPLN'].values
            fund = optimize_nesc_funding(base, nesc, week, initial)
            base = sales_vol_from_cmv(fund, nesc, base, week, opt=2)
            mask = base['NEED_FUNDING'] == 1
            base.loc[mask, 'VLRVRBNSC'] = list(fund)
            base.loc[~mask, 'VLRVRBNSC'] = 0
            base = calculate_tot_fund(base)
            nesc_fund = base['VLRVRBTOTNSC'].sum()
            funding_unt[str(param)] = fund
            funding_tot[str(param)] = nesc_fund
            result[nesc_fund] = (base['VOLVNDPLN'].sum() - base['VOLVNDOTM'].sum())
            
        necessary_funding = funding_unt[min(funding_tot, key=funding_tot.get)]
        base = sales_vol_from_cmv(list(necessary_funding), nesc, base, week, opt=2)
        mask = base['NEED_FUNDING'] == 1
        base.loc[mask, 'VLRVRBNSC'] = list(necessary_funding)
        base.loc[~mask, 'VLRVRBNSC'] = 0
        base = calculate_tot_fund(base)
        base['RPRVRB'] = base['VLRVRBTOTNSC']/base['VLRVRBTOTNSC'].sum()
        nesc_fund = base['VLRVRBTOTNSC'].sum()
        

        return base, nesc_fund


def calculate_unt_fund(base, nesc, verba_disp, week):
    
    def iterate_qtd(nesc, param, mode):
        df_nesc = nesc.copy()

        for i in range(1000):

            if i == 0:
                df_nesc['QTDOTMI'] = df_nesc['QTDSUG']/param
                df_nesc['VLRVRBPLNI'] = df_nesc['VLRVRBPLN']
            else:
                df_nesc['QTDOTMI'] = df_nesc['QTDOTMF']



            df_nesc['VOLVNDSUG'] = df_nesc['VOLVNDGAP']

            df_nesc = etqcmv_to_prccmv(df_nesc)

            df_nesc['MRGBRTPERPLN'] = df_nesc['MRGBRTPEROCD']

            df_nesc['VLRVRBPLN'] = df_nesc['VLRVRBPLNI'] + proposed_fund/df_nesc['QTDOTMI']

            df_nesc = base_price_composition_opt(df_nesc)

            df_nesc = base_price_to_sales_price(df_nesc)

            df_nesc = sales_volume_from_price(df_nesc)

            df_nesc['VOLVNDSUGALC'] = df_nesc['VOLVNDPLN']

            df_nesc['VLRPCOSUGALC'] = df_nesc['VLRPCOPLN']

            df_nesc['QTDOTMF'] = df_nesc['VOLVNDSUGALC']/df_nesc['VLRPCOSUGALC']

            if np.abs(df_nesc['QTDOTMF'].sum() - df_nesc['QTDOTMI'].sum()) < 1e-6:
                break

        if mode == 0:
            try:
                return df_nesc['VLRVRBPLN'].value_counts()[-np.inf]
            except:
                try:
                    return df_nesc['VLRVRBPLN'].value_counts()[np.inf]
                except:
                    return 0
        else:
            return df_nesc
        
        
    base['VLRVRBDSPPRD'] = verba_disp*base['RPRVRB']
    
    proposed_fund = base.loc[base['NEED_FUNDING']==1, 'VLRVRBDSPPRD'].values
    params = {}

    for param in [0.3, 0.5, 1]:
        params[param] = iterate_qtd(nesc, param, mode=0)
        if params[param] == 0:
            min_param = param
            break
        else:
            min_param = min(params, key=params.get)

    nesc = iterate_qtd(nesc, min_param, mode=1)
    nesc['VLRVRBUNTDSP'] = nesc['VLRVRBPLN'] - nesc['VLRVRBPLNI']    
        
    return nesc

def calculate_avail_fund_results(base, nesc, week):
    base = sales_vol_from_cmv(nesc['VLRVRBUNTDSP'].values, nesc, base, week, opt=2)
    mask = base['NEED_FUNDING']==1
    base.loc[mask, 'VLRVRBUNTDSP'] = nesc['VLRVRBUNTDSP'].values
    base.loc[~mask, 'VLRVRBUNTDSP'] = 0
    return base

def calculate_comp(base):
    for i in base.index:
        if base.loc[i, 'VLRPCOMRC'] == 0:
            base.loc[i, 'VLRCOMPOTM'] = 0
        else:
            base.loc[i, 'VLRCOMPOTM'] = base.loc[i, 'VLRPCOOTM']/base.loc[i, 'VLRPCOMRC']
    
    return base

def calculate_unt_user_fund(base, nesc, week):
    
    def iterate_qtd(nesc, param, mode):
        df_nesc = nesc.copy()

        for i in range(1000):

            if i == 0:
                df_nesc['QTDOTMI'] = df_nesc['QTDSUG']/param
                df_nesc['VLRVRBPLNI'] = df_nesc['VLRVRBPLN']
            else:
                df_nesc['QTDOTMI'] = df_nesc['QTDOTMF']



            df_nesc['VOLVNDSUG'] = df_nesc['VOLVNDGAP']

            df_nesc = etqcmv_to_prccmv(df_nesc)

            df_nesc['MRGBRTPERPLN'] = df_nesc['MRGBRTPEROCD']

            df_nesc['VLRVRBPLN'] = df_nesc['VLRVRBPLNI'] + proposed_fund/df_nesc['QTDOTMI']


            df_nesc = base_price_composition_opt(df_nesc)

            df_nesc = base_price_to_sales_price(df_nesc)

            df_nesc = sales_volume_from_price(df_nesc)

            df_nesc['VOLVNDSUGALC'] = df_nesc['VOLVNDPLN']

            df_nesc['VLRPCOSUGALC'] = df_nesc['VLRPCOPLN']

            df_nesc['QTDOTMF'] = df_nesc['VOLVNDSUGALC']/df_nesc['VLRPCOSUGALC']

            if np.abs(df_nesc['QTDOTMF'].sum() - df_nesc['QTDOTMI'].sum()) < 1e-6:
                break

        if mode == 0:
            try:
                return df_nesc['VLRVRBPLN'].value_counts()[-np.inf]
            except:
                try:
                    return df_nesc['VLRVRBPLN'].value_counts()[np.inf]
                except:
                    return 0
        else:
            return df_nesc
        
        
    proposed_fund = base.loc[base['WEEK'].astype(int) >= week-1, 'VLRVRBDSPPRD'].values
    params = {}

    for param in [0.3, 0.5, 1]:
        params[param] = iterate_qtd(nesc, param, mode=0)
        if params[param] == 0:
            min_param = param
            break
        else:
            min_param = min(params, key=params.get)

    nesc = iterate_qtd(nesc, min_param, mode=1)
    nesc['VLRVRBUNTDSP'] = nesc['VLRVRBPLN'] - nesc['VLRVRBPLNI']    
        
    return nesc