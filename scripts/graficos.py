from turtle import color, width

from altair import FontWeight
from matplotlib.lines import lineStyles
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
# from analises import df_query_terror
# from analises import df_estrangeiro
# from analises import df_query_agrupamento
from analises import df_streaming


#--- GRÁFICO GÊNERO X LUCRO ---
#Com o matplotlib desenha o gráfico de baixo para cima, é necessário inverter a tabela para que os gêneros principais apareçam no topo
# df_barras = df_query_agrupamento[::-1]

# #Associação das colunas da tabela com os eixos do gráfico (e adaptação da coluna para melhor visualização no gráfico)
# df_genero = df_barras['Genero']
# df_lucro = (
#     df_barras['Lucro_Medio']
#     .str.replace('$', '', regex=False)
#     .str.replace(',', '', regex=False)
#     .astype(float) / 1_000_000
# )


# #Criando o visual/tamanho do gráfico
# plt.figure(figsize=(10, 6))

# #Associando cores ao top 3 principal + resto
# cores = []
# for genero in df_genero:
#     if genero == 'Animação':
#         cores.append('#0056b3')
#     elif genero == 'Aventura':
#         cores.append('#00b306')
#     elif genero == 'Sci-Fi':
#         cores.append('#b3001b')
#     else:
#         cores.append('#b0c4de')

# #Criando as barras horizontais
# plt.barh(df_genero, df_lucro, color=cores)

# #Título do gráfico e dos eixos
# plt.title('Quais gêneros cinematográficos dão mais lucro no período pós-pandemia (2022-atualmente)?', fontsize=12, fontweight='bold', pad=15)
# plt.xlabel('Lucro médio (em milhões de doláres)')
# plt.ylabel('Gêneros')

# #Criando os separadores de valores no eixo X
# plt.xticks(range(0, 101, 20))
# plt.grid(axis='x', linestyle='--', alpha=0.5)

# #Exibição do gráfico
# plt.tight_layout()
# plt.show()


#--- GRÁFICO ROI - TERROR ---

# 1. Configuração do visual

# plt.figure(figsize=(12,7))
# sns.set_theme(style='whitegrid')


# # 2. Criação das cores e do boxplot
# cores = {'Terror': '#b3001b', 'Animação': '#b0c4de', 'Aventura': '#b0c4de', 'Sci-Fi': '#b0c4de'}

# sns.boxplot(
#     data=df_query_terror,
#     x='genero_agrupado',
#     y='ROI',
#     palette=cores,
#     width=0.5,
#     fliersize=4
# )


# # 3. O PULO DO GATO: Ajustando a escala do eixo Y
# # Como o Skinamarink tem ROI de 141, se não limitarmos o eixo Y, 
# # as caixas vão ficar minúsculas perto do zero. Vamos limitar o Y de -2 até 20 
# # para focar na "zona de segurança" do investimento real!
# plt.ylim(-2, 20)


# # 4. Criando os títulos
# plt.title('Análise de Risco e Retorno: O Terror é mais seguro? (2022-atualmente)')
# plt.xlabel('Gêneros')
# plt.ylabel('ROI (Retorno Sobre o Investimento)')

# # 7. Visualização do gráfico
# plt.tight_layout()
# plt.show()



# --- GRÁFICO COMPARATIVO - FILMES ESTRANGEIROS --- 

# # 1. Filtramos os dados por Era e pegamos os 15 mais lucrativos de cada uma
# pre_pandemia = df_estrangeiro[df_estrangeiro['era_cinema'].str.contains('2015-2019')].nlargest(15, 'lucro')
# #ou pre_pandemia = df_estrangeiro[df_estrangeiro['era_cinema'].str.contains('2015-2019')].sortvalues(by='lucro', ascending=False).head(15)
# pos_pandemia = df_estrangeiro[df_estrangeiro['era_cinema'].str.contains('2022-atualmente')].nlargest(15, 'lucro')

# # 2. Vamos ver a média de lucro do Top 15 de cada época
# print(f"Lucro MÉDIO do Top 15 Estrangeiro (Pré-Pandemia): USD {pre_pandemia['lucro'].mean() / 1_000_000:.1f} Milhões")
# print(f"Lucro MÉDIO do Top 15 Estrangeiro (Pós-Pandemia): USD {pos_pandemia['lucro'].mean() / 1_000_000:.1f} Milhões")

# 3. Criando um DataFrame rápido com os resultados que você encontrou
# dados_veredito = pd.DataFrame({
#     'Era': ['Pré-Pandemia (2015-2019)', 'Pós-Pandemia (2022-atualmente)'],
#     'Lucro Médio (Milhões USD)': [362.6, 508.3]
# })

# # 4. Configuração do visual do gráfico
# plt.figure(figsize=(8, 6))
# sns.set_theme(style="whitegrid")

# # 5. Criando o gráfico de barras
# cores = ['#b0c4de', '#1f4e79'] # Azul claro para o passado, Azul escuro para o recorde atual
# ax = sns.barplot(
#     data=dados_veredito, 
#     x='Era', 
#     y='Lucro Médio (Milhões USD)', 
#     palette=cores,
#     hue='Era',
#     legend=False
# )

# # 6. O PULO DO GATO: Adicionando os números em cima das barras
# for p in ax.patches:
#     ax.annotate(f"USD {p.get_height():.1f} M", 
#                 (p.get_x() + p.get_width() / 2., p.get_height() - 40), 
#                 ha='center', va='center', 
#                 xytext=(0, 10), 
#                 textcoords='offset points', 
#                 fontsize=12, fontweight='bold', color='white' if p.get_height() > 400 else 'black')

# # 7. Títulos e Ajustes
# plt.title('Cinema Internacional: Quebrando as Barreiras de Lucro', fontsize=14, fontweight='bold', pad=15)
# plt.ylabel('Lucro Líquido Médio do Top 15 (Em Milhões de USD)', fontsize=11)
# plt.xlabel('', fontsize=11)
# plt.ylim(0, 600) # Dá um espacinho no topo do gráfico

# plt.tight_layout()
# plt.show()

