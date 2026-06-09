#Perguntas

from tkinter import ALL

import pandas as pd
import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('database.db')

# O que aconteceu com os filmes de orçamento médio?

query_mid_budget = """
    SELECT
        era_cinema,
        COUNT(*) AS Total_filmes,
        AVG(revenue) AS Bilheteria_Media,
        AVG(budget) AS Orcamento_medio,
        AVG(lucro) AS Lucro_medio
    FROM tabela_filmes
    WHERE 
        era_cinema IN  ('4. Consolidação do mercado híbrido (2022-atualmente)', '2. Ascensão dos streamings (2015-2019)')
    AND
        budget BETWEEN 15000000 AND 100000000
    GROUP BY era_cinema
"""

df_mid_budget = pd.read_sql_query(query_mid_budget, conn)
conn.close()
print(df_mid_budget)
print(df_mid_budget.dtypes)


# Quais os gêneros com mais chances de darem lucro?

# query_agrupamento = """
#     SELECT 'Animação' AS Genero, COUNT(*) AS Total_Filmes, AVG(revenue) AS Bilheteria_Media, AVG(lucro) AS Lucro_Medio FROM tabela_filmes WHERE genres LIKE '%Animation%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Aventura', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Adventure%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Sci-Fi', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Science Fiction%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Família', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Family%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Fantasia', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Fantasy%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Ação', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Action%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Comédia', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Comedy%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Thriller', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Thriller%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Romance', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Romance%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Crime', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Crime%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Terror', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Horror%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
#     UNION ALL
#     SELECT 'Drama', COUNT(*), AVG(revenue), AVG(lucro) FROM tabela_filmes WHERE genres LIKE '%Drama%' AND era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)' 
    
#     ORDER BY Lucro_Medio DESC;
# """

# df_query_agrupamento = pd.read_sql_query(query_agrupamento, conn)
# conn.close()

# # --- FORMATAÇÃO DOS NÚMEROS NO PANDAS (À PROVA DE ERROS) ---
# # 1. Substitui qualquer valor nulo (NaN) por 0 antes de converter
# df_query_agrupamento['Total_Filmes'] = df_query_agrupamento['Total_Filmes'].fillna(0).astype(int)
# df_query_agrupamento['Bilheteria_Media'] = df_query_agrupamento['Bilheteria_Media'].fillna(0).astype(int)
# df_query_agrupamento['Lucro_Medio'] = df_query_agrupamento['Lucro_Medio'].fillna(0).astype(int)

# df_query_agrupamento['Total_Filmes'] = df_query_agrupamento['Total_Filmes'].astype(int).map('{:,}'.format)
# df_query_agrupamento['Bilheteria_Media'] = df_query_agrupamento['Bilheteria_Media'].astype(int).map('${:,}'.format)
# df_query_agrupamento['Lucro_Medio'] = df_query_agrupamento['Lucro_Medio'].astype(int).map('${:,}'.format)

# print("\n--- 📊 GÊNEROS MAIS LUCRATIVOS NO PÓS-PANDEMIA (2022+) ---")
# df_tabela = df_query_agrupamento
# print(tabulate(df_tabela, headers='keys', tablefmt='fancy_grid', showindex=False))
# df_tabela.to_excel('tabela_cinema.xlsx', index=False, sheet_name='Lucro por Gênero')
# print("Arquivo 'dados_cinema.xlsx' criado com sucesso! Agora é só abrir no Excel.")


#--- ROI DO GÊNERO TERROR ---
# A query SQL procura buscar os filmes de terror pós-pandemia 
# com orçamento maior que 10.000 USD que obtiveram maior ROI (retorno sobre o investimento)
# e compara-os com os gêneros de maior lucro


# query_terror = """
#     SELECT title, budget, revenue, lucro, (CAST(lucro AS FLOAT) / budget) AS ROI,
#     CASE 
#     WHEN genres LIKE '%Horror%' THEN 'Terror'
#     WHEN genres LIKE '%Animation%' THEN 'Animação'
#     WHEN genres LIKE '%Adventure%' THEN 'Aventura'
#     WHEN genres LIKE '%Science Fiction%' THEN 'Sci-Fi'
#     END AS genero_agrupado
#     FROM tabela_filmes 
#     WHERE era_cinema = '4. Consolidação do mercado híbrido (2022-atualmente)'
#     AND budget >= 10000
#     AND genero_agrupado IS NOT NULL
#     ORDER BY ROI DESC
# """

# df_query_terror = pd.read_sql_query(query_terror, conn)

# # --- PASSO DE LIMPEZA: Corrigindo a bilheteria errada do Memoir of a Snail ---
# # Localizamos a linha onde o título é 'Memoir of a Snail' e corrigimos o revenue para 7 milhões
# df_query_terror.loc[df_query_terror['title'] == 'Memoir of a Snail', 'revenue'] = 7_000_000

# # Depois de corrigir a bilheteria, precisamos recalcular o Lucro e o ROI daquela linha específica
# df_query_terror['lucro'] = df_query_terror['revenue'] - df_query_terror['budget']
# df_query_terror['ROI'] = df_query_terror['lucro'] / df_query_terror['budget']

# conn.close()
# print(df_query_terror)

# O quanto a pandemia e a janela de lançamento nos streamings afetou a bilheteria dos filmes pós-pandemia?

# query_streamings = """
#     SELECT 
#         era_cinema,
#         COUNT(title) AS total_filmes,
#         AVG(budget) AS media_orcamento,
#         AVG(revenue) AS media_bilheteria,
#         AVG(lucro) AS media_lucro
#     FROM tabela_filmes
#     WHERE budget >= 10000
#     GROUP BY era_cinema
#     ORDER BY era_cinema
# """

# df_streaming = pd.read_sql_query(query_streamings, conn)
# conn.close()
# print(df_streaming)
# print(df_streaming.dtypes)
# df_streaming.to_excel('tabela_streaming.xlsx', index=False, sheet_name='Média das eras do cinema', )


# Filmes em língua não-inglesa estão quebrando barreiras de lucro? 


# query_estrangeiro = """
#     SELECT
#         title,
#         ano_lancamento,
#         revenue,
#         budget,
#         lucro,
#         (CAST(lucro AS FLOAT) / budget) AS ROI,
#         era_cinema
#     FROM tabela_filmes
#     WHERE original_language != 'en'
#     AND budget >= 10000
#     AND era_cinema IN 
#         ('4. Consolidação do mercado híbrido (2022-atualmente)',
#         '2. Ascensão dos streamings (2015-2019)')
#     ORDER BY lucro DESC
# """

# df_estrangeiro = pd.read_sql_query(query_estrangeiro, conn)
# conn.close()
# print(df_estrangeiro.head(15))