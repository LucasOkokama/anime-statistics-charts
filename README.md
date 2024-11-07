# Sobre o projeto
Este simples projeto foi feito com o intuíto de estudar um pouco de manipulação de Dataframes com [Pandas](https://pandas.pydata.org/), arquivos Excel com [Openpyxl](https://openpyxl.readthedocs.io/), e criação de gráficos com [Plotly](https://plotly.com/).\
\
Os scripts têm como objetivo gerar gráficos html e tabelas no excel a respeito dos dados presentes na tabela, ajudando a análisar diversas informações a respeito dos animes registrados.


---


# Guias da Planilha
## Tabela
É o local onde deverá ser colocado as `informações dos animes assistidos`. Essa tabela possui as seguintes colunas:

| Nome da Coluna         | Significado                                                 | Valores / Exemplos                                        |                       
|:-----------------------|:------------------------------------------------------------|:----------------------------------------------------------|
| **FRANQUIAS**          | O nome comum pelo qual um anime poderá ser reconhecido.     | Dragon Ball                                               |
| **TIPO**               | O formato em que o anime foi transmitido.                   | Movie, ONA, OVA, Special, TV, TV Special                  |
| **NOTA**               | A sua nota para o anime (valor inteiro)                     | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10                             |         
| **ANIME**              | Nome do anime                                               | Code Geass: Hangyaku no Lelouch                           | 
| **ESTREIA**            | Temporada (season) em que o anime saiu                      | Fall, Spring, Summer, Winter                              |
| **ANO**                | Ano de estreia                                              | ... 2012, 2015, 2020, 2023...                             |        
| **EPISODIO**           | Quantidade de episódios                                     | ... 1, 12, 16, 23, 24, 48, 56 ...                         | 
| **DURACAO**            | Tempo médio de cada episódio **(valor inteiro em minutos)** | ... 12, 14, 22, 23, 24, 140 ...                           |
| **ESTUDIO**            | Nome do estúdio de animação                                 | Sunrise, MAPPA, Bones ...                                 |
| **DEMOGRAFIA**         | Tipo da demografia do anime                                 | Josei, Kodomo, Seinen, Shoujo, Shounen                    |
| **CLASS_IND**          | Classificação de idade                                      | PG-13, R-17, G, R-Plus (R+), PG                           |                
| **FONTE**              | Obra de origem do anime                                     | Manga, Light Novel, Original, Web manga, Visual novel ... |
| **GENERO_1 (2, 3, 4)** | Gênero (genre) do anime                                     | Action, Adventure, Drama, Comedy, Slice of Life ...       |
| **TEMA_1 (2, 3, 4)**   | Tema (theme) do anime                                       | School, Isekai, Iyashikei, Super power, Time travel,  ... |                                                      


## Stats
É o local onde as `tabelas e ranking de estatísticas` aparecerão após executar o Script. Eles serão gerados com textos simples nas próprias células do Excel.\
Aqui você **não deverá escrever nada**, pois diversas células possuem seus dados apagados para gerarem novas informações.

## DoNothing
Guia para fazer anotações. Não possui relação alguma com os scripts.


---


# Pré requisitos
## Python
Ter o python instalado. Veja [Python Download](https://www.python.org/downloads/) para as instruções de instalação.


## Instalar pacotes
Para saber mais sobre instalações de pacotes no python, acesse [Installing Python Modules](https://docs.python.org/3/installing/index.html)
1. Baixe o Pandas:
```
pip install pandas
```
2. Baixe o Plotly:
```
pip install plotly
```
3. Baixe o Openpyxl
```
pip install openpyxl
```


---
# Execução do Script

> [!WARNING]  
> Os seguintes comandos devem ser executados com o arquivo Excel **FECHADO**

Siga o passo a passo para gerar os gráficos no Excel e HTML.

1. Inicialize o CMD na `pasta raiz` do projeto (local onde está localizado o arquivo `animelist-stats.py`)
2. Digite o seguinte comando:
```
py animelist-stats.py
```
3. Acesse o arquivo Excel para visualizar as tabelas, ou abra os arquivos HTML (gerados no próprio root) para visualizar os gráficos.


---
# Variáveis dos scripts
No arquivo `animelist-stats.py` é possível alterar algumas configurações nos valores das variáveis.\
Note que essas configurações somente se aplicam ao que é retornado no próprio Excel, não há nenhuma interferência nos gráficos HTML.\
Abaixo do comentário `"# Variaveis Gerais"` existirão as seguintes variáveis:
1. `qtd_minimo_xxxx` (xxxx por significar classind, tipo, fonte, ano e etc...): Aqui você pode definir o número mínimo de animes que a categoria deve ter para aparecer nas tabelas do Excel.\
Por exemplo, se definir `qtd_minima_estudio = 5`, isso quer dizer que qualquer estúdio, para aparecer nas tabelas, deve ter ao menos 5 (cinco) animes registrados no Excel.

> [!WARNING]  
> Tome cuidado com os valores definidos abaixo, caso eles sejam altos demais, pode ser que eles sobrescrevam alguns dados!

2. `num_max_print_xxxx` (xxxx por significar classind, tipo, fonte, ano e etc...): Aqui você pode definir o número de linhas que uma tabela/ranking deve ter.\
Por exemplo, se definir `num_max_print_ano = 10`, isso quer dizer que a tabela/ranking terá no máximo 10 linhas, formando um "top 10".

<br><br><br><br><br>

---
# Imagens do Projeto
## Rankings/Tabelas no Excel
![Stats Gerais](/readme-images/stats_gerais.png)
![Stats Gerais de Demografia](/readme-images/stats_gerais_demografia.png)
![Stats Gerais de Estreia](/readme-images/stats_gerais_estreia.png)
![Ranking de Franquia](/readme-images/mais_maior_franquia.png)
![Ranking de Franquia](/readme-images/mais_maior_estudio.png)

## Gráficos HTML
![Grafico de Ano](/readme-images/grafico_ano.png)
![Grafico de Fonte](/readme-images/grafico_fonte.png)
![Grafico de Genero](/readme-images/grafico_genero.png)
![Grafico de Tema](/readme-images/grafico_tema.png)