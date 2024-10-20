import pandas as pd


def calc_qtd_notas(ws_stats, df_tabela_info, coluna, end_opcoes, end_qtd, end_porcentagem, end_barra, num_max_print):
    # Organiza o Dataframe ordem Decrescente utilizando como referencia a coluna 'coluna'
    df_tabela_info.sort_values(by=coluna, ascending=False, inplace=True)

    # Remove todas as informações presentes em 'Quantidade de Notas' (apagar dados), e para de apagar na primeira célula sem valor
    stats_gerais_animes_por = 0
    while(ws_stats[end_opcoes].offset(row=stats_gerais_animes_por).value is not None):
        ws_stats[end_opcoes].offset(row=stats_gerais_animes_por).value = None
        ws_stats[end_qtd].offset(row=stats_gerais_animes_por).value = None
        ws_stats[end_porcentagem].offset(row=stats_gerais_animes_por).value = None
        ws_stats[end_barra].offset(row=stats_gerais_animes_por).value = None

        stats_gerais_animes_por+=1


    # Puxa o total de animes
    qtd_filme = df_tabela_info['Mais_Animes_por'].sum()

    stats_gerais_animes_por = 0
    # O 'itertuples' ajuda a iterar sobre um dataframe
    for linha in df_tabela_info.itertuples(index=False, name='Pandas'):
        # Verifica se o numero de valores impressos (stats_gerais_animes_por) NÃO passou 'num_max_print'
        if(not(stats_gerais_animes_por > num_max_print)):
            # Verifica se o valor da célula atual for vazia (is None)
            if(ws_stats[end_opcoes].offset(row=stats_gerais_animes_por).value is None):
                ws_stats[end_opcoes].offset(row=stats_gerais_animes_por).value = getattr(linha, coluna)
                ws_stats[end_qtd].offset(row=stats_gerais_animes_por).value = linha.Mais_Animes_por

                # Calcula o valor da porcentagem e armezena em 'end_porcentagem' e 'end_barra'
                valor_porcentagem = (linha.Mais_Animes_por * 100.0) / qtd_filme / 100
                ws_stats[end_porcentagem].offset(row=stats_gerais_animes_por).value = valor_porcentagem
                ws_stats[end_barra].offset(row=stats_gerais_animes_por).value = valor_porcentagem

                # Adiciona +1 na variavel que conta o numero de valores impressos
                stats_gerais_animes_por+=1


