'''

    PARA PERMITIR QUE O SCRIPT FUNCIONE, EXECUTAR OS SEGUINTES COMANDOS NO CMD:
    pip install openpyxl
    pip install pandas

'''


from openpyxl import load_workbook
import pandas as pd
import time

from scripts import enderecos


# Salvando o tempo em que o script começou a ser executado
tempo_inicial_script = time.time()


print("\n\n\nIniciando execucao do Script!\n")
print("Carregando Workbook e Worksheets...")
# Carrega o Workbook MovieList.xlsx em um variável
wb_animelist = load_workbook(filename = 'AnimeList.xlsx')

# Carrega as guias (worksheets) em variáveis
ws_stats = wb_animelist["Stats"]

print("Criando dataframe com os dados...")
# Cria um dataframe a partir da tabela presente na guia "Tabela" e salva em uma variável
df_tabela_info = pd.read_excel('AnimeList.xlsx', 'Tabela', skiprows = 4, usecols = 'C:V')
# Limpa as linhas vazias do "df_tabela_info"
df_tabela_info = df_tabela_info.dropna(how='all')



import sys


# Variaveis Gerais
## Quantidade minima de filme para aparecer no 'Stats Gerais' e no Ranking
### Painel Central
qtd_minima_classind = 1
qtd_minima_tipo = 1
qtd_minima_fonte = 1
qtd_minima_estreia = 1

qtd_minima_demografia = 1
qtd_minima_genero = 1

qtd_minina_tema = 7


### Painel Direito
qtd_minima_ano = 7
qtd_minima_franquia = 2
qtd_minima_estreiaano = 4
qtd_minima_estudio = 5



# Quantidade máxima de impressões na tela
## Painel Esquerdo
num_max_print_nota = 10

## Painel Central
num_max_print_classind = 5
num_max_print_tipo = 6
num_max_print_fonte = 9
num_max_print_estreia = 4 

num_max_print_demografia = 5
num_max_print_genero = 20

num_max_print_tema = 50


## Painel Direito
num_max_print_ano = 10
num_max_print_franquia = 10 
num_max_print_estreiaano = 10
num_max_print_estudio = 10


'''
Preenche os valores em:
    Barra de Progresso
        Calcula a porcentagem e imprime na barra

    Estatisticas Gerais
        Estudios    Tempo Visto (dias)      Franquias
                    Nota Média
'''
print("Imprimindo valores de Estatistica Geral...")
print("Calculado a Barra de Progesso...")
from scripts import estatistica_geral_barra_progresso
estatistica_geral_barra_progresso.calc_estatistica_geral_barra_progresso(ws_stats, df_tabela_info, enderecos.end_estudios, enderecos.end_tempo_visto, enderecos.end_franquias, enderecos.end_nota_media, enderecos.barra_prog_porcentagem, enderecos.barra_prog_meta)





'''
Junta X colunas em apenas um Dataframe 
    O Dataframe retornado possui:
        Chave (valor informado nos parametros em 'novo_nome_coluna_uniao')
        NOTA
        ANIME    
'''
print("Juntado colunas para efetuar calculos...")
from scripts import x_cols_para_uma
df_genero = x_cols_para_uma.transformar_x_cols_para_uma(df_tabela_info, "GENERO_1", 4, "GENERO")
df_tema = x_cols_para_uma.transformar_x_cols_para_uma(df_tabela_info, "TEMA_1", 4, "TEMA")





'''
Junta X colunas em apenas um Dataframe 
    O Dataframe retornado possui:
        Chave (valor informado nos parametros em 'novo_nome_coluna_uniao')
        NOTA
        ANIME    
'''
from scripts import base_df_estreia_ano
df_estreiaano = base_df_estreia_ano.criar_base_df_estreia_ano(df_tabela_info)





'''
    Cria um Dataframe com uma coluna Chave (tipo CLASS_IND, TIPO, FONTE etc), Mais_Animes_por, Maior_Nota_Media_por
    São os valores desse dataframe que será impresso nos rankings
'''
from scripts import df_mais_maior
print("Criando df_mais_maior de todos os itens...")
# Painel Esquerdo
df_notas = df_mais_maior.criar_df_mais_maior(df_tabela_info, 'NOTA')



# Painel Central
df_classind = df_mais_maior.criar_df_mais_maior(df_tabela_info, 'CLASS_IND')
df_tipo = df_mais_maior.criar_df_mais_maior(df_tabela_info, 'TIPO')
df_fonte = df_mais_maior.criar_df_mais_maior(df_tabela_info, 'FONTE')
df_estreia = df_mais_maior.criar_df_mais_maior(df_tabela_info, 'ESTREIA')

df_demografia = df_mais_maior.criar_df_mais_maior(df_tabela_info, 'DEMOGRAFIA')
df_genero = df_mais_maior.criar_df_mais_maior(df_genero, 'GENERO')

df_tema = df_mais_maior.criar_df_mais_maior(df_tema, 'TEMA')



# Painel Direito
df_ano = df_mais_maior.criar_df_mais_maior(df_tabela_info, 'ANO')
df_franquia = df_mais_maior.criar_df_mais_maior(df_tabela_info, 'FRANQUIA')
df_estreiaano = df_mais_maior.criar_df_mais_maior(df_estreiaano, 'ESTREIA_ANO')
df_estudio = df_mais_maior.criar_df_mais_maior(df_tabela_info, 'ESTUDIO')





'''
Preenche os valores em:
    Quantidade de Notas
        Notas    Qtd.    Porcent.
'''
from scripts import qtd_notas
print("Imprimindo valores de 'Quantidade de Notas'...")
qtd_notas.calc_qtd_notas(ws_stats, df_notas, "NOTA", enderecos.end_notas, enderecos.end_nota_qtd, enderecos.end_nota_porcentagem, enderecos.end_nota_barra, num_max_print_nota)





