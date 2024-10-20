import pandas as pd


def criar_df_mais_maior(df_tabela_info, coluna):
    # Cria dataframe agrupando por uma chave X (informada por 'coluna')
    df_mais_maior = df_tabela_info.groupby(coluna).agg(
        # Cria colunas cujos valores serao definidos pela função (count, mean) sobre uma coluna (ANIME, NOTA)
        Mais_Animes_por = ('ANIME', 'count'),
        Maior_Nota_Media_por = ('NOTA', 'mean')
    ).reset_index() # 'coluna' volta a ser uma coluna, deixando de ser INDEX


    # Vê se algum valor em df_mais_maior[coluna] é diferente de '-'
    # Caso seja diferente de '-', o retorno é TRUE e aquele valor em questão entrará para o novo "df_mais_maior"
    # Caso seka igual a '-', o retorno é FALSE e aquele valor em questão NÃO ENTRARÁ para o novo "df_mais_maior"
    df_mais_maior = df_mais_maior[df_mais_maior[coluna] != '-']


    return df_mais_maior


    