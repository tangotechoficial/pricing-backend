import pandas as pd
from . import plano_compras_final
from . import functions_planocompras_final as fpc
import sqlite3
import sqlalchemy
import boto3
import io
import warnings
warnings.filterwarnings('ignore')

def run_sugerido(plan_month, plan_year, filepd=1, filfat=1, estados=['MG','SC','PA']):
    # Credenciais S3
    s3 = boto3.client('s3',
                  aws_access_key_id=r'AKIA2R5N7LHAEGZAMILX',
                  aws_secret_access_key=r'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')
    
    # Carregando listsa de produtos do MVP
    read_file = s3.get_object(Bucket='martins11tt', Key='bases/prds_mvp.csv')
    prds = pd.read_csv(io.BytesIO(read_file['Body'].read()),sep=';', encoding='latin1')
    
    # Conectando banco postgres
    conn_string = 'postgres://postgres:Martins*2020@pricing-data-parsing.cq8kmgnsewpt.us-east-1.rds.amazonaws.com/pricing_analitica2'
    db = sqlalchemy.create_engine(conn_string)
    
    # Criando lista para salvar os códigos dos produtos que derem problema:
    problems = []
    
    
    for prd in [prds['CODMER'].unique()[0]]:
        for est in ['MG','SC','PA']:

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

            for key in result.keys():
                result[key] = [str(x) for x in result[key]]

            try:
                sugerido_tela, sugerido_base, sugerido = plano_compras_final.sugerido(result)


                user_input = {}

                user_input['VERBA_WEEK1'] = sugerido.loc[0, 'VRBUNTSUGSUG'] - 0.5*sugerido.loc[0, 'VRBUNTSUGSUG']
                user_input['VERBA_WEEK2'] = sugerido.loc[1, 'VRBUNTSUGSUG'] - 0.5*sugerido.loc[1, 'VRBUNTSUGSUG']
                user_input['VERBA_WEEK3'] = sugerido.loc[2, 'VRBUNTSUGSUG'] - 0.5*sugerido.loc[2, 'VRBUNTSUGSUG']
                user_input['VERBA_WEEK4'] = sugerido.loc[3, 'VRBUNTSUGSUG'] - 0.5*sugerido.loc[3, 'VRBUNTSUGSUG']
                user_input['VERBA_WEEK5'] = sugerido.loc[4, 'VRBUNTSUGSUG'] - 0.5*sugerido.loc[4, 'VRBUNTSUGSUG']

                user_input['CMVCMP_WEEK1'] = sugerido.loc[0, 'VLRCMVPCOSUG'] + 0.05*sugerido.loc[0, 'VLRCMVPCOSUG']
                user_input['CMVCMP_WEEK2'] = sugerido.loc[1, 'VLRCMVPCOSUG'] + 0.05*sugerido.loc[1, 'VLRCMVPCOSUG']
                user_input['CMVCMP_WEEK3'] = sugerido.loc[2, 'VLRCMVPCOSUG'] + 0.05*sugerido.loc[2, 'VLRCMVPCOSUG']
                user_input['CMVCMP_WEEK4'] = sugerido.loc[3, 'VLRCMVPCOSUG'] + 0.05*sugerido.loc[3, 'VLRCMVPCOSUG']
                user_input['CMVCMP_WEEK5'] = sugerido.loc[4, 'VLRCMVPCOSUG'] + 0.05*sugerido.loc[4, 'VLRCMVPCOSUG']

                planejado_base, planejado= plano_compras_final.planejado(user_input, sugerido)
                
                print('Gravando dados no banco.')
                planejado_base.to_sql(name='MOVPLNCMPCAL', con=db, index=False, if_exists='append')
                planejado.to_sql(name='OUTPUT_PLN', con=db, index=False, if_exists='append')


            except:
                print(prd)
                problems.append(prd)


    pd.DataFrame(problems).to_csv('problems.csv', index=False)