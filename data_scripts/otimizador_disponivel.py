import pandas as pd
import numpy as np
from . import functions_otimizador as fopt
from . import optimizer as opt
from datetime import date, datetime
import sqlalchemy
import boto3
import io




def run_disp(process_date, verba_disp, grpprd, ctg, subctg, divfrn, filepd=1, filfat=1):
    
    conn_string = 'postgres://postgres:Martins*2020@pricing-data-parsing.cq8kmgnsewpt.us-east-1.rds.amazonaws.com/pricing_analitica2'
    db = sqlalchemy.create_engine(conn_string)

    
    filt = {}
    filt['filepd'] = filepd
    filt['filfat'] = filfat
    filt['subctg'] = subctg
    filt['ctg'] = ctg
    filt['grpprd'] = grpprd
    filt['divfrn'] = divfrn
    filt['date'] = process_date

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

    query_base = '''
                 SELECT   *
                 FROM     "OUTPUT_OTM1"
                 WHERE    "CODFILEPD" = {filepd} AND
                          "CODFILFAT" = {filfat} AND
                          "CODGRPPRD" = {grpprd} AND
                          "CODCTGPRD" = {ctg} AND
                          "CODSUBCTGPRD" = {subctg} AND
                          "CODDIVFRN" = {divfrn}
                 '''.format(filepd=filt['filepd'],
                            filfat=filt['filfat'],
                            grpprd=filt['grpprd'],
                            ctg=filt['ctg'],
                            subctg=filt['subctg'],
                            divfrn=filt['divfrn'])

    base1 = pd.read_sql_query(query_base, db)

    nesc = fopt.create_opt_df(base1, week)

    base, nesc = opt.avail_fund(filt, base1, nesc, week,  verba_disp)
    
    base_tela = base[['CMVREAL',
    'CODCTGPRD',
    'CODDIVFRN',
    'CODESTUNI',
    'CODFILEPD',
    'CODFILFAT',
    'CODGRPPRD',
    'CODPRD',
    'CODSUBCTGPRD',
    'DATREF',
    'FUNDINGMEDREAL',
    'MONTH',
    'MRGBRTPEROTM',
    'MRGBRTPERPLN',
    'MRGBRTPERREAL',
    'QDEDIASMN',
    'VLRCMVPCOPLN',
    'VLRCOMPOTM',
    'VLRCOMPPLN',
    'VLRPCOOTM',
    'VLRPCOPLN',
    'VLRPCOREAL',
    'VLRVRBNSC',
    'VLRVRBPLN',
    'VLRVRBTOTNSC',
    'VOLVNDOTM',
    'VOLVNDPLN',
    'VOLVNDREAL',
    'YEAR',
    'WEEK'      
    ]]
    
    return base_tela