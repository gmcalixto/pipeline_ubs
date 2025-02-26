import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Carregar o arquivo CSV
def load_data():
    df = pd.read_csv("ubs_atualizado.csv", sep=";", encoding="utf-8")
    df["LATITUDE"] = df["LATITUDE"].astype(str).str.replace(",", ".").astype(float)
    df["LONGITUDE"] = df["LONGITUDE"].astype(str).str.replace(",", ".").astype(float)
    return df.dropna(subset=["LATITUDE", "LONGITUDE"])  # Remover valores NaN

df = load_data()

# Criar interface no Streamlit
st.title("Mapa de UBS por Estado")

# Seleção de UF pelo Nome_UF
ufs = df["Nome_UF"].unique()
uf_selected = st.selectbox("Selecione a UF", sorted(ufs))

df_filtered = df[df["Nome_UF"] == uf_selected]

# Criar mapa Folium
map_center = [df_filtered["LATITUDE"].mean(), df_filtered["LONGITUDE"].mean()]
m = folium.Map(location=map_center, zoom_start=6)

for _, row in df_filtered.iterrows():
    folium.Marker(
        location=[row["LATITUDE"], row["LONGITUDE"]],
        popup=row["NOME"],
        icon=folium.Icon(icon="info-sign")
    ).add_to(m)

# Exibir o mapa no Streamlit
folium_static(m)

st.write(f"Total de UBSs exibidas: {len(df_filtered)}")
