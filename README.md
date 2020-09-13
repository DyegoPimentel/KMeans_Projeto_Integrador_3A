# Projeto_Integrador_3A
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

<p><strong>Arquivos Inclusos</strong></p>

<p>O arquivo “dataset.py” é responsável por criar o banco de dados “projeto_integrador_3A”, e criar a coleção “sintomas”. Dentro desta coleção, será inserido 30 documentos de pacientes com 3 doenças distintas (COVID-19, Dengue, Ansiedade). Este dataset é fictício, fique à vontade para usar outro dataset caso tenha interesse.</p>



