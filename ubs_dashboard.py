import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o arquivo atualizado
df = pd.read_csv("ubs_atualizado.csv", sep=";")

# Contar a frequência de UBS por estado
df_freq = df['Nome_UF'].value_counts().reset_index()
df_freq.columns = ['Estado', 'Frequência']

# Criar o dashboard
st.title("Dashboard de Unidades Básicas de Saúde")

# Gráfico de barras
grafico = px.bar(df_freq, x='Estado', y='Frequência', 
                 title='Frequência de UBS', 
                 labels={'Estado': 'Estado', 'Frequência': 'Número de UBS'},
                 text_auto=True)

st.plotly_chart(grafico)

# Filtro para estados específicos
estados = st.multiselect("Selecione os estados", df_freq['Estado'].unique())
if estados:
    df_filtrado = df[df['Nome_UF'].isin(estados)]
    st.write(df_filtrado)

// comentario teste