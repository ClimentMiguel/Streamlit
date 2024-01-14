import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.set_page_config(page_title="Introduction")

df = pd.read_csv('DATABASE RAW.csv')

def introduccion_datos():
    texto_intro = """
    ****

    En el presente análisis, examinaremos una base de datos que captura información crucial sobre la salud y los hábitos de sueño de individuos pertenecientes a diversas ocupaciones y rangos de edad. 
    Consta de 374 registros que incluyen datos demográficos, niveles de actividad física, calidad del sueño y otros parámetros relevantes.

   
    Adentrémonos en el estudio de esta información detallada para extraer conclusiones significativas que puedan contribuir a una comprensión más profunda de la relación entre la ocupación, los hábitos de sueño y la salud en esta población específica.
    """

    return texto_intro

# Datos para las opciones del radio botón y sus descripciones
datos_descripciones = {
    'Person ID': 'Identificador único para cada individuo.',
    'Género': 'Género de la persona (Masculino/Femenino).',
    'Edad': 'Edad de la persona en años.',
    'Ocupación': 'Ocupación o profesión de la persona.',
    'Duración del Sueño (horas)': 'Número de horas que la persona duerme por día.',
    'Calidad del Sueño (escala: 1-10)': 'Calificación subjetiva de la calidad del sueño, en una escala del 1 al 10.',
    'Nivel de Actividad Física (minutos/día)': 'Número de minutos que la persona se involucra en actividad física diariamente.',
    'Nivel de Estrés (escala: 1-10)': 'Calificación subjetiva del nivel de estrés experimentado por la persona, en una escala del 1 al 10.',
    'Categoría de BMI': 'Categoría de BMI de la persona (por ejemplo, Bajo peso, Normal, Sobrepeso).',
    'Presión Arterial (sistólica/diastólica)': 'Medición de la presión arterial de la persona, indicada como presión sistólica sobre presión diastólica.',
    'Ritmo Cardíaco (ppm)': 'Ritmo cardíaco en reposo de la persona en pulsaciones por minuto.',
    'Pasos Diarios': 'Número de pasos que la persona da por día.',
    'Trastorno del Sueño': 'Presencia o ausencia de un trastorno del sueño en la persona (Ninguno, Insomnio, Apnea del sueño).'
}

def mostrar_descripcion(opcion_seleccionada):
    st.subheader(opcion_seleccionada)
    st.write(datos_descripciones[opcion_seleccionada])
    
    
def show_questions_for_hypothesis():
    # Título para el planteamiento
    st.title("Planteamiento ")

    # Definir preguntas e hipótesis con sus preguntas asociadas
    preguntas_hipotesis = {
        "Como influencian las distintas variables en la duración del sueño": [
            "¿Cómo afecta la ocupación de una persona a la duración de su sueño?",
            "¿Existe una relación entre la actividad física y la duración del sueño?",
            "¿El nivel de estrés influye en la duración del sueño?",
            "¿Hay diferencias significativas en la duración del sueño entre personas con diferentes categorías de IMC?"
        ],
        "Como influencian distintas variables personales en la calidad del sueño": [
            "¿Cómo la ocupación de una persona influye en la calidad de su sueño?",
            "¿La actividad física regular se relaciona con una mejor calidad del sueño?",
            "¿El nivel de estrés afecta la percepción subjetiva de la calidad del sueño?"
        ],
        "Comno influencian distintas variables personales en el tipo de enfermedad del sueño": [
            "¿Cómo la ocupación de una persona influye en el tipo de enfermedad del sueño?",
            "¿La actividad física o el nivel de estrés están asociados con trastornos específicos del sueño?",
            "¿Hay diferencias en la presencia de trastornos del sueño entre personas con diferentes categorías de IMC?"
        ],
        "Como las características del sueño influencian en distintas variables personales": [
            "¿Cómo la duración del sueño se relaciona con otras características del sueño?",
            "¿La calidad del sueño afecta la actividad física diaria de una persona?",
            "¿Personas con ciertos trastornos del sueño tienen diferencias en el nivel de estrés o categoría de IMC?"
        ]
    }

    # Crear una lista con las hipótesis
    hipotesis = list(preguntas_hipotesis.keys())

    # Seleccionar hipótesis usando un widget de Streamlit
    selected_hypothesis = st.selectbox("Selecciona un Planteamiento:", hipotesis)

    # Mostrar las preguntas asociadas a la hipótesis seleccionada
    if selected_hypothesis in preguntas_hipotesis:
        st.header(f"{selected_hypothesis} ")
        for pregunta in preguntas_hipotesis[selected_hypothesis]:
            st.info(pregunta)
    else:
        st.warning("¡Selecciona una hipótesis para ver las preguntas asociadas!")

    
