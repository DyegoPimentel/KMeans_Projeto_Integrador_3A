"""
Pontifícia Universidade Católica de Goiás

PROJETO INTEGRADOR 3-A

Curso: Big Data e Inteligência Artificial
Professor: Gustavo Siqueira Vinhal
Alunos: Diego de Medeiros, Dyego Pimentel, Vanessa Pereira, Ysaque Araujo.
Semestre: 2020/2
"""

# Através desta linha importamos o MongoCliente que é responsavel por realizar a conexão com nosso banco de dados.
from pymongo import MongoClient


# Aqui criamos uma variavel para receber a conexão com nosso banco de dados, neste caso estamos utilizando o mongoDB em localhost.
client = MongoClient("localhost", 27017)

# O print abaixo foi usado para retornar os nomes dos bancos de dados existentes, e assim confirmar que a conexão através da variavel "client" esta ok.
# print(client.list_database_names())

###########################
### TABELA DE SINTOMAS
###
### 1 - FEBRE
### 2 - DOR DE CABEÇA
### 3 - FALTA DE AR
### 4 - MANCHAS VERMELHAS
### 5 - FALTA DE APETITE
### 6 - DOR NO CORPO
### 7 - ISOLAMENTO SOCIAL
### 8 - MEDO
### 9 - ANSIEDADE
###
############################

# Para nivelar, iremos criar um banco de dados "projeto_integrador_3A", E na sequência inserir dados fictícios.
db = client.projeto_integrador_3A

# Aqui iremos inserir 30 pacientes sendo 10 com covid, 10 com dengue, e 10 com ansiedade. 
# Foi inserido apenas o nome fictício do paciente, e os sintomas. Para que nosso algoritmo faça a classificação.
db.sintomas.insert_many(
    [
        {
        "id_paciente": 1,
        "nome":"Paciente 1",
        "id_sintoma_1":1,
        "sintoma 1":"Febre",
        "id_sintoma_2":2,
        "sintoma 2":"Dor de Cabeca"   
        },
        {
        "id_paciente": 2,
        "nome":"Paciente 2",
        "id_sintoma_1":2,
        "sintoma 1":"Dor de Cabeca",
        "id_sintoma_2":3,
        "sintoma 2":"Falta de Ar"  
        },
        {
        "id_paciente": 3,
        "nome":"Paciente 3",
        "id_sintoma_1":1,
        "sintoma 1":"Febre",
        "id_sintoma_2":3,
        "sintoma 2":"Falta de Ar" 
        },
        {
        "id_paciente": 4,
        "nome":"Paciente 4",
        "id_sintoma_1":1,
        "sintoma 1":"Febre",
        "id_sintoma_2":2,
        "sintoma 2":"Dor de Cabeca" 
        },
        {
        "id_paciente": 5,
        "nome":"Paciente 5",
        "id_sintoma_1":3,
        "sintoma 1":"Falta de Ar",
        "id_sintoma_2":2,
        "sintoma 2":"Dor de Cabeca" 
        },
        {
        "id_paciente": 6,
        "nome":"Paciente 6",
        "id_sintoma_1":4,
        "sintoma 1":"Manchas Vermelhas",
        "id_sintoma_2":5,
        "sintoma 2":"Falta de Apetite"
        },
        {
        "id_paciente": 7,
        "nome":"Paciente 7",
        "id_sintoma_1":4,
        "sintoma 1":"Manchas Vermelhas",
        "id_sintoma_2":6,
        "sintoma 2":"Dor no Corpo"
        },
        {
        "id_paciente": 8,
        "nome":"Paciente 8",
        "id_sintoma_1":6,
        "sintoma 1":"Dor no Corpo",
        "id_sintoma_2":5,
        "sintoma 2":"Falta de Apetite"
        },
                {
        "id_paciente": 9,
        "nome":"Paciente 9",
        "id_sintoma_1":4,
        "sintoma 1":"Manchas Vermelhas",
        "id_sintoma_2":5,
        "sintoma 2":"Falta de Apetite"
        },
        {
        "id_paciente": 10,
        "nome":"Paciente 10",
        "id_sintoma_1":6,
        "sintoma 1":"Dor no Corpo",
        "id_sintoma_2":4,
        "sintoma 2":"Manchas Vermelhas"
        },

        {
        "id_paciente": 11,
        "nome":"Paciente 11",
        "id_sintoma_1":7,
        "sintoma 1":"Isolamento Social",
        "id_sintoma_2":8,
        "sintoma 2":"Medo"
        },
        {
        "id_paciente": 12,
        "nome":"Paciente 12",
        "id_sintoma_1":7,
        "sintoma 1":"Isolamento Social",
        "id_sintoma_2":9,
        "sintoma 2":"Ansiedade"
        },
        {
        "id_paciente": 13,
        "nome":"Paciente 13",
        "id_sintoma_1":8,
        "sintoma 1":"Medo",
        "id_sintoma_2":9,
        "sintoma 2":"Ansiedade"
        },
                {
        "id_paciente": 14,
        "nome":"Paciente 14",
        "id_sintoma_1":7,
        "sintoma 1":"Isolamento Social",
        "id_sintoma_2":9,
        "sintoma 2":"Ansiedade"
        },
        {
        "id_paciente": 15,
        "nome":"Paciente 15",
        "id_sintoma_1":8,
        "sintoma 1":"Medo",
        "id_sintoma_2": 7,
        "sintoma 2":"Isolamento Social"
        },

    ]
)