# Projeto_Integrador_3A <br> KMeans - Aprendizado Não Supervisionado
Neste Projeto Integrador iremos utilizar a tecnica de Aprendizado não supervisionado (K-Means) para classificar doenças através dos sintomas dos pacientes.

<p><strong> Programas necessarios </strong></p>
<ul>
<li>MongoDB: https://www.mongodb.com/try/download/community</li>
<li>Python(Anaconda): https://www.anaconda.com/products/individual</li>
</ul>
<p><strong> Passo a Passo </strong></p>
<p>Após instalar o MongoDB e o Python(Anaconda) certifique-se de que sua versão do “pip” esta atualizado, para isso basta entrar via prompt de comando na pasta do seu projeto e digitar:</p>

<p><code>python -m pip install --upgrade pip</code></p>

<p>Após isso, podemos instalar o modulo “Pymongo” que fara a conexão da nossa aplicação com o banco de dados, inserindo via prompt de comando na pasta do projeto o seguinte codigo:</p>

<p><code>python -m pip install pymongo</code></p>

<p>Precisaremos do modulo "Pandas" para o nosso algoritimo, para isso basta inserir via prompt de comando os seguintes codigos:

<p><code>pip install wheel</code></p>
<p><code>pip install pandas</code></p>

<p>Usaremos o Matplotlib para gerar os graficos, para isso basta inserir via prompt de comando o seguinte codigo:</p>

<p><code>python -m pip install -U matplotlib</code></p>

<p>Para realizar a clusterização iremos utilizar a biblioteca do sklearn, para isso basta inserir via prompt de comando o seguinte codigo:</p>

<p><code>pip install -U scikit-learn</code></p>

<p><strong>Arquivos Inclusos</strong></p>

<p>O arquivo “dataset.py” é responsável por criar o banco de dados “projeto_integrador_3A”, e criar a coleção “sintomas”. Dentro desta coleção, será inserido 30 documentos de pacientes com 3 doenças distintas (COVID-19, Dengue, Depressão). Este dataset é fictício, fique à vontade para usar outro dataset caso tenha interesse.</p>

<p>O arquivo "kmeans.py" é responsavel por realizar o agrupamento dos pacientes baseado nos sintomas, e após os clusters serem formados, um grafico informando a qual cluster cada doença pertence é gerado. </p>

<p><strong>Pontifícia Universidade Católica de Goiás</strong></p>

<p><strong>PROJETO INTEGRADOR 3-A</strong></p>

<p>Curso: Big Data e Inteligência Artificial
Professor: Gustavo Siqueira Vinhal
Alunos: Diego de Medeiros, Dyego Pimentel, Vanessa Pereira, Ysaque Araujo.
Semestre: 2020/2</p>


