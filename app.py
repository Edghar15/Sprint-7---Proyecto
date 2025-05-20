import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🚗 Análisis de Vehículos Usados")

@st.cache_data
def load_data():
    return pd.read_csv("data/vehicles_us.csv")

df = load_data()

# Sidebar
st.sidebar.header("Filtros")
selected_models = st.sidebar.multiselect(
    "Modelos:", 
    options=df["model"].unique(),
    default=df["model"].unique()[0]
)

# DataFrame filtrado
filtered_df = df[df["model"].isin(selected_models)]
st.dataframe(filtered_df)

st.header("Gráficos Interactivos")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.scatter(filtered_df, x="year", y="price", color="model")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    conteo_modelos = filtered_df['model'].value_counts().reset_index()
    conteo_modelos.columns = ['modelo', 'cantidad']
    fig2 = px.bar(
        conteo_modelos,
        x='modelo',
        y='cantidad',
        labels={'modelo': 'Modelo', 'cantidad': 'Vehículos'}
    )
    st.plotly_chart(fig2, use_container_width=True)