# Function to get gender distribution
def gender_distribution():
    gender_counts = df['Gender'].value_counts()
    return gender_counts

# Sección 1: Distribución de Género
def distribucion_genero():
    st.title("Distribución de Género en el Conjunto de Datos")
    
    # Mostrar distribución de género
    st.write("Recuento de Género:")
    st.write(gender_distribution())

# Sección 2: Estadísticas de Edad
def estadisticas_edad():
    st.title("Estadísticas de Edad en el Conjunto de Datos")
    
    # Calcular estadísticas de edad
    max_edad = max(df['Age'])
    min_edad = min(df['Age'])
    media_edad = sum(df['Age']) / len(df['Age'])

    # Mostrar resultados de edad
    st.write(f"Edad Máxima: {max_edad} años")
    st.write(f"Edad Mínima: {min_edad} años")
    st.write(f"Edad Media: {media_edad:.2f} años")  # Formatear la media con dos decimales

    # Gráfico de distribución de edad
    st.title("Distribución de Edad")
    fig, ax = plt.subplots()
    sns.histplot(df['Age'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

# Sección 3: Numero de Ocupaciones
def numero_ocupaciones():
    # Contar las ocupaciones
    occupations_counts = df['Occupation'].value_counts()

    # Mostrar cuadro de selección con las ocupaciones
    st.title("Numero de Ocupaciones")
    selected_occupation = st.selectbox("Selecciona una ocupación", occupations_counts.index)

    # Mostrar la cuenta de la ocupación seleccionada
    st.write(f"Cuenta de {selected_occupation}: {occupations_counts[selected_occupation]}")

    # Gráfico de distribución de ocupaciones
    st.title("Distribución de Ocupaciones")
    fig, ax = plt.subplots()
    sns.countplot(y=df['Occupation'], ax=ax)
    st.pyplot(fig)

# Sección 4: Matriz de Correlación
def matriz_correlacion():
    # Crear un nuevo DataFrame con las variables numéricas y la conversión de 'BMI Category' a una variable numérica
    selected_columns = ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level', 'BMI Category', 'Heart Rate', 'Daily Steps']
    selected_data = df[selected_columns].copy()

    # Convertir 'BMI Category' en una variable numérica
    bmi_mapping = {'Normal Weight': 0, 'Normal': 1, 'Overweight': 2, 'Obese': 3}
    selected_data['BMI Category'] = selected_data['BMI Category'].map(bmi_mapping)

    # Calculando la matriz de correlación para las columnas seleccionadas
    selected_correlation_matrix = selected_data.corr()

    # Visualización de la matriz de correlación
    st.title("Matriz de Correlación para Variables Seleccionadas")
    st.write(selected_correlation_matrix)

    # Gráfico de heatmap
    st.title("Heatmap de la Matriz de Correlación")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(selected_correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5, ax=ax)
    st.pyplot(fig)

# Sección 5: Codificación de 'Gender' y Agrupación de Datos por 'Sleep Disorder'
def codificacion_y_agrupacion():
   #Convertir la variable "blood pressure" en 2

    # Dividiendo la columna 'Blood Pressure' en dos columnas: 'Systolic BP' y 'Diastolic BP'
    df[['Systolic BP', 'Diastolic BP']] = df['Blood Pressure'].str.split('/', expand=True).astype(int)

    df.head() #Convertir la variable "blood pressure" en 2

    # Dividiendo la columna 'Blood Pressure' en dos columnas: 'Systolic BP' y 'Diastolic BP'
    df[['Systolic BP', 'Diastolic BP']] = df['Blood Pressure'].str.split('/', expand=True).astype(int)
 
    
    # Reemplazando NaN por 'None' en la columna 'Sleep Disorder'
    df['Sleep Disorder'].fillna('None', inplace=True)

    # Verificando si la sustitución se realizó correctamente
    nan_check = df['Sleep Disorder'].isnull().sum()
    nan_check
    # Codificación de la variable 'Gender'
    df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1}) # 0 para Male y 1 para Female

    # Agrupando los datos por 'Sleep Disorder'
    grouped_data = df.groupby('Sleep Disorder').agg({
        'Age': pd.Series.mode,
        'Gender': lambda x: (1 - x.mean()) * 100, # Porcentaje de hombres, 
        'Stress Level': 'mean',
        'Physical Activity Level': 'mean',
        'Occupation': lambda x: x.value_counts(normalize=True) * 100, # Porcentaje de cada ocupación
        'Heart Rate': 'mean',
        'Systolic BP': 'mean',
        'Diastolic BP': 'mean'
    })

    # Reorganizando para una mejor visualización
    grouped_data = grouped_data.rename(columns={'Age': 'Most Common Age', 'Gender': '% Men', 'Stress Level': 'Average Stress Level',
    'Physical Activity Level': 'Average Physical Activity Level', 'Heart Rate': 'Average Heart Rate', 
    'Systolic BP': 'Average Systolic BP', 'Diastolic BP': 'Average Diastolic BP'})

    st.title("Codificación de 'Genero' y Agrupación de Datos por 'Desordenes de Sueño'")
    st.write(grouped_data.T)  # Transponiendo para una mejor visualización

