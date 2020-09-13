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
        "Nome":"Paciente 1",
        "Sintomas":["Febre","Dor de Cabeça", "Cansaço"]
        },
        {
        "Nome":"Paciente 2",
        "Sintomas":["Febre","Dor de Cabeça", "Cansaço"]
        },
        {
        "Nome":"Paciente 3",
        "Sintomas":["Febre","Dor de Cabeça", "Cansaço"]
        },
        {
        "Nome":"Paciente 4",
        "Sintomas":["Febre","Dor de Cabeça", "Cansaço"]
        },
        {
        "Nome":"Paciente 5",
        "Sintomas":["Febre","Dor de Cabeça", "Cansaço"]
        },
        {
        "Nome":"Paciente 6",
        "Sintomas":["Febre","Dor de Cabeça", "Cansaço"]
        },
        {
        "Nome":"Paciente 7",
        "Sintomas":["Febre","Dor de Cabeça", "Cansaço"]
        },
        {
        "Nome":"Paciente 8",
        "Sintomas":["Febre","Dor de Cabeça", "Cansaço"]
        },
        {
        "Nome":"Paciente 9",
        "Sintomas":["Febre","Dor de Cabeça", "Cansaço"]
        },
        {
        "Nome":"Paciente 10",
        "Sintomas":["Febre","Dor de Cabeça", "Cansaço"]
        },
        {
        "Nome":"Paciente 11",
        "Sintomas":["Dores Musculares","Manchas Vermelhas", "Falta de Apetite"]
        },
        {
        "Nome":"Paciente 12",
        "Sintomas":["Dores Musculares","Manchas Vermelhas", "Falta de Apetite"]
        },
        {
        "Nome":"Paciente 13",
        "Sintomas":["Dores Musculares","Manchas Vermelhas", "Falta de Apetite"]
        },
        {
        "Nome":"Paciente 14",
        "Sintomas":["Dores Musculares","Manchas Vermelhas", "Falta de Apetite"]
        },
        {
        "Nome":"Paciente 15",
        "Sintomas":["Dores Musculares","Manchas Vermelhas", "Falta de Apetite"]
        },
        {
        "Nome":"Paciente 16",
        "Sintomas":["Dores Musculares","Manchas Vermelhas", "Falta de Apetite"]
        },
        {
        "Nome":"Paciente 17",
        "Sintomas":["Dores Musculares","Manchas Vermelhas", "Falta de Apetite"]
        },
        {
        "Nome":"Paciente 18",
        "Sintomas":["Dores Musculares","Manchas Vermelhas", "Falta de Apetite"]
        },
        {
        "Nome":"Paciente 19",
        "Sintomas":["Dores Musculares","Manchas Vermelhas", "Falta de Apetite"]
        },
        {
        "Nome":"Paciente 20",
        "Sintomas":["Dores Musculares","Manchas Vermelhas", "Falta de Apetite"]
        },
        {
        "Nome":"Paciente 21",
        "Sintomas":["Fadiga","Medo", "Insônia"]
        },
        {
        "Nome":"Paciente 22",
        "Sintomas":["Fadiga","Medo", "Insônia"]
        },
        {
        "Nome":"Paciente 23",
        "Sintomas":["Fadiga","Medo", "Insônia"]
        },
        {
        "Nome":"Paciente 24",
        "Sintomas":["Fadiga","Medo", "Insônia"]
        },
        {
        "Nome":"Paciente 25",
        "Sintomas":["Fadiga","Medo", "Insônia"]
        },
        {
        "Nome":"Paciente 26",
        "Sintomas":["Fadiga","Medo", "Insônia"]
        },
        {
        "Nome":"Paciente 27",
        "Sintomas":["Fadiga","Medo", "Insônia"]
        },
        {
        "Nome":"Paciente 28",
        "Sintomas":["Fadiga","Medo", "Insônia"]
        },
        {
        "Nome":"Paciente 29",
        "Sintomas":["Fadiga","Medo", "Insônia"]
        },
        {
        "Nome":"Paciente 30",
        "Sintomas":["Fadiga","Medo", "Insônia"]
        },
    ]
)