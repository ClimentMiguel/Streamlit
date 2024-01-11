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
# Calcular la media de duración del sueño por profesión
# Calcular la media de duración del sueño por profesión
# Calcular la media de duración del sueño por profesión




# Suponiendo que ya tienes media_duracion calculado
media_duracion = df.groupby('Occupation')['Sleep Duration'].mean().reset_index()

# Gráfico de dispersión para calidad del sueño
fig = px.scatter(df, x='Occupation', y='Quality of Sleep', size='Quality of Sleep',
                 title='Calidad del Sueño por Profesión',
                 labels={'Quality of Sleep': 'Calidad del Sueño', 'Occupation': 'Profesión'},
                 size_max=30)

# Añadir puntos para la media de duración del sueño
fig.add_trace(go.Scatter(x=media_duracion['Occupation'], y=media_duracion['Sleep Duration'],
                         mode='markers', marker=dict(size=10, symbol='circle', color='red'), 
                         name='Media de Duración'))

# Mostrar el gráfico
st.plotly_chart(fig)
####################################################################################################################















st.markdown("<p style='color: green; font-size: 24px;'>¿Influye la profesión en el desarrollo de trastornos del sueño?</p>", unsafe_allow_html=True)
####################################################################################################################
#GRÁFICA 2: TRASTORNO DEL SUEÑO POR PROFESIÓN

# Obtener la lista única de profesiones
profesiones = df['Occupation'].unique()

# Añadir un selectbox con las opciones de profesiones
opcion_seleccionada = st.selectbox('Selecciona una profesión', profesiones)

# Filtrar el DataFrame según la profesión seleccionada
df_profesion = df[df['Occupation'] == opcion_seleccionada]

# Contar la frecuencia de cada tipo de Sleep Disorder
conteo_sleep_disorder = df_profesion['Sleep Disorder'].value_counts()

# Definir colores personalizados
colors_pie = {'None': 'grey', 'Sleep Apnea': 'Green', 'Insomnia': 'Light green'}

# Crear un gráfico de tarta con Plotly Express y colores personalizados
fig = px.pie(conteo_sleep_disorder, values=conteo_sleep_disorder.values, names=conteo_sleep_disorder.index,
             title=f'Proporción de Sleep Disorder para {opcion_seleccionada}')

# Cambiar colores usando el parámetro template
fig.update_traces(marker=dict(colors=[colors_pie[disorder] for disorder in conteo_sleep_disorder.index]))

# Mostrar el gráfico de tarta
st.plotly_chart(fig)













st.markdown('---')
#GRÁFICA 3: TRASTORNO DEL SUEÑO POR PROFESIÓN



colors = {'None': 'grey', 'Sleep Apnea': 'Green', 'Insomnia': 'Light green'}

conteo_profesiones = pd.crosstab(index=df['Occupation'], columns=df['Sleep Disorder'])

# Reorganizar las columnas para poner 'None' al final
conteo_profesiones = conteo_profesiones[['Sleep Apnea', 'Insomnia', 'None']]

# Crear el gráfico de barras apiladas con colores personalizados
fig = px.bar(conteo_profesiones, x=conteo_profesiones.index,
             y=conteo_profesiones.columns,
             labels={'y': 'Número de personas'},
             title='Número de personas con cada tipo de trastorno del sueño por profesión',
             category_orders={'x': conteo_profesiones.index[::-1]},
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




























