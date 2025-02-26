import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o arquivo CSV
def load_data():
    df = pd.read_csv("ubs_atualizado.csv", sep=";", encoding="utf-8")
    return df

df = load_data()

# Criar interface no Streamlit
st.title("Distribuição de UBS por Estado")

# Contar UBS por estado
df_count = df["Nome_UF"].value_counts().reset_index()
df_count.columns = ["Estado", "Total"]

# Criar gráfico de pizza com Plotly
fig = px.pie(df_count, names="Estado", values="Total", title="Distribuição de UBS por Estado", hole=0.3)

# Exibir gráfico no Streamlit
st.plotly_chart(fig)

st.write("Total de UBSs no dataset:", df.shape[0])
