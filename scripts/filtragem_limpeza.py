import pandas as pd
from tabulate import tabulate

caminho_csv = 'dados\\TMDB_all_movies.csv'
#As colunas mais necessárias para a análise são as de título, status, lançamento, orçamento, receita, gênero, elenco e data de lançamento.
#Assim, é necessário filtrar e limpar a tabela nessas colunas

#Leitura do arquivo
df = pd.read_csv(caminho_csv)

#Filtragem da coluna de lançamento
#Para filtrar: df = df[condicao]
df = df[df['status'] == 'Released']

#Filtragem de orçamento e receita
df = df[(df['budget'] > 0) & (df['revenue'] > 0)]

#Remove linhas onde gênero, elenco e data de lançamento estão vazias
df = df.dropna(subset=['title','genres','cast','release_date'])

#Converte a data de lançamento em datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

#Colunas de lucro e ano de lançamento
df['lucro'] = df['revenue'] - df['budget']
df['ano_lancamento'] = df['release_date'].dt.year

#Decidi rotular os filmes de acordo com 'eras', baseados no seu ano de lançamento. 
#Vai ajudar a catalogar e separar melhor a linha temporal

def rotular_era(ano):
    if ano < 2015:
        return '1. Pré-streamings (antes de 2015)'
    elif 2015 <= ano <= 2019:
        return '2. Ascensão dos streamings (2015-2019)'
    elif 2020 <= ano <= 2021:
        return '3. Pandemia e boom dos streamings (2020-2021)'
    elif ano >= 2022:
        return '4. Consolidação do mercado híbrido (2022-atualmente)'
    else:
        return 'Ignorar'
    
df['era_cinema'] = df['ano_lancamento'].apply(rotular_era)

#Teste da tabela limpa e filtrada
tabela_filtrada = df
colunas_principais = ['title', 'ano_lancamento', 'budget', 'revenue', 'lucro', 'era_cinema']

# --- RESOLUÇÃO DOS NÚMEROS ESQUISITOS ---
# Criamos uma cópia apenas para o print e convertemos os valores para inteiros normais (int64)
amostra_formatada = tabela_filtrada[colunas_principais].head(20).copy()
amostra_formatada['budget'] = amostra_formatada['budget'].astype('int64')
amostra_formatada['revenue'] = amostra_formatada['revenue'].astype('int64')
amostra_formatada['lucro'] = amostra_formatada['lucro'].astype('int64')

print(tabulate(amostra_formatada, headers='keys', tablefmt='fancy_grid', showindex=False))