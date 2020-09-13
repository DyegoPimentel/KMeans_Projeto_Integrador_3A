"""
Pontifícia Universidade Católica de Goiás

PROJETO INTEGRADOR 3-A

Curso: Big Data e Inteligência Artificial
Professor: Gustavo Siqueira Vinhal
Alunos: Diego de Medeiros, Dyego Pimentel, Vanessa Pereira, Ysaque Araujo.
Semestre: 2020/2
"""

# Importamos o pandas para visualizarmos o dataframe de forma mais simples.
import pandas as pd

# Importamos o matplotlib para gerar graficos. 
import matplotlib.pyplot as plt

# Importamos o sklearn para realizar a clusterização. 
from sklearn.cluster import KMeans

# Através desta linha importamos o MongoCliente que é responsavel por realizar a conexão com nosso banco de dados.
from pymongo import MongoClient

# Aqui criamos uma variavel para receber a conexão com nosso banco de dados, neste caso estamos utilizando o mongoDB em localhost.
client = MongoClient("localhost", 27017)

# Definimos a variavel "df" para receber os dados do banco de dados
df = pd.DataFrame.from_records(client.projeto_integrador_3A.sintomas.find())

# Aqui deletamos a coluna _ID pois não iremos precisar dela para o desenvolvimento do nosso algoritmo.
del df['_id']

# A linha abaixo é apenas para verificar se a variavel "df" esta retornando os dados corretamente. 
print(df.head())

