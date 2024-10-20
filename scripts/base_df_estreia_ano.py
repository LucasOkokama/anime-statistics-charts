import pandas as pd


def criar_base_df_estreia_ano(df_tabela_info):
    if df_tabela_info['ANIME'].sum() != 0:
        # Cria uma nova coluna chamada 'ESTREIA/ANO' formada pelo valor contido em 'ESTREIA', uma barra (/) e pelo valor contido em 'ANO'
        # Transforma o conjunto resultante em uma string
        df_tabela_info['ESTREIA_ANO'] =  df_tabela_info['ESTREIA'] + '/' + df_tabela_info['ANO'].astype(int).astype(str)

    else:
        # Cria coluna ESTREIA_ANO sem valores
        df_tabela_info['ESTREIA_ANO'] = ''

    return df_tabela_info


    