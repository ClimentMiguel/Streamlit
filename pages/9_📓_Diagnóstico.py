import streamlit as st
import streamlit_survey as ss
import modelo_predictivo as mp

logged = st.session_state["Logged"]
if logged == True:

    st.header("Diagnóstico de sueño")
    survey = ss.StreamlitSurvey("Survey")

    age = st.slider("¿Cual es su edad?", min_value=0, max_value=100, value=50)

    height = st.number_input("Insertar altura en cm:", min_value=0, max_value=300, value=150)

    weight = st.number_input("Insertar peso en kg:", min_value=0, max_value=300, value=70)

    sleep = st.number_input("Cuantas horas de sueño sueles dormir al día?:", min_value=0, max_value=24, value=8)

    stress = st.slider("Del 1 al 10, como definirias tu nivel de estrés (siendo 10 el más alto)?", min_value=1, max_value=10, value=5)

    sex = survey.radio("Especifica tu sexo: ", options=["Femenino", "Masculino"], horizontal=True)

    prediction = mp.predict_with_condition(age,height,weight,sleep,stress, sex)
    if prediction == "Sleep apnea":
        st.header("¡Podrías tener apnea del sueño!")
    elif prediction == "Insomnia":
        st.header("¡Podrías tener insomnio!")
    elif prediction == "None":
        st.header("Lo más posible es que no padezcas de ningún trastorno de sueño =)")

    st.image("./Sleep diagnosis.jpeg")

else:
    st.header("¡Debes estar loggeado para participar en el diagnóstico! >=(")
