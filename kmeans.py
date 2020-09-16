"""
Pontifícia Universidade Católica de Goiás

PROJETO INTEGRADOR 3-A

Curso: Big Data e Inteligência Artificial
Professor: Gustavo Siqueira Vinhal
Alunos: Diego de Medeiros, Dyego Pimentel, Vanessa Pereira, Ysaque Araujo.
Semestre: 2020/2
"""

################################################################
###############    IMPORTANDO AS BIBLIOTECAS     ###############
################################################################

# Importamos o pandas para visualizarmos o dataframe de forma 
# mais simples.
import pandas as pd

# Importamos o numpy para realizar a manipulação numerica.
import numpy as np

# Importamos o matplotlib para gerar graficos. 
import matplotlib.pyplot as plt

# Importamos o sklearn para realizar a clusterização. 
from sklearn.cluster import KMeans

################################################################
############### CONEXÃO COM MONGODB EM LOCALHOST ###############
################################################################

# Através desta linha importamos o MongoCliente que é responsavel
# por realizar a conexão com nosso banco de dados.
from pymongo import MongoClient

# Aqui criamos uma variavel para receber a conexão com nosso 
# banco de dados, neste caso estamos utilizando o mongoDB em 
# localhost utilizando a porta padrão.
client = MongoClient("localhost", 27017)

# Definimos a variavel "df" para receber os dados do banco de dados
df = pd.DataFrame.from_records(client.projeto_integrador_3A.sintomas.find())

# Aqui deletamos a coluna _ID pois não iremos precisar dela para o 
# desenvolvimento do nosso algoritmo.
del df['_id']


################################################################
######### CONEXÃO COM BANCO DE DADOS VIA GOOGLE SHEETS #########
################################################################
# Para usar esse metodo de conexão você deve comentar todas as #
# linhas da conexão com o mongoDB para evitar erros de conexão #
# e após isso descomente os codigos abaixo!                    #
################################################################
# Este metodo importa Google Sheets via link e converte para   #
# csv, indicada caso não possa instalar o mongoDB local.       #

""" DESCOMENTE AQUI SE QUISER USAR O GOOGLE SHEETS COMO BANCO DE 
DADOS.

googleSheetId = '1IVDqFrB1XLnhbrLiJW34BPkgNUXWdySsDSFH1XYxyeI'
workSheetName = 'projeto_integrador_3A'
urlGoogle = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(googleSheetId,workSheetName)

df = pd.read_csv(urlGoogle)

"""

################################################################
###############       TRATAMENTO DOS DADOS       ###############
################################################################

# Aqui foi criado um dataframe com a variavel "dados" para que 
# possamos manipular os dados sem interferir no banco de dados.
dados = pd.DataFrame(data=df, columns=['id_paciente','nome','id_sintomas','sintomas'])


# A variavel X recebe as colunas de id de pacientes e sintomas, 
# para ser utilizada no kmeans.
X = df[['id_paciente','id_sintomas']]

# Kmeans
kmeans = KMeans(n_clusters = 3, max_iter = 300, n_init = 10)
clusters = kmeans.fit_predict(X)

# Insere a coluna "cluster" no dataframe "dados", assim podemos
# identificar em qual grupo cada paciente esta.
dados.insert(loc=4, column='cluster', value=clusters)

# x representa os pacientes e os devidos sintomas.
x = X.to_numpy()


# Aqui gera uma tabela com todos os pacientes do cluster 0
grupo0 = dados.loc[dados['cluster'] == 0]

# Aqui gera uma tabela com todos os pacientes do cluster 1
grupo1 = dados.loc[dados['cluster'] == 1]

# Aqui gera uma tabela com todos os pacientes do cluster 2
grupo2 = dados.loc[dados['cluster'] == 2]

################################################################
###############             GRAFICOS             ###############
################################################################

# Este if verifica quais são os sintomas do grupo 0 e 
# retorna a legenda adequada.
if grupo0['id_sintomas'].isin(['1.0','1.9']).any(): # Aqui verifica se os sintomas dos pacientes do grupo 0 estão
# entre 1.0 e 1.9(identificação dos sintomas), se sim, significa que os pacientes do grupo 0 são os pacientes com 
# COVID. Se não vai para etapa do elif e continua a verificação até descobrir qual a doença esta relacionada ao
# grupo 0.
    plt.scatter( # essa função plota os pontos no grafico.
    x[clusters == 0,0], x[clusters == 0,1],
    s=50, c='red', # s=size | c=color
    label='COVID-19 (CLUSTER 0)' # legenda
    )
elif grupo0['id_sintomas'].isin(['2.0','2.9']).any() :
    plt.scatter(
    x[clusters == 0,0], x[clusters == 0,1],
    s=50, c='orange',
    label='Dengue (CLUSTER 0)'
    )
else:
    plt.scatter(
    x[clusters == 0,0], x[clusters == 0,1],
    s=50, c='black',
    label='Depressão (CLUSTER 0)'
    )

# Este if verifica quais são os sintomas do grupo 1 e 
# retorna a legenda adequada.
if grupo1['id_sintomas'].isin(['1.0','1.9']).any():
    plt.scatter( # essa função plota os pontos no grafico.
    x[clusters == 1,0], x[clusters == 1,1],
    s=50, c='red', # s=size | c=color
    label='COVID-19 (CLUSTER 1)' # legenda
    )
elif grupo1['id_sintomas'].isin(['2.0','2.9']).any() :
    plt.scatter(
    x[clusters == 1,0], x[clusters == 1,1],
    s=50, c='orange',
    label='Dengue (CLUSTER 1)'
    )
else:
    plt.scatter(
    x[clusters == 1,0], x[clusters == 1,1],
    s=50, c='black',
    label='Depressão (CLUSTER 1)'
    )

# Este if verifica quais são os sintomas do grupo 2 e
# retorna a legenda adequada.
if grupo2['id_sintomas'].isin(['1.0','1.9']).any():
    plt.scatter( # essa função plota os pontos no grafico.
    x[clusters == 2,0], x[clusters == 2,1],
    s=50, c='red', # s=size | c=color
    label='COVID-19 (CLUSTER 2)' # legenda
    )
elif grupo2['id_sintomas'].isin(['2.0','2.9']).any() :
    plt.scatter(
    x[clusters == 2,0], x[clusters == 2,1],
    s=50, c='orange',
    label='Dengue (CLUSTER 2)'
    )
else:
    plt.scatter(
    x[clusters == 2,0], x[clusters == 2,1],
    s=50, c='black',
    label='Depressão (CLUSTER 2)'
    )

plt.title("Diagnostico de Doenças através de Sintomas") # Esta função plota o titulo no grafico.
plt.xlabel("Pacientes") # Esta função plota a descrição do eixo X.
plt.ylabel("Sintomas") # Esta função plota a descrição do eixo Y.
plt.legend() # Esta função plota a legenda no grafico.
plt.show() # Esta função plota o grafico.
