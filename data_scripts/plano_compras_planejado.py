import pandas as pd
from . import plano_compras_final
from . import functions_planocompras_final as fpc
import sqlite3
import sqlalchemy
import boto3
import io
import warnings
warnings.filterwarnings('ignore')

# Necessário passar código do produto  a partir do filtro (prd)
# Necessário passar código UF como string a partir do filtro (est)
# Necessário passar user_input como dicionário (ver Notebook)
def run_planejado(prd, est, plan_month, plan_year, user_input, filepd=1, filfat=1):
    # Credenciais S3
    s3 = boto3.client('s3',
                  aws_access_key_id=r'AKIA2R5N7LHAEGZAMILX',
                  aws_secret_access_key=r'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')
    
    # Conectando banco postgres
    conn_string = 'postgres://postgres:Martins*2020@pricing-data-parsing.cq8kmgnsewpt.us-east-1.rds.amazonaws.com/pricing_analitica2'
    db = sqlalchemy.create_engine(conn_string)
    
    result= {}
    result['CODPRD'] = [prd]
    result['CODFILEPD'] = [filepd]
    result['CODFILFAT'] = [filfat]
    result['CODESTUNI'] = [est] 
    result['MONTH'] = [plan_month]
    result['YEAR'] = [plan_year]

    for key in result.keys():
        result[key] = [str(x) for x in result[key]]

    infos = fpc.get_complementary_infos(prd=result['CODPRD'])
    result['CODSUBCTGPRD'] = infos['CODSUBCTGPRD']
    result['CODCTGPRD'] = infos['CODCTGPRD']
    result['CODGRPPRD'] = infos['CODGRPPRD']
    result['CODDIVFRN'] = infos['CODDIVFRN']

    result['MONTH'] = ['0'+str(x) if int(x)<10 else str(x) for x in result['MONTH']]
    # result['YEAR'] =['2019']

    for key in result.keys():
        result[key] = [str(x) for x in result[key]]
        
        
    query = '''
        SELECT   "CODPRD",
                 "CODFILEPD",
                 "CODFILFAT",
                 "CODESTUNI",
                 "MONTH",
                 "YEAR",
                 "CODSUBCTGPRD",
                 "CODCTGPRD",
                 "CODGRPPRD",
                 "CODDIVFRN",
                 "WEEK",
                 "QDEDIASMN",
                 "VOLVNDLIQSUBOCD",
                 "MRGBRTOCD",
                 "VLRRCTLIQOCD",
                 "MRGBRTPEROCD",
                 "VLRHSTVNDLIQSUB",
                 "VLRHSTVNDLIQPRD",
                 "VLRHSTRCTLIQPRD",
                 "RPRHST",
                 "RPRRCTLIQ",
                 "VOLVNDSUG",
                 "MRGBRTSUG",
                 "VLRRCTLIQSUG",
                 "RPRHSTBNF",
                 "RPRHSTFLX",
                 "RPRHSTMRGCNL",
                 "RPRHSTSUPFLX",
                 "RPRHSTDESFIN",
                 "Elasticidade",
                 "PRDINELAST",
                 "PCOMED",
                 "QTDMED",
                 "PCOMAX",
                 "PCOMIN",
                 "VLRVOLVNDMED",
                 "VLRPCOSUG",
                 "QTDSUG",
                 "VLRPCOBASESUG",
                 "FLEX",
                 "ICMS",
                 "PIS_COFINS",
                 "COMPLEMENTO",
                 "DEVOLUÇÃO",
                 "VerbaPco",
                 "Bonificado",
                 "Rebate",
                 "FundPco",
                 "VLRFLXSUG",
                 "VLRDEVSUG",
                 "VLRPISCOFSUG",
                 "VLRICMSSUG",
                 "VLRMRGBRTSUG",
                 "VLRCMVPCOSUG",
                 "VLRCMVCMPATU",
                 "VLRCMVPCOATU",
                 "FTRCMVCMPCMVPCO",
                 "ATUMAIORMETA",
                 "VRBUNTSUGSUG",
                 "NUMANOMES",
                 "VLRPCOMRC",
                 "VLRCOMPSUG",
                 "VOLVNDSUGALC",
                 "VNDSUGMAIORVNDALC",
                 "VLRIMPTOTSUG",
                 "VLRVRBPLAN"
        
        FROM     "OUTPUT_PLN"
        WHERE    "CODPRD" = {prd} AND
                 "MONTH" = {month} AND
                 "CODFILEPD" = {filepd} AND
                 "CODFILFAT" = {filfat} AND
                 "CODESTUNI" = '{est}'
        '''.format(prd=result['CODPRD'][0],
                   month=int(result['MONTH'][0]),
                   filepd=int(result['CODFILEPD'][0]),
                   filfat=int(result['CODFILFAT'][0]),
                   est=result['CODESTUNI'][0])

    sugerido = pd.read_sql_query(query, db)
    
    sugerido['WEEK'] = sugerido.apply(lambda x: '0'+str(int(str(x['NUMANOMESSMN'])[-1])-1), axis=1)
    sugerido['MONTH'] = sugerido.apply(lambda x: int(str(x['NUMANOMESSMN'][4:6])),axis=1)
    sugerido['YEAR'] = sugerido.apply(lambda x: int(str(x['NUMANOMESSMN'][:4])), axis=1)

    planejado_base, planejado = plano_compras_final.planejado(user_input, sugerido)
    return planejado_base

