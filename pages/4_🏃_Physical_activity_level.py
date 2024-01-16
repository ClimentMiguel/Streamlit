#pip install streamlit
#pip install statsmodels

import streamlit as st
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts


# Importamos el dataset
df = pd.read_csv('DATABASE RAW.csv')
df['Sleep Disorder'] = df['Sleep Disorder'].fillna('None')

# Pregunta
st.markdown('# :grey[Actividad Física y Pasos Diarios]')
st.markdown("# ¿Las personas que hacen ejercicio duermen mejor?")
c1,c2,c3 = st.columns(3)
boton1 = c1.button('Calidad de Sueño', key = 1)
boton2 = c2.button('Horas de sueño',key = 2)
boton3 = c3.button('Trastornos del sueño',key = 3)


#Graficas
# Graficas de calidad de sueño
if boton1:
    st.markdown('#### Calidad del sueño según nivel de ejercicio y pasos diarios')
    fig1 = px.scatter(
        data_frame=df, x="Physical Activity Level", y="Quality of Sleep", trendline="ols"
    )
    st.write(fig1)
   
    fig2 = px.scatter(
        data_frame=df, x="Daily Steps", y="Quality of Sleep", trendline="ols"
    )
    st.write(fig2)

#Graficas de horas de sueño
if boton2:
    st.markdown('#### Horas de sueño según nivel de ejercicio y pasos diarios')
    fig3 = px.scatter(
        data_frame=df, x="Physical Activity Level", y="Sleep Duration", trendline="ols"
    )
    st.write(fig3)

    fig4 = px.scatter(
        data_frame=df, x="Daily Steps", y="Sleep Duration", trendline="ols"
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

