# Inteligencia_artificial
Estudo voltado para inteligência artificial

#### Instalação Poetry <br>

`pip install poetry`<br>
Cria uma pasta para o projeto `projeto`<br>


### Inicio
Abre um novo terminal no vscode e cria uma maquina virtual `venv`<br>
`python -m venv venv` ativa a MV <br>
`.\venv\Script\activate`<br>

##### Dentro da pasta do Projeto Com o poetry ja instalado e com a VM ativada add as bibliotecas
`poetry add pandas scikit-learn streamlit matplotlib`


#### Instalação das Bibliotecas
`pip install pandas`<br>
`pip install scikit-learn`<br>
`pip install streamlit`<br>
`pip install matplotlib`<br>


#### Comandos 
`pip freez` - lista as bibliotecas instaladas


##### Salva dentro do projeto um arquivo .csv com os Diametros e os Preços das pizzas Exemplo:
```
diametro,preco
20,50
22,55
24,60
26,65
28,70
30,75
32,80
34,85
36,90
38,95
40,100

```

#### Cria 2 arquivo no principal (app.py e teste.ipynb) no arquivo jupter teste.ipynb

```
# Carregando o arquivo .csv
import pandas as pd

df = pd.read_csv("pizzas.csv")
df
```
####  Grafico 
```
df.plot(kind="scatter", x="diametro", y="preco")
```
##### <Axes: xlabel='diametro', ylabel='preco'>
```
from sklear import lenear_model
model = linear_model.LinearRegression()

# trinamento do modelo
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)
```
Predict<br>
  * estudar o predict([[diametro]]) 
```
print(modelo.predict([[110]])[0][0])
```
# -------------
Passa os parametros no teste para o arquivo `app.py` <br>
```
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

st.title("Prevendo o valor da pizza pelo Diametro: ")
```
no terminal da o comando: <br>
`streamlit run app.py` <br>

![image](https://github.com/user-attachments/assets/ecef519f-75e2-478c-8471-5cb79878eded)