def run_planejado_tela(week, plan_month, plan_year, prd, est, cmvcmp, vrbpln, filepd=1, filfat=1):
    conn_string = 'postgres://postgres:Martins*2020@pricing-data-parsing.cq8kmgnsewpt.us-east-1.rds.amazonaws.com/pricing_analitica2'
    db = sqlalchemy.create_engine(conn_string)



    query = '''
            SELECT   "CODPRD",
                     "CODFILEPD",
                     "CODFILFAT",
                     "CODESTUNI",
                     "NUMANOMESSMN",
                     "VLRVNDLIQCAL" AS "VOLVNDSUG",
                     "VLRPCOVNDLIQCAL" AS "VLRPCOSUG",
                     "VLRPCOMEDMCD" AS "VLRPCOMRC",
                     "VLRPCOBSECAL" AS "VLRPCOBASESUG",
                     "VLRFLXSUG",
                     "VLRDVLCAL" AS "VLRDEVSUG",
                     "VLRPISCAL" AS "VLRPISCOFSUG",
                     "VLRICMCAL" AS "VLRICMSSUG",
                     "VLRMRGBRTCAL" AS "VLRMRGBRTSUG",
                     "VLRCMVCAL" AS "VLRCMVPCOSUG",
                     "VLRCSTCMPMER"AS "VLRCMVCMPATU",
                     "VLRMCDCAL" AS "VLRCOMPSUG",
                     "VLRCMVPCOATU",
                     "VLRVNDPRVCTR" AS "VOLVNDSUGALC",
                     "VLRRBTOCD" AS "VRBUNTSUGSUG",
                     "VLRIMPTOTCAL" AS "VLRIMPTOTSUG"




            FROM     "mrt.MOVPLNCMPCAL"
            WHERE    "CODPRD" = {prd} AND
                     SUBSTRING("NUMANOMESSMN" :: varchar(255),1,6) IN ('{year_month}') AND
                     "CODFILEPD" = {filepd} AND
                     "CODFILFAT" = {filfat} AND
                     "CODESTUNI" = '{est}'
            '''.format(prd=prd,
                       year_month=str(plan_year)+ '0' + str(plan_month) if plan_month<10 else str(plan_month),
                       filepd=filepd,
                       filfat=filfat,
                       est=est)

    resultados = pd.read_sql_query(query, db)
    
    query = '''
        SELECT  "CODPRD",
                "CODFILEPD",
                "CODFILFAT",
                "CODESTUNI",
                "NUMANOMESSMN",
                "QDEDIAUTL" AS "QDEDIASMN",
                "VLRMRGBRTOCD" AS "MRGBRTPEROCD",
                "PERRCTLIQ" AS "RPRRCTLIQ",
                "FTRBNFCLIASC" AS "RPRHSTBNF",
                "FTRAJTDSCFLX" AS "RPRHSTFLX",
                "FTRVLRMER" AS "RPRHST",
                "PERMRGADICNLVND" AS "RPRHSTMRGCNL",
                "PERSUPFLX" AS "RPRHSTSUPFLX",
                "PERTBTICMDSPASR" AS "RPRHSTDESFIN",
                "QDEITE" AS "QTDSUG",
                "VLRMCDCAL" AS "Elasticidade",
                "VLRPCOBSEMER" AS "PCOMED",
                "QDEMEDITE" AS "QTDMED",
                "VLRPCOMAXCSM" AS "PCOMAX",
                "VLRPCOMNMCSM" AS "PCOMIN",
                "VLRMEDVNDMER" AS "VLRVOLVNDMED",
                "VLRFLXCNS" AS "FLEX",
                "VLRICM" AS "ICMS",
                "VLRPIS" AS "PIS_COFINS",
                "VLRCPLCSTPCO" AS "COMPLEMENTO",
                "VLRDVL" AS "DEVOLUÇÃO",
                "VLRVBA" AS "VerbaPco",
                "VLRBNF" AS "Bonificado",
                "VLRFNDRBTITE" AS "Rebate",
                "VLRFND" AS "FundPco",
                "PERCALPCOCMP" AS "FTRCMVCMPCMVPCO"
                
        FROM     "mrt.MOVPRMPLNCMP"
        WHERE    "CODPRD" = {prd} AND
                 SUBSTRING("NUMANOMESSMN" :: varchar(255),1,6) IN ('{year_month}') AND
                 "CODFILEPD" = {filepd} AND
                 "CODFILFAT" = {filfat} AND
                 "CODESTUNI" = '{est}'
    '''.format(prd=prd,
               year_month=str(plan_year)+ '0' + str(plan_month) if plan_month<10 else str(plan_month),
               filepd=filepd,
               filfat=filfat,
               est=est)
                
                
        
    parametros = pd.read_sql_query(query, db)

    sugerido = pd.merge(resultados, parametros, how='left', on=['CODPRD', 'CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'NUMANOMESSMN'])
    
    sugerido['WEEK'] = sugerido.apply(lambda x: '0'+str(int(str(x['NUMANOMESSMN'])[-1])-1), axis=1)
    sugerido['MONTH'] = sugerido.apply(lambda x: int(str(x['NUMANOMESSMN'][4:6])),axis=1)
    sugerido['YEAR'] = sugerido.apply(lambda x: int(str(x['NUMANOMESSMN'][:4])), axis=1)
    
    
    planejado = sugerido.loc[sugerido['WEEK'].astype(int) == week-1]
    planejado['VLRCMVCMPPLN'] = cmvcmp
    planejado['VLRBONPLN'] = planejado['Bonificado']
    planejado['VLRVRBPLN'] = vrbpln
    planejado['VLRVBAPCOPLN'] = planejado['VerbaPco']
    planejado['MRGBRTPERPLN'] = planejado['MRGBRTPEROCD']
    
    planejado = planejado_base, planejado = plano_compras_final.planejado_tela(planejado)
    
    dict_columns = {
                'CODPRD': 'CODPRD',
                'CODFILEPD': 'CODFILEPD',
                'CODFILFAT': 'CODFILFAT',
                'CODESTUNI': 'CODESTUNI',
                'NUMANOMESSMN': 'NUMANOMESSMN',
                'VOLVNDSUG': 'VLRVNDLIQCAL',
                'VOLVNDPLN':'VLRVNDLIQOCD',
                'VLRCOMPPLN':'VLRMCDOCD',
                'VLRPCOMRC': 'VLRPCOMEDMCD',
                'MRGBRTPEROCD':'MRGBRTPEROCD',
                'VLRPCOPLN': 'VLRPCOVNDLIQOCD',
                'VLRPCOBASEPLN': 'VLRPCOBSEOCD',
                'VLRIMPTOTPLN': 'VLRIMPTOTOCD',
                'VLRICMSPLN': 'VLRICMOCD',
                'VLRPISCOFPLN': 'VLRPISOCD',
                'VLRDEVPLN': 'VLRDVLOCD',
                'VLRFLXPLN': 'VLRFLXPLN',
                'VLRMRGBRTPLN': 'VLRMRGBRTOCD',
                'VRBUNTSUGPLN': 'VLRRBTCAL',
                'VLRVRBPLN': 'VLRVBAOCD',
                'VLRCMVPCOSUG': 'VLRCMVCAL',
                'VLRCMVPCOATU': 'VLRCMVPCOATU',
                'VLRCMVCMPPLN': 'VLRCSTCMPIDL'
                }
    
    planejado = planejado[dict_columns.keys()]

    planejado = planejado.rename(columns=dict_columns)
    
    return planejado