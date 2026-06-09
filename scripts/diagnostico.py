from ast import And

import pandas as pd

df = pd.read_csv('dados\\TMDB_all_movies.csv')

print("--- 1. TAMANHO DO DATASET ---")
#Quantidade total de linhas e colunas
print('Tamanho de linhas:')
print(df.shape[0])
print('Tamanho de colunas:')
print(df.shape[1])
print("-" * 30)

print("\n--- 2. LINHAS EM BRANCO (NULAS) POR COLUNA ---")
# Mostra apenas as colunas que têm pelo menos um valor nulo
valores_nulos = df.isnull().sum()
print(valores_nulos)
print("-" * 30)

print("\n--- 3. FILMES COM VALORES ZERADOS (ERROS DE PREENCHIMENTO) ---")
# No cinema, orçamento ou receita = 0 geralmente significa "dado não coletado"
orcamento_zero = (df['budget'] == 0).sum()
receita_zero = (df['revenue'] == 0).sum()
sem_nome = ((df['title'] == "") | (df['title'].isnull())).sum()
print(f'Filmes com orçamento não coletado: {orcamento_zero}')
print(f'Filmes com receita não coletada: {receita_zero}')
print(f'Filme sem título: {sem_nome}')
print("-" * 30)

print("\n--- 4. TIPOS DE DADOS DAS COLUNAS CHAVE ---")
print(df[['release_date', 'budget', 'revenue', 'original_language']].dtypes)
print("-" * 30)


print('\n--- 5. LISTA DE COLUNAS DO DATASET ---')
print(list(df.columns))

print(df[['title','spoken_languages']].head(10))
print('---'*50)
print(df[['title','original_language']].head(10))





