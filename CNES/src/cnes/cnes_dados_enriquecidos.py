import json
import requests
import pandas as pd 
import time

df = pd.read_csv("/home/cristina/Projetos/cnes-enriquecimento-dados/CNES/data/cnes_amostra.csv", encoding="latin1", low_memory=False,nrows=100)


def cep_api_viacep(dataframe):
    new_dataframe = pd.DataFrame()

    for row in dataframe.itertuples():

        try:
            response = requests.get(f'https://viacep.com.br/ws/{row.CO_CEP}/json/',timeout=5)
            response.raise_for_status()
            response_df = pd.json_normalize(response.json())
            new_dataframe = pd.concat([new_dataframe, response_df], ignore_index=True)

        except requests.exceptions.RequestException as e:
            print(f"Erro com o CEP {row.CO_CEP}: {e}")
            continue
    
    return new_dataframe



df_ceps = cep_api_viacep(df)

df_ceps["cep"] = df_ceps["cep"].str.replace("-", "")

df['CO_CEP'] = df['CO_CEP'].astype(str).str.zfill(8)

df_enriquecido = df.merge(df_ceps, left_on='CO_CEP', right_on='cep', how='left')

df_enriquecido = df_enriquecido.drop_duplicates(keep='first')

df_enriquecido.reset_index(drop=True, inplace=True)

df_enriquecido.drop(["Unnamed: 0","cep","ibge","gia","siafi","erro"], axis=1, inplace=True)

df_enriquecido = df_enriquecido.rename(columns={"logradouro": "LOGRADOURO_ATUALIZADO",
                               "unidade": "UNIDADE",
                               "complemento":"COMPLEMENTO",
                               "bairro": "BAIRRO_ATUALIZADO",
                               "localidade": "CIDADE",
                               "uf": "UF",
                               "estado": "ESTADO",
                               "regiao": "REGIAO",
                               "ddd": "DDD"})


colunas_api = ["LOGRADOURO_ATUALIZADO","UNIDADE","COMPLEMENTO","BAIRRO_ATUALIZADO","CIDADE","UF","ESTADO","REGIAO"]

for coluna_api in colunas_api:
    if coluna_api in df_enriquecido.columns:
        df_enriquecido[coluna_api] = df_enriquecido[coluna_api].str.upper()


df_enriquecido.to_csv("/home/cristina/Projetos/cnes-enriquecimento-dados/CNES/data/cnes_dados_enriquecidos.csv", index=False)


