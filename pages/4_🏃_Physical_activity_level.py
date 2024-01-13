#pip install streamlit
#pip install statsmodels

import streamlit as st
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts

# Importamos el dataset
df = pd.read_csv('/Users/Tomasss/uni/23_24Master/Visualizacion_de_datos/Entrega/Sleep_health_and_lifestyle_dataset.csv')

# Se presume que la cantidad de actividad fisica puede estar relacionada con el numero de pasos. Lo comprobamos:
st.markdown('## Correlacion actividad fisica ~ pasos diarios')
fig0 = px.scatter(df, x = 'Physical Activity Level', y = 'Daily Steps', trendline="ols")
st.write(fig0)
# Se ve que hay un poco de correlacion. 
# A la hora de ver como afecta a la calidad del sueño seguramente ambas afecten de manera parecida


# Primera gráfica. ¿Las personas que hacen ejercicio duermen mejor?
st.markdown("### ¿Las personas que hacen ejercicio duermen mejor?")
fig1 = px.scatter(
    data_frame=df, x="Physical Activity Level", y="Quality of Sleep"
)
st.write(fig1)
   

st.markdown("### Second Chart")
fig2 = px.histogram(data_frame=df, x="Daily Steps")
st.write(fig2)