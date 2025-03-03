import streamlit as st 
import pandas as pd
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import numpy as np

# Carrega o arquivo CSV
df = pd.read_csv("pizzas.csv")

# Criar o modelo de regressão linear
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]
modelo.fit(x, y)

# Titulo da aplicação
st.title("Prevendo o valor de uma pizza: ")
#st.divider()

# ==========================================================================
st.subheader("Gráfico de dados de Preço vs. Diametro")
plt.figure(figsize=(6,4))
plt.scatter(x, y, color="blue", label="Dados")
plt.plot(x, modelo.predict(x), color="red", label="Linha de Regressão")
plt.xlabel("Diametro (cm)")
plt.ylabel("Preço (R$)")
plt.legend()
st.pyplot(plt)

st.divider()
# ==========================================================================
diametro = st.number_input("Digite o tamanho do diametro da pizza: ")

if diametro != 0:

    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com o diametro de {diametro} é de R${preco_previsto:.2f}. ")
    st.balloons()
else:
    st.write("Digite um valor de diametro diferente de 0 para obter a previsão ")
