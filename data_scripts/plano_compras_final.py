import pandas as pd
import numpy as np
import sqlite3
from . import functions_planocompras_final as fpc
import sqlalchemy

conn_string = 'postgres://postgres:Martins*2020@pricing-data-parsing.cq8kmgnsewpt.us-east-1.rds.amazonaws.com/pricing_analitica2'
db = sqlalchemy.create_engine(conn_string)


def sugerido(result, last_n_weeks=15, trava_pco_min=0.1, trava_pco_max=0.1):
        
    prd = result['CODPRD']
    filepd = result['CODFILEPD']
    filfat = result['CODFILFAT']
    est = result['CODESTUNI']
    subctg = result['CODSUBCTGPRD']
    ctg = result['CODCTGPRD']
    grpprd = result['CODGRPPRD']
    divfrn = result['CODDIVFRN']
    month = result['MONTH']
    year = result['YEAR']

    final = pd.DataFrame(result)
    final
    
    
    final = fpc.get_weekly_goals_subctg(final, month, year, divfrn, filepd, 
                                              est, grpprd, ctg, subctg)
    
    final = fpc.add_prd_hst_rpr(final, grpprd, ctg, subctg, prd, est, month, year, filepd, filfat, divfrn) # <- demorada
    
    final = fpc.calculate_suggested_volume_of_sales(final)

    final = fpc.get_hst_rpr_desc(final, prd, filepd, filfat, month, year, est) # <- demorada
    
    final = fpc.get_hst_rpr_acr(final, prd, filepd, filfat, month, year, est) # <- demorada
    
    final = fpc.get_els_params(final, prd, filepd, filfat, est)
    
    try:
        final = fpc.get_mean_price_quantity(final, prd, filepd, filfat, est, month, year, last_n_weeks=last_n_weeks)# <- demorada
    except:
        final = fpc.get_mean_price_quantity(final, prd, filepd, filfat, est, month, year, last_n_weeks=52)
             
    final = fpc.calculate_sug_price_opt(final, trava_pco_min, trava_pco_max)

    # final = fpc.fix_sug_prc(final)
    
    final = fpc.calculate_suggested_quantity(final)
    
    final = fpc.calculate_base_price(final)

    final = fpc.price_decomposition(final, prd, est, filepd, filfat)

    final = fpc.cmv_etq(final, prd, filepd, divfrn)

    final = fpc.get_current_etq_prc_cmv(final, prd, filepd, filfat)

    final = fpc.compare_sug_atu(final)

    final = fpc.suggested_funding_sug(final)

    final = fpc.calculate_sug_competitivity(final,
                                            prd,
                                            divfrn,
                                            est,
                                            month,
                                            year)

    final = fpc.calculate_accomplished_volume_of_sales(final)


    final['VLRIMPTOTSUG'] = final['VLRICMSSUG'] + final['VLRPISCOFSUG']
    final['VLRVRBPLAN'] = '-'

    final_tela = fpc.calculate_month_results_sug(final)

    final_base = final_tela[['CODPRD', 'CODFILEPD', 'CODFILFAT', 'CODESTUNI', 'MONTH', 'YEAR',
                             'WEEK', 'VOLVNDSUG', 'VOLVNDSUGALC', 'MRGBRTPEROCD', 'VLRPCOSUG', 'VLRPCOBASESUG',
                             'VLRIMPTOTSUG', 'VLRICMSSUG', 'VLRPISCOFSUG', 'VLRDEVSUG', 'VLRFLXSUG','VLRMRGBRTSUG',
                             'VRBUNTSUGSUG', 'VLRVRBPLAN', 'VLRCMVPCOSUG', 'VLRCMVPCOATU', 'VLRCMVCMPATU']]
    
    final_tela = final_tela[['WEEK', 'VOLVNDSUG', 'VOLVNDSUGALC', 'MRGBRTPEROCD', 'VLRPCOSUG', 'VLRPCOBASESUG',
                             'VLRIMPTOTSUG', 'VLRICMSSUG', 'VLRPISCOFSUG', 'VLRDEVSUG', 'VLRFLXSUG',
                             'VLRMRGBRTSUG', 'VRBUNTSUGSUG', 'VLRVRBPLAN', 'VLRCMVPCOSUG', 'VLRCMVPCOATU', 'VLRCMVCMPATU']]
    
    return final_tela, final_base, final

