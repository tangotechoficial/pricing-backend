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
    planejado_base, planejado = plano_compras_final.planejado(user_input, sugerido)
    return planejado_base
