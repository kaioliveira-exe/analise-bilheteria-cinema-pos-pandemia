import pandas
import sqlite3
import filtragem_limpeza

conn = sqlite3.connect('database.db')
filtragem_limpeza.tabela_filtrada.to_sql('tabela_filmes', conn, index='false', if_exists='replace')

