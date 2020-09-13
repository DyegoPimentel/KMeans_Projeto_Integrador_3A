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

# Para nivelar, iremos criar um banco de dados "projeto_integrador_3A", E na sequência inserir dados fictícios.
db = client.projeto_integrador_3A

# Aqui iremos inserir 30 pacientes sendo 10 com covid, 10 com dengue, e 10 com ansiedade. 
# Foi inserido apenas o nome fictício do paciente, e os sintomas. Para que nosso algoritmo faça a classificação.
db.sintomas.insert_many(
    [
        {
        "id_paciente": 1,
        "nome":"Paciente 1",
        "id_sintomas":1,
        "sintomas":"Febre"
        },
        {
        "id_paciente": 2,
        "nome":"Paciente 2",
        "id_sintomas":1.1,
        "sintomas":"Dor de Cabeca"
        },
        {
        "id_paciente": 3,
        "nome":"Paciente 3",
        "id_sintomas":1,
        "sintomas":"Febre"
        },
        {
        "id_paciente": 4,
        "nome":"Paciente 4",
        "id_sintomas":1.1,
        "sintomas":"Dor de Cabeca"
        },
        {
        "id_paciente": 5,
        "nome":"Paciente 5",
        "id_sintomas":1,
        "sintomas":"Febre"
        },
        {
        "id_paciente": 6,
        "nome":"Paciente 6",
        "id_sintomas":1.1,
        "sintomas":"Dor de Cabeca"
        },
        {
        "id_paciente": 7,
        "nome":"Paciente 7",
        "id_sintomas":1.2,
        "sintomas":"Falta de Ar"
        },
        {
        "id_paciente": 8,
        "nome":"Paciente 8",
        "id_sintomas":1,
        "sintomas":"Febre"
        },
        {
        "id_paciente": 9,
        "nome":"Paciente 9",
        "id_sintomas":1.1,
        "sintomas":"Dor de Cabeca"
        },
        {
        "id_paciente": 10,
        "nome":"Paciente 10",
        "id_sintomas":1.2,
        "sintomas":"Falta de Ar"
        },
        {
        "id_paciente": 11,
        "nome":"Paciente 11",
        "id_sintomas":2,
        "sintomas":"Manchas Vermelhas"
        },
        {
        "id_paciente": 12,
        "nome":"Paciente 12",
        "id_sintomas":2,
        "sintomas":"Manchas Vermelhas"
        },
        {
        "id_paciente": 13,
        "nome":"Paciente 13",
        "id_sintomas":2.1,
        "sintomas":"Dor no Corpo"
        },
        {
        "id_paciente": 14,
        "nome":"Paciente 14",
        "id_sintomas":2,
        "sintomas":"Manchas Vermelhas"
        },
        {
        "id_paciente": 15,
        "nome":"Paciente 15",
        "id_sintomas":2.1,
        "sintomas":"Dor no Corpo"
        },
        {
        "id_paciente": 16,
        "nome":"Paciente 16",
        "id_sintomas":2.2,
        "sintomas":"Falta de Apetite"
        },
        {
        "id_paciente": 17,
        "nome":"Paciente 17",
        "id_sintomas":2,
        "sintomas":"Manchas Vermelhas"
        },
        {
        "id_paciente": 18,
        "nome":"Paciente 18",
        "id_sintomas":2.2,
        "sintomas":"Falta de Apetite"
        },
        {
        "id_paciente": 19,
        "nome":"Paciente 19",
        "id_sintomas":2,
        "sintomas":"Manchas Vermelhas"
        },
        {
        "id_paciente": 20,
        "nome":"Paciente 20",
        "id_sintomas":2.1,
        "sintomas":"Dor no Corpo"
        },
        {
        "id_paciente": 21,
        "nome":"Paciente 21",
        "id_sintomas":3,
        "sintomas":"Isolamento Social"
        },
        {
        "id_paciente": 22,
        "nome":"Paciente 22",
        "id_sintomas":3,
        "sintomas":"Isolamento Social"
        },
        {
        "id_paciente": 23,
        "nome":"Paciente 23",
        "id_sintomas":3.1,
        "sintomas":"Medo"
        },
        {
        "id_paciente": 24,
        "nome":"Paciente 24",
        "id_sintomas":3,
        "sintomas":"Isolamento Social"
        },
        {
        "id_paciente": 25,
        "nome":"Paciente 25",
        "id_sintomas":3.2,
        "sintomas":"Ansiedade"
        },
        {
        "id_paciente": 26,
        "nome":"Paciente 26",
        "id_sintomas":3.1,
        "sintomas":"Medo"
        },
        {
        "id_paciente": 27,
        "nome":"Paciente 27",
        "id_sintomas":3,
        "sintomas":"Isolamento Social"
        },
        {
        "id_paciente": 28,
        "nome":"Paciente 28",
        "id_sintomas":3.1,
        "sintomas":"Medo"
        },
        {
        "id_paciente": 29,
        "nome":"Paciente 29",
        "id_sintomas":3,
        "sintomas":"Isolamento Social"
        },
        {
        "id_paciente": 30,
        "nome":"Paciente 30",
        "id_sintomas":3.2,
        "sintomas":"Ansiedade"
        },
    ]
)