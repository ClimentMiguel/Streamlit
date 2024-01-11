# Importación de librerías
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Carga de datos
df = pd.read_csv(r'sleep.csv')






#TÍTULO: ¿Cómo influye el género en la calidad y duración del sueño?
st.markdown("<p style='color: red; font-size: 24px;'>¿Influye el género en la calidad y duración del sueño?</p>", unsafe_allow_html=True)





####################################################################################################################
#GRÁFICA 0: GRÁFICA CON NÚMERO DE HOMBRES Y NÚMERO DE MUJERES
fig = px.histogram(df, x='Gender', title='Número de hombres y mujeres', labels={'Gender': 'Género'}, color='Gender')
# Eliminar la etiqueta del eje y
fig.update_yaxes(title_text='')
# Mostrar el gráfico en la misma página
st.plotly_chart(fig)
####################################################################################################################











####################################################################################################################
st.markdown('---')
#GRÁFICA 1: CALIDAD DEL SUEÑO POR GÉNERO -> Género no influye en la calidad del sueño
#Título de este apartado
st.markdown("<p style='font-size: 20px;'>Calidad del sueño según género</p>", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.express as px

# Función para generar la gráfica de barras de la calidad del sueño por género
def generar_grafica(df, genero):
    df_filtrado = df[df['Gender'] == genero]
    conteo_calidad_sueno = df_filtrado['Quality of Sleep'].value_counts().reindex(range(11), fill_value=0)

    fig = px.bar(
        x=conteo_calidad_sueno.index,
        y=conteo_calidad_sueno.values,
        labels={'x': 'Calidad de sueño', 'y': 'Cantidad'},
        title=f'Calidad de sueño ({genero})',
        category_orders={'x': list(range(11))}
    )

    return fig

# Estado de los checkboxes
estado_del_checkbox_femenino = st.checkbox("Femenino", value=False)
estado_del_checkbox_masculino = st.checkbox("Masculino", value=False)
estado_del_checkbox_comparacion = st.checkbox("Comparación entre ambos géneros", value=False)

# Verificar si los checkboxes están marcados y mostrar las gráficas correspondientes
if estado_del_checkbox_comparacion:
    # Generar la gráfica de barras comparativa entre ambos géneros
    df_mujeres = df[df['Gender'] == 'Female']
    df_hombres = df[df['Gender'] == 'Male']

    # Calcular la frecuencia de cada nivel para mujeres y hombres
    conteo_calidad_sueno_mujeres = df_mujeres['Quality of Sleep'].value_counts().reindex(range(11), fill_value=0)
    conteo_calidad_sueno_hombres = df_hombres['Quality of Sleep'].value_counts().reindex(range(11), fill_value=0)

    # Crear la gráfica de barras comparativa entre mujeres y hombres
    fig_comparacion = px.bar(
        x=range(11),
        y=[conteo_calidad_sueno_mujeres.values, conteo_calidad_sueno_hombres.values],
        title='Comparación de la calidad del sueño entre géneros',
        labels={'x': 'Nivel de calidad de sueño', 'y': 'Cantidad'},
        color_discrete_sequence=['purple', 'blue'],
        barmode='group',  # Agrupa las barras del mismo valor de x
        category_orders={'x': list(range(11))}  # Especificar el orden de los niveles de calidad del sueño
    )

    # Actualizar las etiquetas de la leyenda
    fig_comparacion.data[0].name = 'Female'
    fig_comparacion.data[1].name = 'Male'

    # Mostrar la gráfica de comparación
    st.plotly_chart(fig_comparacion)

# Verificar si los checkboxes individuales están marcados y mostrar las gráficas correspondientes
if estado_del_checkbox_femenino:
    fig_femenino = generar_grafica(df, 'Female')
    # Mostrar la gráfica de mujeres
    st.plotly_chart(fig_femenino)

if estado_del_checkbox_masculino:
    fig_masculino = generar_grafica(df, 'Male')
    # Mostrar la gráfica de hombres
    st.plotly_chart(fig_masculino)
####################################################################################################################













####################################################################################################################
st.markdown('---')
#GRÁFICA 2: DURACIÓN DEL SUEÑO POR GÉNERO -> Género no influye en la duración del sueño
#Título de este apartado
st.markdown("<p style='font-size: 20px;'>Duración del sueño según género</p>", unsafe_allow_html=True)

# Calcular la media de horas que duermen hombres y mujeres
media_sueno_por_genero = df.groupby('Gender')['Sleep Duration'].mean().reset_index()

# Crear el gráfico de barras
fig = px.bar(
    media_sueno_por_genero, x='Gender', y='Sleep Duration',
    title='Media de horas de sueño por género',
    labels={'x': 'Género', 'y': 'Media de Horas de Sueño'}
)

# Establecer los límites del eje Y
fig.update_layout(yaxis=dict(range=[0, 10]))

# Mostrar el gráfico
st.plotly_chart(fig)
























st.markdown('---')
####################################################################################################################
#GRÁFICA 3:TRASTORNOS DEL SUEÑO POR GÉNERO

#TÍTULO: ¿Influye el género en los trastornos del sueño?
st.markdown("<p style='color: red; font-size: 24px;'>¿Influye el género en los trastornos del sueño?</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 20px;'>Trastronos del sueño según género</p>", unsafe_allow_html=True)
# Función para generar la gráfica de barras de la calidad del sueño por género
def generar_grafica(df, genero):
    df_filtrado = df[df['Gender'] == genero]
    conteo_trastornos_sueno = df_filtrado['Sleep Disorder'].value_counts().reindex(['None', 'Sleep Apnea', 'Insomnia'], fill_value=0)

    fig = px.bar(
        x=conteo_trastornos_sueno.index,
        y=conteo_trastornos_sueno.values,
        labels={'x': 'Trastorno del sueño', 'y': 'Cantidad'},
        title=f'Trastornos del sueño ({genero})',
    )

    return fig

# Estado de los checkboxes
# Añade un sufijo único a cada clave para evitar duplicados
def make_unique_key(base_key, suffix):
    return f"{base_key} {suffix}"

# Estado de los checkboxes
estado_del_checkbox_femenino = st.checkbox(make_unique_key("Femenino  ", ""), value=False)
estado_del_checkbox_masculino = st.checkbox(make_unique_key("Masculino", ""), value=False)
estado_del_checkbox_comparacion = st.checkbox(make_unique_key("Comparación entre ambos géneros", ""), value=False)

# Verificar si los checkboxes están marcados y mostrar las gráficas correspondientes
if estado_del_checkbox_comparacion:
    # Generar la gráfica de barras comparativa entre ambos géneros
    df_mujeres = df[df['Gender'] == 'Female']
    df_hombres = df[df['Gender'] == 'Male']

    # Calcular la frecuencia de cada trastorno para mujeres y hombres
    conteo_trastornos_mujeres = df_mujeres['Sleep Disorder'].value_counts().reindex(['None', 'Sleep Apnea', 'Insomnia'], fill_value=0)
    conteo_trastornos_hombres = df_hombres['Sleep Disorder'].value_counts().reindex(['None', 'Sleep Apnea', 'Insomnia'], fill_value=0)

    # Crear la gráfica de barras comparativa entre mujeres y hombres
    fig_comparacion = px.bar(
        x=['None', 'Sleep Apnea', 'Insomnia'],
        y=[conteo_trastornos_mujeres.values, conteo_trastornos_hombres.values],
        title='Comparación de los trastornos del sueño entre géneros',
        labels={'x': 'Trastorno del sueño', 'y': 'Cantidad'},
        color_discrete_sequence=['purple', 'blue'],
        barmode='group',  # Agrupa las barras del mismo valor de x
    )

    # Actualizar las etiquetas de la leyenda
    fig_comparacion.data[0].name = 'Female'
    fig_comparacion.data[1].name = 'Male'

    # Mostrar la gráfica de comparación
    st.plotly_chart(fig_comparacion)

# Verificar si los checkboxes individuales están marcados y mostrar las gráficas correspondientes
if estado_del_checkbox_femenino:
    fig_femenino = generar_grafica(df, 'Female')
    # Mostrar la gráfica de mujeres
    st.plotly_chart(fig_femenino)

if estado_del_checkbox_masculino:
    fig_masculino = generar_grafica(df, 'Male')
    # Mostrar la gráfica de hombres
    st.plotly_chart(fig_masculino)





#CONCLUSIONES INFLUENCIA DEL GÉNERO EN LA CALIDAD, DURACIÓN Y TRASTORNOS:
#NO INFLUYE EN LA CALIDAD NI EN LA DURACIÓN.
#SÍ INFLUYE EN LOS TRASTORNOS:
#LOS HOMBRES TIENEN MENOS TRASTRONOS DEL SUEÑO
#TIENEN EL MISMO INSOMNIO QUE LAS MUJERES
#LAS MUJERES MUCHA MÁS SLEEP APNEA


















st.markdown('---')
#TÍTULO: ¿INFLUYE LA EDAD DUR Y CAL?
st.markdown("<p style='color: red; font-size: 24px;'>¿Influye la edad en la calidad y duración del sueño?</p>", unsafe_allow_html=True)

#GRÁFICA 4: EDAD Y CALIDAD 
st.markdown("<p style='font-size: 20px;'>Calidad del sueño según la edad</p>", unsafe_allow_html=True)

media_calidad_sueno_por_edad = df.groupby('Age')['Quality of Sleep'].mean().reset_index()

# Crear el gráfico de líneas
fig = px.line(
    media_calidad_sueno_por_edad, x='Age', y='Quality of Sleep',
    title='Media de calidad del sueño según la edad',
    labels={'x': 'Edad', 'y': 'Media de Calidad del Sueño'}
)

# Mostrar el gráfico
st.plotly_chart(fig)






st.markdown('---')
#######################################################################################################
#GRÁFICA 5: EDAD Y DURACIÓN
# Calcular la media de la duración del sueño por edad
st.markdown("<p style='font-size: 20px;'>Duración del sueño según la edad</p>", unsafe_allow_html=True)
media_duracion_sueno_por_edad = df.groupby('Age')['Sleep Duration'].mean().reset_index()

# Crear el gráfico de líneas
fig = px.line(
    media_duracion_sueno_por_edad, x='Age', y='Sleep Duration',
    title='Media de la duración del sueño según la edad',
    labels={'x': 'Edad', 'y': 'Media de Duración del Sueño'}
)

# Mostrar el gráfico
st.plotly_chart(fig)












st.markdown('---')
#######################################################################################################
#GRÁFICA 5: CALIDAD, EDAD Y DURACIÓN
st.markdown("<p style='font-size: 20px;'>Calidad y duración del sueño según la edad</p>", unsafe_allow_html=True)
media_por_edad = df.groupby('Age').mean().reset_index()

# Crear gráfico de líneas conjunto
fig = px.line(
    media_por_edad, x='Age', y=['Quality of Sleep', 'Sleep Duration'],
    title='Relación entre la edad y la calidad y duración del sueño',
    labels={'Age': 'Edad', 'value': 'Valor Medio'},
    color_discrete_map={'Quality of Sleep': 'blue', 'Sleep Duration': 'green'}
)

# Mostrar el gráfico
st.plotly_chart(fig)













st.markdown('---')
#######################################################################################################
#GRÁFICA 5: EDAD Y TRASTORNOS DEL SUEÑO
st.markdown("<p style='color: red; font-size: 24px;'>¿Influye la edad en los trastornos del sueño?</p>", unsafe_allow_html=True)
# Categorizar las edades en grupos

# Categorizar las edades en grupos
bins = [27, 34, 40, 45, 50, 54, 59]
labels = ['27-34', '35-40', '41-45', '46-50', '51-54', '55-59']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Contar el número de personas con cada Sleep Disorder por grupo de edad
conteo_por_grupo = df.groupby(['Age Group', 'Sleep Disorder']).size().reset_index(name='Count')

# Definir colores personalizados
colors = {'None': 'grey', 'Sleep Apnea': 'lightblue', 'Insomnia': 'blue'}  # Cambiar 'lightblue' al color actual de 'None'

# Crear gráfico de barras
fig = px.bar(
    conteo_por_grupo, x='Age Group', y='Count', color='Sleep Disorder',
    title='Número de personas con trastorno del sueño por grupo de edad',
    labels={'Age Group': 'Grupo de Edad', 'Count': 'Número de Personas'},
    color_discrete_map=colors
)

# Mostrar el gráfico
st.plotly_chart(fig)#################################################################################



#CONCLUSIONES INFLUENCIA DE LA EDAD EN LA CALIDAD, DURACIÓN Y TRASTORNOS DEL SUEÑO
#La edad influye en la calidad del sueño
#Las personas que peor duermen son las más jovenes
#Las que mejor duermen son las más mayores

#La edad influye en la duración
#Las que menos duermen son las más jovenes
#Las que más duermen ñas más mayores


#La edad influye en el desarrollo de trastronos del sueño
#Las personas más jovenes son las que tienen más trastornos
#Las perosnas mayores las que menos
#Destacar que los de 40 años tienen insomnio
#Los mayores sleep apnea