'''
Preenche os valores em:
    Mais Animes por XXXXX
        Imprime ranking

    Maior Nota Média por XXXXX
        Imprime ranking
'''
from scripts import ranking_mais_maior
print("Gerando rankings de todos os itens...")
# Painel Central
ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_classind, "CLASS_IND", qtd_minima_classind, enderecos.end_mais_filme_classind, enderecos.end_maior_nota_media_classind, num_max_print_classind, 0)
ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_tipo, "TIPO", qtd_minima_tipo, enderecos.end_mais_filme_tipo, enderecos.end_maior_nota_media_tipo, num_max_print_tipo, 0)
ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_fonte, "FONTE", qtd_minima_fonte, enderecos.end_mais_filme_fonte, enderecos.end_maior_nota_media_fonte, num_max_print_fonte, 0)
ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_estreia, "ESTREIA", qtd_minima_estreia, enderecos.end_mais_filme_estreia, enderecos.end_maior_nota_media_estreia, num_max_print_estreia, 0)

ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_demografia, "DEMOGRAFIA", qtd_minima_demografia, enderecos.end_mais_filme__demografia, enderecos.end_maior_nota_media__demografia, num_max_print_demografia, 0)
ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_genero, "GENERO", qtd_minima_genero, enderecos.end_mais_filme_genero, enderecos.end_maior_nota_media_genero, num_max_print_genero, -20)

ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_tema, "TEMA", qtd_minina_tema, enderecos.end_mais_filme_tema, enderecos.end_maior_nota_media_tema, num_max_print_tema, -25)


# Painel Direito
ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_ano, "ANO", qtd_minima_ano, enderecos.end_mais_filme_ano, enderecos.end_maior_nota_media_ano, num_max_print_ano, 0)
ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_franquia, "FRANQUIA", qtd_minima_franquia, enderecos.end_mais_filme_franquia, enderecos.end_maior_nota_media_franquia, num_max_print_franquia, -25)
ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_estreiaano, "ESTREIA_ANO", qtd_minima_estreiaano, enderecos.end_mais_filme_estreiaano, enderecos.end_maior_nota_estreiaano, num_max_print_estreiaano, -25)
ranking_mais_maior.calc_ranking_mais_maior(ws_stats, df_estudio, "ESTUDIO", qtd_minima_estudio, enderecos.end_mais_filme_estudio, enderecos.end_maior_nota_media_estudio, num_max_print_estudio, -25)





'''
Preenche os valores em:
    Stats Gerais de Filmes por XXXXX
        <Tipo>     Avg     Qtd.     Porcent.
'''
from scripts import stats_gerais_filme_por
print("Imprimindo valores de 'Stats Gerais de Filmes por' de todos os itens...")
print("Gerando graficos interativos...")
# Painel Central
stats_gerais_filme_por.calc_stats_gerais_filme_por(ws_stats, df_classind, "CLASS_IND", qtd_minima_classind, enderecos.end_classinds, enderecos.end_classind_nota_media, enderecos.end_classind_qtd, enderecos.end_classind_porcentagem, enderecos.end_classind_barra, num_max_print_classind)
stats_gerais_filme_por.calc_stats_gerais_filme_por(ws_stats, df_tipo, "TIPO", qtd_minima_tipo, enderecos.end_tipos, enderecos.end_tipo_nota_media, enderecos.end_tipo_qtd, enderecos.end_tipo_porcentagem, enderecos.end_tipo_barra, num_max_print_tipo)
stats_gerais_filme_por.calc_stats_gerais_filme_por(ws_stats, df_fonte, "FONTE", qtd_minima_fonte, enderecos.end_fontes, enderecos.end_fonte_nota_media, enderecos.end_fonte_qtd, enderecos.end_fonte_porcentagem , enderecos.end_fonte_barra, num_max_print_fonte)
stats_gerais_filme_por.calc_stats_gerais_filme_por(ws_stats, df_estreia, "ESTREIA", qtd_minima_estreia, enderecos.end_estreias, enderecos.end_estreia_nota_media, enderecos.end_estreia_qtd, enderecos.end_estreia_porcentagem , enderecos.end_estreia_barra, num_max_print_estreia)

stats_gerais_filme_por.calc_stats_gerais_filme_por(ws_stats, df_demografia, "DEMOGRAFIA", qtd_minima_demografia, enderecos.end_demografias, enderecos.end_demografia_nota_media, enderecos.end_demografia_qtd, enderecos.end_demografia_porcentagem , enderecos.end_demografia_barra, num_max_print_demografia)
stats_gerais_filme_por.calc_stats_gerais_filme_por(ws_stats, df_genero, "GENERO", qtd_minima_genero, enderecos.end_generos, enderecos.end_genero_nota_media, enderecos.end_genero_qtd, enderecos.end_genero_porcentagem , enderecos.end_genero_barra, num_max_print_genero)

stats_gerais_filme_por.calc_stats_gerais_filme_por(ws_stats, df_tema, "TEMA", qtd_minina_tema, enderecos.end_temas, enderecos.end_tema_nota_media, enderecos.end_tema_qtd, enderecos.end_tema_porcentagem , enderecos.end_tema_barra, num_max_print_tema)










# Salva as alterações efetudas no workbook
print("Salvando as alteracoes feitas no Excel...")
wb_animelist.save('AnimeList.xlsx')



# Salvando o tempo em que o script terminou de ser executado
tempo_final_script = time.time()

# Calculando tempo...
tempo_execucao_script = "{:.4f}".format(tempo_final_script - tempo_inicial_script)

# Imprime tempo de execução na tela
print(f"\n\nTempo de Execucao: {tempo_execucao_script} segundos\n\n\n\n\n")