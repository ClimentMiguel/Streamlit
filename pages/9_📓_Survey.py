import streamlit as st
import streamlit_survey as ss
logged = st.session_state["Logged"]
if logged == True:

    st.header("Sleep Survey")
    survey = ss.StreamlitSurvey("Survey Example")

    age = st.slider("Whats your age?", min_value=0, max_value=100, value=50)

    sex = survey.radio("Specify your sex: ", options=["Female", "Male"], horizontal=True)

    bmi = survey.radio("Select your BMI category: ", options=["Normal", "Overweight", "Obese"], horizontal=True)

    stress = st.slider("From 1-10, how would you define your stress levels (being 10 the highest stress)", min_value=1, max_value=10, value=5)
else:
    st.header("You must be logged in to participate in the survey!")
