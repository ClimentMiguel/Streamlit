#pip install streamlit
#pip install statsmodels

import streamlit as st
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts


# Importamos el dataset
df = pd.read_csv('/Users/Tomasss/uni/23_24Master/Visualizacion_de_datos/Entrega/Sleep_health_and_lifestyle_dataset.csv')
df['Sleep Disorder'] = df['Sleep Disorder'].fillna('None')

# Pregunta
st.markdown('# :grey[Actividad Física y Pasos Diarios]')
st.markdown("# ¿Las personas que hacen ejercicio duermen mejor?")

boton1 = st.button('Calidad de Sueño')
boton2 = st.button('Horas de sueño')
boton3 = st.button('Trastornos del sueño')


#Graficas
# Graficas de calidad de sueño
if boton1:
    st.markdown('#### Calidad del sueño según nivel de ejercicio y pasos diarios')
    fig1 = px.scatter(
        data_frame=df, x="Physical Activity Level", y="Quality of Sleep", trendline="lowess"
    )
    st.write(fig1)
   
    fig2 = px.scatter(
        data_frame=df, x="Daily Steps", y="Quality of Sleep", trendline="lowess"
    )
    st.write(fig2)

#Graficas de horas de sueño
if boton2:
    st.markdown('#### Horas de sueño según nivel de ejercicio y pasos diarios')
    fig3 = px.scatter(
        data_frame=df, x="Physical Activity Level", y="Sleep Duration", trendline="lowess"
    )
    st.write(fig3)

    fig4 = px.scatter(
        data_frame=df, x="Daily Steps", y="Sleep Duration", trendline="lowess"
    )
    st.write(fig4)

# Graficas del trastorno de sueño
if boton3:
    st.markdown("#### Trastorno o no según nivel de ejercicio y pasos diarios")
    st.markdown("Nivel de Actividad Física")
    fig5 = px.box(data_frame=df, x="Sleep Disorder", y = 'Physical Activity Level')
    st.write(fig5)

    st.markdown("Pasos diarios")
    fig6 = px.box(data_frame=df, x="Sleep Disorder", y = 'Daily Steps')
    st.write(fig6)

