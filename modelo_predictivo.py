import pandas as pd

# Cargar el archivo CSV
file_path = './DATABASE RAW.csv'
data = pd.read_csv(file_path)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import numpy as np
import random

# Seleccionando las columnas relevantes y codificando las variables categóricas
features = data[['Age', 'BMI Category', 'Stress Level', 'Sleep Duration', 'Gender']]
features['BMI Category'] = LabelEncoder().fit_transform(features['BMI Category'])
features['Gender'] = LabelEncoder().fit_transform(features['Gender'])
le = LabelEncoder()
le.fit(["Insomnia","Sleep apnea","None"])
target = LabelEncoder().fit_transform(data['Sleep Disorder'])

# Dividiendo los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

# Escalando las variables de características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Creando y entrenando el modelo

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Definiendo una función para hacer la predicción con la condición especial
def predict_with_condition(age, height, weight, sleep_duration, stress_level, gender):
    # Calcular el BMI
    bmi = weight / (height ** 2)

    # Codificar el género
    gender_encoded = 0 if gender.lower() == "femenino" else 1

    # Si las horas de sueño son más o igual de 6, predecir "ningún trastorno"
    if sleep_duration >= 6:
        return "None"

    # De lo contrario, usar el modelo para predecir
    else:
        # Preparar los datos para la predicción
        input_data = np.array([[age, bmi, stress_level, sleep_duration, gender_encoded]])
        input_data_scaled = scaler.transform(input_data)

        # Realizar la predicción
        prediction = model.predict(input_data_scaled)
        # Decodificar la predicción
        return le.inverse_transform([prediction[0]])

# Probar la función con un conjunto de datos de prueba
#test_age = 55
#test_height = 1.60
#test_weight = 60
#test_sleep_duration = 6
#test_stress_level = 1
#test_gender = "Masculino"

#predict_with_condition(test_age, test_height, test_weight, test_sleep_duration, test_stress_level, test_gender)