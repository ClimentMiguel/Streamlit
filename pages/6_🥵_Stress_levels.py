import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = './DATABASE RAW.csv'
data = pd.read_csv(file_path)
data['Sleep Disorder'].fillna('None', inplace=True)

#categorical_counts = data.select_dtypes(include=['object']).nunique()

#unique_values_categorical = {column: data[column].unique() for column in data.select_dtypes(include=['object']).columns}
st.title("Efecto del estrés en el sueño")
st.subheader("Duración del sueño")
fig =plt.figure(figsize=(12, 8))
sns.scatterplot(data=data, x="Sleep Duration", y="Quality of Sleep", size="Stress Level", 
                sizes=(20, 700), alpha=0.7, marker="o", edgecolor="black")
plt.title("Relación entre Duración del Sueño, Calidad del Sueño y Nivel de Estrés")
plt.xlabel("Duración del Sueño (horas)")
plt.ylabel("Calidad del Sueño")
plt.legend(title="Nivel de Estrés")
st.pyplot(fig)

st.subheader("Calidad del sueño")


# Categorización de la duración del sueño y la calidad del sueño
# Se pueden ajustar los rangos según sea necesario
data['Sleep Duration Category'] = pd.cut(data['Sleep Duration'], 
                                         bins=[0, 6, 8, 24], 
                                         labels=['Short (<7h)', 'Medium (7h)', 'Long (>8h)'])

data['Quality of Sleep Category'] = pd.cut(data['Quality of Sleep'], 
                                           bins=[0, 3, 6, 10], 
                                           labels=['Low (<6)', 'Medium (6-8)', 'High (9-10)'])

# Gráfico de violín para Calidad del Sueño vs Nivel de Estrés
fig2 = plt.figure(figsize=(12, 6))
sns.violinplot(data=data, x='Quality of Sleep Category', y='Stress Level')
plt.title('Distribución del Nivel de Estrés por Categoría de Calidad del Sueño - Gráfico de Violín')
plt.xlabel('Categoría de Calidad del Sueño')
plt.ylabel('Nivel de Estrés')
plt.show()

st.pyplot(fig2)

st.subheader("Trastornos del sueño")

# Calculating the median stress level for each type of sleep disorder
stress_sleep_disorder_median = data.groupby('Sleep Disorder')['Stress Level'].median().sort_values()

# Creating a bar plot with the median values
fig3 = plt.figure(figsize=(10, 6))
stress_sleep_disorder_median.plot(kind='barh', color='lightcoral')

# Adding plot title and labels
plt.title('Median Stress Level for Each Type of Sleep Disorder')
plt.xlabel('Median Stress Level')
plt.ylabel('Type of Sleep Disorder')

# Displaying the plot
plt.show()

st.pyplot(fig3)