def planejado(user_input, final):

    planejado = final.copy()
    # Escrevendo input do usuário no DataFrame
    for i in range(planejado.shape[0]):
        planejado.loc[i, 'VLRCMVCMPPLN'] = user_input['CMVCMP_WEEK'+str(i+1)]
        planejado.loc[i, 'VLRBONPLN'] = planejado.loc[i, 'Bonificado']
        planejado.loc[i, 'VLRVRBPLN'] = user_input['VERBA_WEEK'+str(i+1)]
        planejado.loc[i, 'VLRVBAPCOPLN'] = planejado.loc[i, 'VerbaPco']
        planejado.loc[i, 'MRGBRTPERPLN'] = planejado.loc[i, 'MRGBRTPEROCD']

    planejado = fpc.etqcmv_to_prccmv(planejado)

    planejado = fpc.suggested_funding_pln(planejado)

    planejado = fpc.base_price_composition(planejado)

    planejado = fpc.base_price_to_sales_price(planejado)

    planejado = fpc.sales_volume_from_price(planejado)

    planejado = fpc.compare_pln_sug(planejado)

    planejado = fpc.pln_qtt(planejado)

    planejado = fpc.calculate_pln_competitivity(planejado)

    planejado['VLRIMPTOTPLN'] = planejado['VLRICMSPLN'] + planejado['VLRPISCOFPLN']

    planejado_base = fpc.calculate_month_results_pln(planejado)

    planejado_base =  planejado_base[['CODPRD',
                                    'CODFILEPD',
                                    'CODFILFAT',
                                    'CODESTUNI',
                                    'MONTH',
                                    'YEAR',
                                    'WEEK',
                                    'VOLVNDSUG',
                                    'VOLVNDSUGALC',
                                    'MRGBRTPEROCD',
                                    'VLRPCOSUG',
                                    'VLRPCOBASESUG',
                                    'VLRIMPTOTSUG',
                                    'VLRICMSSUG',
                                    'VLRPISCOFSUG',
                                    'VLRDEVSUG',
                                    'VLRFLXSUG',
                                    'VLRMRGBRTSUG',
                                    'VRBUNTSUGSUG',
                                    'VLRVRBPLAN',
                                    'VLRCMVPCOSUG',
                                    'VLRCMVPCOATU',
                                    'VLRCMVCMPATU',
                                    'VLRPCOMRC',
                                    'VLRCOMPSUG',
                                    'VOLVNDPLN',
                                    'VLRPCOPLN',
                                    'VLRPCOBASEPLN',
                                    'VLRIMPTOTPLN',
                                    'VLRICMSPLN',
                                    'VLRPISCOFPLN',
                                    'VLRDEVPLN',
                                    'VLRFLXPLN',
                                    'VLRMRGBRTPLN',
                                    'VRBUNTSUGPLN',
                                    'VLRVRBPLN',
                                    'VLRCMVPCOPLN',
                                    'VLRCMVCMPPLN',
                                     'VLRCOMPPLN']]


    
    return planejado_base, planejado


def teste_pln_cmp(result):

    prd = result['CODPRD']
    filepd = result['CODFILEPD']
    filfat = result['CODFILFAT']
    est = result['CODESTUNI']
    subctg = result['CODSUBCTGPRD']
    ctg = result['CODCTGPRD']
    grpprd = result['CODGRPPRD']
    divfrn = result['CODDIVFRN']
    month = result['MONTH']
    year = result['YEAR']

    final = pd.DataFrame(result)

    final = fpc.get_weekly_goals_subctg(final, ['01'], ['2020'], divfrn, filepd, 
                                              est, grpprd, ctg, subctg)

    final = fpc.get_executed_values(final, prd, filepd,
                                    filfat, est, month, year)

    final = fpc.mrg_vol_as_executed(final)

    final = fpc.get_hst_rpr_desc(final, prd, filepd,
                                 filfat, ['01'], ['2020'], est)
    
    final = fpc.get_hst_rpr_acr(final, prd, filepd,
                                filfat, ['01'], ['2020'], est)

    final = fpc.get_els_params(final, prd, filepd, filfat, est)

    final = fpc.get_mean_price_quantity(final, prd, filepd, filfat, est, last_n_weeks=15)

    final = fpc.calculate_suggested_price(final)

    final = fpc.fix_sug_prc(final)

    final = fpc.calculate_suggested_quantity(final)

    final = fpc.calculate_base_price(final)

    final = fpc.get_executed_base_price(final, prd, filepd, filfat, est)

    final = fpc.price_decomposition(final, prd, est, filepd, filfat)

    final = fpc.calculate_sug_competitivity(final, prd, divfrn, est, month, year)

    final = fpc.cmv_etq(final, prd, filepd, divfrn)

    final = fpc.get_current_etq_prc_cmv(final, prd, filepd, filfat)

    final = fpc.suggested_funding_sug(final)

    final = fpc.calculate_accomplished_volume_of_sales(final)

    #Planejado:
    final = fpc.userinput_as_executed(final)

    final = fpc.etqcmv_to_prccmv(final)

    final = fpc.suggested_funding_pln(final)

    final = fpc.base_price_composition(final)

    final = fpc.base_price_to_sales_price(final)

    final = fpc.sales_volume_from_price(final)

    final = fpc.pln_qtt(final)

    final = fpc.calculate_pln_competitivity(final)

    err_pcovnd, err_qtd, err_pcobase, err_cmv = fpc.present_error(final)

    return final, err_pcovnd, err_qtd, err_pcobase, err_cmv

