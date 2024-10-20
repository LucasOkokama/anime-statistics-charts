import pandas as pd


'''
ws_stats                ---> Worksheet de Stats (referência a guia "Stats" do Excel)
df_tabela_info          ---> Dataframe da tabela de informações contida na guia "Tabela" do Excel
coluna                  ---> Coluna no Datagrame onde deverá ser feito o groupby (agrupar por ANO, DIRETOR, DISTRIBUIDORA e etc)
qtd_anime_minimo        ---> Quantidade minima de animes para entrar no Ranking
end_mais_animes         ---> Endereço (na guia Stats) para Mais Animes por XXXXX
end_maior_nota_media    ---> Endereço (na guia Stats) para Maior Nota Média por XXXXX
num_max_print           ---> Numero de linha que será impresso no Excel para compor o Ranking
xaxis_label_angulacao   ---> Angulação (inclinação) dos labels do Eixo X do gráfico gerado
'''

def calc_ranking_mais_maior(ws_stats, df_tabela_info, coluna, qtd_anime_minimo, end_mais_animes, end_maior_nota_media, num_max_print, xaxis_label_angulacao):

    from scripts import grafico_linha
    if df_tabela_info[coluna].sum() != 0:
        # Cria um gráfico com os valores 'Mais_Animes_por' e 'Maior_Nota_Media_por'
        grafico_linha.gerar_grafico_linha(df_tabela_info, coluna, xaxis_label_angulacao)
    

    # Remove todas as informações presentes nos Rankings (apagar dados), e para de apagar na primeira célula sem valor
    ranking_linha_atual = 0
    while(ws_stats[end_mais_animes].offset(row=ranking_linha_atual).value is not None):
        ws_stats[end_mais_animes].offset(row=ranking_linha_atual).value = None
        ws_stats[end_maior_nota_media].offset(row=ranking_linha_atual).value = None
        ranking_linha_atual+=1


    # Cria um novo dataframe organizado por "Mais_Animes_por" (quantidade de animes) em ordem decrescente
    df_mais = df_tabela_info.sort_values(by='Mais_Animes_por', ascending=False).reset_index(drop=True) # drop=True pega o atual index e descarta ele, criando um novo index
    # Cria um novo dataframe organizado por "Maior_Nota_Media_por" em ordem decrescente
    df_maior = df_tabela_info.sort_values(by='Maior_Nota_Media_por', ascending=False).reset_index(drop=True) # drop=True pega o atual index e descarta ele, criando um novo index


    rodar_mais_maior = 0
    rodar_mais_maior_interno = 0
    # Loop para imprimir X linhas do ranking na tela
    while rodar_mais_maior_interno < num_max_print and rodar_mais_maior < len(df_mais):
        # Verifica se a celula atual esta vazia
        if(ws_stats[end_mais_animes].offset(row=rodar_mais_maior_interno).value is None):
            # Define o numero minimo de animes para que o item apareça no Ranking
            if(df_mais['Mais_Animes_por'][rodar_mais_maior] >= qtd_anime_minimo):
                # Formata a String que será impressa no Excel
                string_mais_maior = "{}.  {} [{} Animes]   ~{} pts".format(
                    rodar_mais_maior_interno + 1,
                    df_mais[coluna][rodar_mais_maior],
                    df_mais['Mais_Animes_por'][rodar_mais_maior],
                    "{:.2f}".format(df_mais['Maior_Nota_Media_por'][rodar_mais_maior]).replace('.', ',')
                )

                # Imprime "Mais Animes por"
                ws_stats[end_mais_animes].offset(row=rodar_mais_maior_interno).value = string_mais_maior

                rodar_mais_maior_interno+=1

                
            else:
                # Quebra o Loop While que imprime o ranking
                break    
        else:
            # Quebra o Loop While que imprime o ranking
            break

        rodar_mais_maior+=1



    rodar_mais_maior = 0
    rodar_mais_maior_interno = 0
    # Loop para imprimir X linhas do ranking na tela
    while rodar_mais_maior_interno < num_max_print and rodar_mais_maior < len(df_maior):
        # Verifica se a celula atual esta vazia
        if(ws_stats[end_maior_nota_media].offset(row=rodar_mais_maior_interno).value is None):
            # Define o numero minimo de animes para que o item apareça no Ranking
            if(df_maior['Mais_Animes_por'][rodar_mais_maior] >= qtd_anime_minimo):
                # Formata a String que será impressa no Excel
                string_mais_maior = "{}.  {} [{} pts]   ~{} Animes".format(
                    rodar_mais_maior_interno + 1,
                    df_maior[coluna][rodar_mais_maior],
                    "{:.2f}".format(df_maior['Maior_Nota_Media_por'][rodar_mais_maior]).replace('.', ','),
                    df_maior['Mais_Animes_por'][rodar_mais_maior]
                )

                # Imprime "Maior Nota Média por"
                ws_stats[end_maior_nota_media].offset(row=rodar_mais_maior_interno).value = string_mais_maior

                rodar_mais_maior_interno+=1
        else:
            # Quebra o Loop While que imprime o ranking
            break

        rodar_mais_maior+=1


