# Sprint-7---Proyecto

# 🚗 Análisis de Vehículos Usados

## 📌 Contexto
Aplicación web interactiva para analizar características de vehículos de segunda mano, con filtros dinámicos y visualizaciones.

## 🛠 Funcionalidades
- Filtrado por modelo, año y precio
- Gráficos interactivos con Plotly:
  - Dispersión: Precio vs Año
  - Barras: Conteo por modelo
- Despliegue en Render

## 🔍 Dataset
`vehicles_us.csv` contiene:
- 10,000 registros
- Columnas: `price`, `model_year`, `odometer`, `condition`, etc.

## ▶ Ejecución local
```bash
streamlit run app.py
