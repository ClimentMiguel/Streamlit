




# Importación de librerías
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Carga de datos
df = pd.read_csv(r'sleep.csv')

# TÍTULO: ¿Influye la profesión en la calidad y duración del sueño?
st.markdown("<p style='color: green; font-size: 24px;'>¿Influye la profesión en la calidad y duración del sueño?</p>", unsafe_allow_html=True)




####################################################################################################################
#GRÁFICA 1: Profesión y calidad y duración

import streamlit as st
import pandas as pd
import plotly.express as px

# Suponiendo que ya tienes media_calidad_sueno y media_duracion calculados
media_calidad_sueno = df.groupby('Occupation')['Quality of Sleep'].mean().reset_index()
media_duracion = df.groupby('Occupation')['Sleep Duration'].mean().reset_index()

# Fusionar los DataFrames por profesión
media_combinada = pd.merge(media_calidad_sueno, media_duracion, on='Occupation', how='inner')

# Ordenar el DataFrame por la media de calidad del sueño de forma descendente
media_combinada = media_combinada.sort_values(by='Quality of Sleep', ascending=False)

# Crear gráfico de barras agrupadas
fig = px.bar(media_combinada, x='Occupation', y=['Quality of Sleep', 'Sleep Duration'],
             title='Comparación de la calidad y duración del sueño por profesión ',
             labels={'value': 'Valor Medio', 'variable': 'Métrica', 'Occupation': 'Profesión'},
             barmode='group',  # barmode='group' agrupa las barras para cada profesión
             color_discrete_map={'Quality of Sleep': 'green', 'Sleep Duration': 'lightgreen'})  # Define los colores

# Establecer el rango del eje y de 0 a 10
fig.update_yaxes(range=[0, 10])

# Mostrar el gráfico de barras agrupadas
st.plotly_chart(fig)



















####################################################################################################################


























st.markdown("<p style='color: green; font-size: 24px;'>¿Influye la profesión en el desarrollo de trastornos del sueño?</p>", unsafe_allow_html=True)
####################################################################################################################
#GRÁFICA 2: TRASTORNO DEL SUEÑO POR PROFESIÓN

import streamlit as st
import pandas as pd
import plotly.express as px

# Obtener la lista única de profesiones
profesiones = df['Occupation'].unique()

# Añadir un selectbox con las opciones de profesiones
opcion_seleccionada = st.selectbox('Selecciona una profesión', profesiones)

# Filtrar el DataFrame según la profesión seleccionada
df_profesion = df[df['Occupation'] == opcion_seleccionada]

# Contar la frecuencia de cada tipo de Sleep Disorder
conteo_sleep_disorder = df_profesion['Sleep Disorder'].value_counts()

# Definir colores personalizados
colors_pie = {'None': 'grey', 'Sleep Apnea': 'Green', 'Insomnia': 'lightgreen'}  # Modificado para Insomnia

# Crear un gráfico de tarta con Plotly Express y colores personalizados
fig = px.pie(conteo_sleep_disorder, values=conteo_sleep_disorder.values, names=conteo_sleep_disorder.index,
             title=f'Porcentaje de trastornos del sueño para {opcion_seleccionada}')

# Cambiar colores usando el parámetro template
fig.update_traces(marker=dict(colors=[colors_pie[disorder] for disorder in conteo_sleep_disorder.index]))

# Mostrar el gráfico de tarta
st.plotly_chart(fig)








































st.markdown('---')
#GRÁFICA 3: TRASTORNO DEL SUEÑO POR PROFESIÓN

import pandas as pd
import plotly.express as px
import streamlit as st

# Definir colores personalizados
colors = {'None': 'grey', 'Sleep Apnea': 'green', 'Insomnia': 'lightgreen'}

# Calcular la tabla de contingencia (crosstab) con las frecuencias
conteo_profesiones = pd.crosstab(index=df['Occupation'], columns=df['Sleep Disorder'])

# Reorganizar las columnas para poner 'None' al final
conteo_profesiones = conteo_profesiones[['Sleep Apnea', 'Insomnia', 'None']]

# Calcular el total por profesión
total_por_profesion = conteo_profesiones.sum(axis=1)

# Calcular los porcentajes
porcentajes_profesiones = conteo_profesiones.divide(total_por_profesion, axis=0) * 100

# Crear el gráfico de barras apiladas con colores personalizados
fig = px.bar(
    porcentajes_profesiones,
    x=porcentajes_profesiones.index,
    y=porcentajes_profesiones.columns,
    labels={'y': 'Porcentaje de personas'},
    title='Porcentaje de personas con cada tipo de trastorno del sueño por profesión',
    category_orders={'x': porcentajes_profesiones.index[::-1]},
    height=600,
    color_discrete_map=colors,
)

# Ajustar la leyenda
fig.update_layout(legend=dict(title='Sleep Disorder'))

# Mostrar el gráfico
st.plotly_chart(fig)



#CONCLUSIONES:
#LA PROFESIÓN INFLUYE EN LA CALIDAD DEL SUEÑO.
#DOCTOR, NURSE, EMNGINEER Y ACCOUNTANT SON LAS QUE TIENEN MEJOR CALIDAD
#SOFTWARE ENGINEER, SALES REPRE Y CIENTIST LOS QUE PEOR

#LA PROFESIÓN INFLUYE EN LA DURACIÓN DEL SUEÑO 
#LOS QUE MÁS LOS INGENIEROS
#LOS QUE MENOS LOS SALES REPRE


#LA PROFESIÓN INFLUYE EN LOS TRASTORNOS
#Hay profesiones que tienen mas trastornos que otras y diferentes
#Nurse, salesperson y teacher las que mas
#sales repre y scientist las que mas




























