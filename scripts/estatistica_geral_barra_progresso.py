import pandas as pd
from openpyxl.styles import numbers


def calc_estatistica_geral_barra_progresso(ws_stats, df_tabela_info, end_estudios, end_tempo_visto, end_franquias, end_nota_media, barra_prog_porcentagem, barra_prog_meta):
    # Conta a quantidade de 'ESTUDIO' usando o nunique() que conta valores apenas uma vez (sem repetir)
    qtd_estudios = df_tabela_info['ESTUDIO'].nunique()
    ws_stats[end_estudios].value = qtd_estudios

    # Conta o tempo total de anime visto até o momento. 
    # Faz 'EPISODIO' multiplicado por 'DURACAO' (em minuto) para conseguir o total de Minutos
    # Depois soma todos os minutos de cada anime, divide por 60 (transforma em hora), divide por 24 (transforma em dia)
    tempo_visto = (df_tabela_info['EPISODIO'] * df_tabela_info['DURACAO']).sum() / 60.0 / 24.0
    ws_stats[end_tempo_visto].number_format = numbers.FORMAT_NUMBER_00
    ws_stats[end_tempo_visto].value =  float("{:.2f}".format(tempo_visto))

    # Conta a quantidade de 'FRANQUIA' usando o nunique() que conta valores apenas uma vez (sem repetir)
    # Remove as linhas que possuem '-' na coluna 'FRANQUIA' (ou seja, sem franquia)
    qtd_franquias = df_tabela_info[df_tabela_info['FRANQUIA'] != '-']['FRANQUIA'].nunique()
    ws_stats[end_franquias].value = qtd_franquias
    
    # Calcula a média das notas de todos animes
    nota_media = df_tabela_info['NOTA'].mean()
    ws_stats[end_nota_media].number_format = numbers.FORMAT_NUMBER_00
    ws_stats[end_nota_media].value =  float("{:.2f}".format(nota_media))


    # Retorna a quantidade total de 'ANIME' presente no Excel
    qtd_filmes = df_tabela_info['ANIME'].count()
    
    # Verifica se existe algum texto de Meta
    if(ws_stats[barra_prog_meta].value != None):
        index_dois_pontos = ws_stats[barra_prog_meta].value.find(':')
        # Verifica se existe ':' no texto de Meta
        if(index_dois_pontos != -1):
            # Retorna o valor da Meta pegando tudo após 2 caracteres de ':'
            meta_qtd_filmes =  int(ws_stats[barra_prog_meta].value[index_dois_pontos+2:])

            # Calcula a Porcentagem de Progresso
            prog_porcentagem = (qtd_filmes * 100) / meta_qtd_filmes
            # Imprime a Porcentagem de Progesso
            ws_stats[barra_prog_porcentagem].value = prog_porcentagem


            