# Sección 6: Gráficos para Sleep Disorders
def graficos_sleep_disorders(df):
    # Agrupar los datos antes de llamar a la función
    grouped_data = df.groupby('Sleep Disorder').agg({
        'Age': lambda x: x.mode().iloc[0],
        'Gender': lambda x: (1 - x.mean()) * 100,
        'Stress Level': 'mean',
        'Physical Activity Level': 'mean',
        'Occupation': lambda x: x.value_counts(normalize=True) * 100,
        'Heart Rate': 'mean',
        'Systolic BP': 'mean',
        'Diastolic BP': 'mean'
    })

    sleep_disorders = ['None', 'Insomnia', 'Sleep Apnea']
    metrics = ['Age', 'Gender', 'Stress Level', 
               'Physical Activity Level', 'Occupation', 
               'Heart Rate', 'Systolic BP', 'Diastolic BP']

    # Creación de una lista de DataFrames, uno para cada métrica
    dfs = []
    for metric in metrics:
        temp_df = grouped_data[metric].reset_index()
        temp_df.rename(columns={metric: 'Value'}, inplace=True)
        temp_df['Metric'] = metric
        dfs.append(temp_df)

    # Combinando todos los DataFrames en uno para la visualización
    combined_df = pd.concat(dfs)

    # Creando los gráficos
    st.title("Gráficos para Desordenes de Sueño")
    for metric in metrics:
        st.subheader(metric)
        fig, ax = plt.subplots(figsize=(10, 6))

        # Convertir NumPy arrays a listas directamente en el DataFrame
        metric_data = combined_df[combined_df['Metric'] == metric].copy()
        metric_data['Sleep Disorder'] = metric_data['Sleep Disorder'].astype(str)
        
        # Convertir numpy.ndarray a listas
        metric_data['Value'] = metric_data['Value'].apply(lambda x: x[0] if isinstance(x, np.ndarray) else x)

        sns.barplot(x='Sleep Disorder', y='Value', hue='Metric', data=metric_data, ax=ax)
        plt.title(metric)
        plt.xticks(rotation=45)
        st.pyplot(fig)


   
# Sección 9: Gráficos de sectores para ocupaciones por trastorno del sueño
def pie_charts_occupations_by_disorder(df):
    st.title("Gráficos de Sectores: Ocupaciones por Trastorno del Sueño")

    # Agrupar los datos por 'Sleep Disorder' para la métrica de ocupaciones
    grouped_occupation_data = df.groupby('Sleep Disorder')['Occupation'].value_counts(normalize=True).unstack(fill_value=0) * 100

    # Crear gráficos de sectores para las ocupaciones en cada trastorno del sueño
    for disorder in grouped_occupation_data.index:
        st.subheader(f"Occupations for {disorder}")
        fig, ax = plt.subplots(figsize=(10, 6))
        grouped_occupation_data.loc[disorder].plot(kind='pie', autopct='%1.1f%%', ax=ax)
        plt.title(f"Occupations for {disorder}")
        plt.ylabel('')
        st.pyplot(fig)


# Sección 8: Creación de la aplicación
def main():
    st.title("Análisis de Datos de Salud y Hábitos de Sueño")
    
    # Mostrar la introducción
    st.write(introduccion_datos())
    
    st.title("Descripciones de Datos")

    # Radio botón para seleccionar opciones
    opcion_seleccionada = st.radio("Selecciona una opción:", list(datos_descripciones.keys()))

    # Mostrar descripción basada en la opción seleccionada
    mostrar_descripcion(opcion_seleccionada)
    
    show_questions_for_hypothesis()
    
    # Llamadas a las funciones para cada sección
    distribucion_genero()
    estadisticas_edad()
    numero_ocupaciones()
    matriz_correlacion()
    #codificacion_y_agrupacion()
    # Llamar a la función graficos_sleep_disorders y pasar df como argumento
    #graficos_sleep_disorders(df)
       
    # Llamada a la función pie_charts_occupations_by_disorder en main()
    #pie_charts_occupations_by_disorder(df)
  
  
if __name__ == "__main__":
    main()