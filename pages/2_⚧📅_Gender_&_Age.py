



# Importación de librerías
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Carga de datos
df = pd.read_csv('DATABASE RAW.csv')

df["Sleep Disorder"]  = df["Sleep Disorder"].fillna(value="None")

st.title("Efectos del género y la edad en el sueño")


#TÍTULO: ¿Cómo influye el género en la calidad y duración del sueño?
st.markdown("<p style='color: brown; font-size: 24px;'>¿Influye el género en la calidad y duración del sueño?</p>", unsafe_allow_html=True)





####################################################################################################################
#GRÁFICA 0: GRÁFICA CON NÚMERO DE HOMBRES Y NÚMERO DE MUJERES
fig = px.histogram(df, x='Gender', title='Número de hombres y mujeres', labels={'Gender': 'Género'}, color='Gender',
                   color_discrete_map={'Male': 'brown', 'Female': 'burlywood'})

# Eliminar la etiqueta del eje y
fig.update_yaxes(title_text='')

# Mostrar el gráfico en la misma página
st.plotly_chart(fig)
####################################################################################################################











####################################################################################################################
st.markdown('---')
#GRÁFICA 1: CALIDAD DEL SUEÑO POR GÉNERO -> Género no influye en la calidad del sueño
#Título de este apartado
st.markdown("<p style='color: brown; font-size: 20px;'>Calidad del sueño</p>", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.express as px

# Assuming you have a DataFrame named df

# Función para generar la gráfica de barras de la calidad del sueño por género
def generar_grafica(df, genero, color_barras):
    df_filtrado = df[df['Gender'] == genero]
    conteo_calidad_sueno = df_filtrado['Quality of Sleep'].value_counts().reindex(range(11), fill_value=0)

    total = conteo_calidad_sueno.sum()
    porcentajes = (conteo_calidad_sueno / total) * 100

    fig = px.bar(
        x=porcentajes.index,
        y=porcentajes.values,
        labels={'x': 'Calidad de sueño', 'y': 'Porcentaje'},
        title=f'Calidad de sueño ({genero}) - Porcentaje',
        category_orders={'x': list(range(11))},
        color_discrete_sequence=[color_barras] * len(porcentajes)  # Establecer el color de las barras
    )

    return fig

# Opciones de botones de radio
opciones_genero = ['Femenino', 'Masculino', 'Comparación entre ambos géneros']
opcion_seleccionada = st.radio("Seleccione una opción", opciones_genero)

# Colores deseados
color_marron = 'brown'
color_marron_claro = 'burlywood'

# Verificar la opción seleccionada y mostrar las gráficas correspondientes
if opcion_seleccionada == 'Comparación entre ambos géneros':
    df_mujeres = df[df['Gender'] == 'Female']
    df_hombres = df[df['Gender'] == 'Male']
    
    conteo_calidad_sueno_mujeres = df_mujeres['Quality of Sleep'].value_counts().reindex(range(11), fill_value=0)
    conteo_calidad_sueno_hombres = df_hombres['Quality of Sleep'].value_counts().reindex(range(11), fill_value=0)

    total_mujeres = conteo_calidad_sueno_mujeres.sum()
    total_hombres = conteo_calidad_sueno_hombres.sum()
    porcentajes_mujeres = (conteo_calidad_sueno_mujeres / total_mujeres) * 100
    porcentajes_hombres = (conteo_calidad_sueno_hombres / total_hombres) * 100

    fig_comparacion = px.bar(
        x=range(11),
        y=[porcentajes_mujeres.values, porcentajes_hombres.values],
        title='Comparación de la calidad del sueño entre géneros - Porcentaje',
        labels={'x': 'Nivel de calidad de sueño', 'y': 'Porcentaje'},
        color_discrete_sequence=[color_marron_claro, color_marron],  # Establecer los colores de las barras
        barmode='group',
        category_orders={'x': list(range(11))}
    )

    fig_comparacion.data[0].name = 'Female'
    fig_comparacion.data[1].name = 'Male'

    st.plotly_chart(fig_comparacion)

else:
    genero_seleccionado = 'Female' if opcion_seleccionada == 'Femenino' else 'Male'
    fig_genero = generar_grafica(df, genero_seleccionado, color_marron_claro if genero_seleccionado == 'Female' else color_marron)
    st.plotly_chart(fig_genero)











####################################################################################################################
































####################################################################################################################
st.markdown('---')
#GRÁFICA 2: DURACIÓN DEL SUEÑO POR GÉNERO -> Género no influye en la duración del sueño
#Título de este apartado
st.markdown("<p style=' color: brown; font-size: 20px;'>Duración del sueño</p>", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.express as px

# Supongamos que ya tienes el DataFrame df

# Calcular la media de horas que duermen hombres y mujeres
media_sueno_por_genero = df.groupby('Gender')['Sleep Duration'].mean().reset_index()

# Crear el gráfico de barras
fig = px.bar(
    media_sueno_por_genero, x='Gender', y='Sleep Duration',
    title='Media de horas de sueño por género',
    labels={'x': 'Género', 'y': 'Media de Horas de Sueño'},
    color='Gender',
    color_discrete_map={'Male': 'brown', 'Female': 'burlywood'}
)

# Establecer los límites del eje Y
fig.update_layout(yaxis=dict(range=[0, 10]))

# Mostrar el gráfico
st.plotly_chart(fig)



####################################################################################################################



































st.markdown('---')
####################################################################################################################
#GRÁFICA 3:TRASTORNOS DEL SUEÑO POR GÉNERO

#TÍTULO: ¿Influye el género en los trastornos del sueño?
st.markdown("<p style='color: brown; font-size: 24px;'>¿Influye el género en los trastornos del sueño?</p>", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.express as px

# Función para generar la gráfica de barras de la calidad del sueño por género
def generar_grafica(df, genero):
    df_filtrado = df[df['Gender'] == genero]
    conteo_trastornos_sueno = df_filtrado['Sleep Disorder'].value_counts().reindex(['None', 'Sleep Apnea', 'Insomnia'], fill_value=0)

    total = conteo_trastornos_sueno.sum()
    porcentajes = (conteo_trastornos_sueno / total) * 100

    fig = px.bar(
        x=porcentajes.index,
        y=porcentajes.values,
        labels={'x': 'Trastorno del sueño', 'y': 'Porcentaje'},
        title=f'Trastornos del sueño ({genero}) - Porcentaje',
        color=porcentajes.index,  # Utiliza los trastornos del sueño como variable de color
        color_discrete_map={'None': 'lightgrey', 'Sleep Apnea': 'brown', 'Insomnia': 'burlywood'}  # Define los colores
    )

    return fig

# Añade un sufijo único a cada clave para evitar duplicados
def make_unique_key(base_key, suffix):
    return f"{base_key} {suffix}"

# Opciones de botones de radio
opciones_genero = ['Femenino', 'Masculino', 'Comparación entre ambos géneros']
opcion_seleccionada = st.radio("Seleccione una opción", opciones_genero, key=make_unique_key("Radio", "Gender"))

# Verificar la opción seleccionada y mostrar las gráficas correspondientes
if opcion_seleccionada == 'Comparación entre ambos géneros':
    # Generar la gráfica de barras comparativa entre ambos géneros
    df_mujeres = df[df['Gender'] == 'Female']
    df_hombres = df[df['Gender'] == 'Male']

    # Calcular la frecuencia de cada trastorno para mujeres y hombres
    conteo_trastornos_mujeres = df_mujeres['Sleep Disorder'].value_counts().reindex(['None', 'Sleep Apnea', 'Insomnia'], fill_value=0)
    conteo_trastornos_hombres = df_hombres['Sleep Disorder'].value_counts().reindex(['None', 'Sleep Apnea', 'Insomnia'], fill_value=0)

    # Calcular porcentajes
    total_mujeres = conteo_trastornos_mujeres.sum()
    total_hombres = conteo_trastornos_hombres.sum()
    porcentajes_mujeres = (conteo_trastornos_mujeres / total_mujeres) * 100
    porcentajes_hombres = (conteo_trastornos_hombres / total_hombres) * 100

    # Crear la gráfica de barras comparativa entre mujeres y hombres
    fig_comparacion = px.bar(
        x=porcentajes_mujeres.index,
        y=[porcentajes_mujeres.values, porcentajes_hombres.values],
        title='Comparación de los trastornos del sueño entre géneros - Porcentaje',
        labels={'x': 'Trastorno del sueño', 'y': 'Porcentaje'},
        color_discrete_sequence=['burlywood', 'brown', 'grey'],  # Define los colores
        barmode='group',  # Agrupa las barras del mismo valor de x
    )

    # Actualizar las etiquetas de la leyenda
    fig_comparacion.data[0].name = 'Female'
    fig_comparacion.data[1].name = 'Male'

    # Mostrar la gráfica de comparación
    st.plotly_chart(fig_comparacion)

else:
    genero_seleccionado = 'Female' if opcion_seleccionada == 'Femenino' else 'Male'
    fig_genero = generar_grafica(df, genero_seleccionado)
    # Mostrar la gráfica del género seleccionado
    st.plotly_chart(fig_genero)







###





#CONCLUSIONES INFLUENCIA DEL GÉNERO EN LA CALIDAD, DURACIÓN Y TRASTORNOS:
#NO INFLUYE EN LA CALIDAD NI EN LA DURACIÓN.
#SÍ INFLUYE EN LOS TRASTORNOS:
#LOS HOMBRES TIENEN MENOS TRASTRONOS DEL SUEÑO
#TIENEN EL MISMO INSOMNIO QUE LAS MUJERES
#LAS MUJERES MUCHA MÁS SLEEP APNEA
######################################################################################################################

































###########################################################
st.markdown('---')
#TÍTULO: ¿INFLUYE LA EDAD DUR Y CAL?
st.markdown("<p style='color: brown; font-size: 24px;'>¿Influye la edad en la calidad y duración del sueño?</p>", unsafe_allow_html=True)

#######################################################################################################
#GRÁFICA 6: CALIDAD, EDAD Y DURACIÓN
bitch= df["Age"].unique().tolist()

avgQuality = [df[df["Age"]== el]["Quality of Sleep"].mean() for el in bitch]
avgDuration = [df[df["Age"]== el]["Sleep Duration"].mean() for el in bitch]
media_por_edad = pd.DataFrame(list(zip(bitch,avgQuality, avgDuration)),
      columns=["Age",'Quality of Sleep','Sleep Duration'])

# Crear gráfico de líneas conjunto
fig = px.line(
    media_por_edad, x='Age', y=['Quality of Sleep', 'Sleep Duration'],
    title='Relación entre la edad y la calidad y duración del sueño',
    labels={'Age': 'Edad', 'value': 'Valor Medio'},
    color_discrete_map={'Quality of Sleep': 'burlywood', 'Sleep Duration': 'brown'}  # Modifica los colores aquí
)

# Mostrar el gráfico
st.plotly_chart(fig)





#######################################################################################################












st.markdown('---')
#######################################################################################################
#GRÁFICA 7: EDAD Y TRASTORNOS DEL SUEÑO
st.markdown("<p style='color: brown; font-size: 24px;'>¿Influye la edad en los trastornos del sueño?</p>", unsafe_allow_html=True)
# Categorizar las edades en grupos



import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Categorizar las edades en grupos
bins = [27, 34, 40, 45, 50, 54, 59]
labels = ['27-34', '35-40', '41-45', '46-50', '51-54', '55-59']
colors = {'None': 'grey', 'Sleep Apnea': 'brown', 'Insomnia': 'burlywood'}

# Aplicar el nuevo orden al DataFrame
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Contar el número de personas con cada Sleep Disorder por grupo de edad
conteo_por_grupo = df.groupby(['Age Group', 'Sleep Disorder']).size().reset_index(name='Count')

# Calcular el total de personas por grupo de edad
total_por_grupo = conteo_por_grupo.groupby('Age Group')['Count'].transform('sum')

# Calcular el porcentaje
conteo_por_grupo['Percentage'] = (conteo_por_grupo['Count'] / total_por_grupo) * 100

# Crear gráfico de barras usando plotly.graph_objects
fig = go.Figure()

for sleep_disorder, color in colors.items():
    subset = conteo_por_grupo[conteo_por_grupo['Sleep Disorder'] == sleep_disorder]
    fig.add_trace(go.Bar(
        x=subset['Age Group'],
        y=subset['Percentage'],
        name=sleep_disorder,
        marker_color=color
    ))

# Actualizar el diseño del gráfico
fig.update_layout(
    title='Porcentaje de personas con trastorno del sueño por grupo de edad',
    xaxis_title='Grupo de Edad',
    yaxis_title='Porcentaje',
    barmode='group'  # Agrupar las barras
)

# Ajustar el rango del eje y
fig.update_yaxes(range=[0, 100])

# Mostrar el gráfico
st.plotly_chart(fig)





