import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o arquivo CSV
def load_data():
    df = pd.read_csv("ubs_atualizado.csv", sep=";", encoding="utf-8")
    return df

df = load_data()

# Criar interface no Streamlit
st.title("Histograma da Quantidade de UBS por Município")

# Contar UBS por município
df_count = df["Nome_Município"].value_counts().reset_index()
df_count.columns = ["Município", "Total"]

# Controle deslizante para filtrar municípios
min_ubs, max_ubs = st.slider(
    "Selecione o intervalo de UBS por município",
    min_value=int(df_count["Total"].min()),
    max_value=int(df_count["Total"].max()),
    value=(int(df_count["Total"].min()), int(df_count["Total"].max()))
)

df_filtered = df_count[(df_count["Total"] >= min_ubs) & (df_count["Total"] <= max_ubs)]

# Criar histograma com Plotly
fig = px.histogram(df_filtered, x="Município", y="Total", title="Quantidade de UBS por Município", labels={"Município": "Município", "Total": "Número de UBS"}, nbins=50)

# Exibir gráfico no Streamlit
st.plotly_chart(fig)

st.write("Total de UBSs no dataset:", df.shape[0])
