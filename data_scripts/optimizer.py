import pandas as pd
import numpy as np
from . import functions_otimizador as fopt
from datetime import date, datetime
import sqlalchemy

pd.set_option('display.max_columns', 500)

conn_string = 'postgres://postgres:Martins*2020@pricing-data-parsing.cq8kmgnsewpt.us-east-1.rds.amazonaws.com/pricing_analitica2'
db = sqlalchemy.create_engine(conn_string)


def nesc_fund(filt):
    
    planejado = fopt.get_pln_results(filt)
    realizado, week = fopt.get_exec_results(filt, planejado)
    base = fopt.create_opt_base(planejado, realizado)
    base['DATREF'] = filt['date']
    for i in base.index:
        if base.loc[i, 'VLRPCOMRC'] != 0:
            base.loc[i, 'VLRCOMPREAL'] = base.loc[i, 'VLRPCOREAL']/base.loc[i, 'VLRPCOMRC']
        else:
            base.loc[i, 'VLRCOMPREAL'] = 0
    base = fopt.distribute_gap(base, week)
    nesc = fopt.create_opt_df(base, week)
    base, nesc_fund = fopt.calculate_nesc_funding(base, nesc, week)
    base = fopt.calculate_comp(base)
    
    return base, nesc, nesc_fund, week

def avail_fund(filt, base, nesc, week,  verba_disp):
    nesc = fopt.calculate_unt_fund(base, nesc, verba_disp, week)
    base = fopt.calculate_avail_fund_results(base, nesc, week)
    base = fopt.calculate_comp(base)
    
    return base, nesc
