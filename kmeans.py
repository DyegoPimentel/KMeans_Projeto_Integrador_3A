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

# Importamos o numpy para realizar a manipulação numerica.
import numpy as np

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
#print(df['id_paciente'])

# Aqui foi criado um dataframe com a variavel dados para que possamos manipular os dados sem interferir no banco de dados.
dados = pd.DataFrame(data=df, columns=['id_paciente','nome','id_sintomas','sintomas'])
#print(dados.head())

# A variavel X recebe as colunas de id de pacientes e sintomas, para ser utilizada no kmeans.
X = df[['id_paciente','id_sintomas']]
#print(X.head())

# Kmeans
kmeans = KMeans(n_clusters = 3, max_iter = 300, n_init = 10)
clusters = kmeans.fit_predict(X)
#print(clusters)

# Insere a coluna "cluster"
dados.insert(loc=4, column='cluster', value=clusters)
print(dados.head())


x = X.to_numpy()
#print(x)

# Plota os pontos
plt.scatter(
    #df['id_paciente'],df['id_sintomas'],
    x[clusters == 0,0], x[clusters == 0,1],
    s=50, c='lightgreen',
    label='COVID-19'
    )

plt.scatter(
    #df['id_paciente'],df['id_sintomas'],
    x[clusters == 1,0], x[clusters == 1,1],
    s=50, c='orange',
    label='Dengue'
    )

plt.scatter(
    #df['id_paciente'],df['id_sintomas'],
    x[clusters == 2,0], x[clusters == 2,1],
    s=50, c='pink',
    label='Depressão'
    )

plt.title("Diagnostico de Doenças através de Sintomas")
plt.xlabel("Pacientes")
plt.ylabel("Sintomas")
plt.legend()
plt.show()
