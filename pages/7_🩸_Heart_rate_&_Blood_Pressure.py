import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels

st.set_page_config(page_title="Heart rate & Blood Pressure")

file = pd.read_csv("DATABASE RAW.csv",delimiter=',',encoding="latin-1")

def generate_graph_bp(df, type_1,type_2):
    fig = px.scatter(df, x=type_1, y=[type_2],
                labels={'value': 'Blood Pressure', 'variable': 'Type'},
                trendline="ols")

    return fig

st.title("Effects of sleep on blood pressure & Heartrate")


st.header("Blood pressure")

bloodPressure = pd.DataFrame(file["Blood Pressure"])

bloodPressure[['Systolic', 'Diastolic']] = bloodPressure['Blood Pressure'].str.split('/', expand=True)
bloodPressure = bloodPressure.drop("Blood Pressure", axis = 1)
systolic = pd.DataFrame(bloodPressure["Systolic"])
diastolic = pd.DataFrame(bloodPressure["Diastolic"])

st.subheader("Sleep Duration")

sleepDuration = pd.DataFrame(file["Sleep Duration"])

merged_sys = pd.concat([sleepDuration, systolic], axis=1)
merged_dias = pd.concat([sleepDuration, diastolic], axis=1)

c1, c2= st.columns(2)
checkSys = c1.button("Systolic", key = "1")
checkDias = c2.button("Diastolic", key = "2")

if checkSys == True:

    fig = generate_graph_bp(merged_sys,"Sleep Duration","Systolic")
    fig.update_layout(xaxis_title= "Sleep Duration (hours)", yaxis_title='Systolic Blood Pressure (mm Hg)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title='Effect of sleep duration on blood pressure')
    fig.update_traces(marker=dict(color='red'))
    st.plotly_chart(fig)
elif checkDias == True:

    fig = generate_graph_bp(merged_dias,"Sleep Duration","Diastolic")
    fig.update_layout(xaxis_title="Sleep Duration (hours)", yaxis_title='Diastolic Blood Pressure (mm Hg)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title='Effect of sleep duration on blood pressure')
    fig.update_traces(marker=dict(color='green'))
    st.plotly_chart(fig)

st.subheader("Sleep Quality")

sleepQuality = pd.DataFrame(file["Quality of Sleep"])

c1, c2= st.columns(2)
checkSysQ = c1.button("Systolic", key= "3")
checkDiasQ = c2.button("Diastolic", key = "4")

merged_sysQ = pd.concat([sleepQuality, systolic], axis=1)
merged_diasQ = pd.concat([sleepQuality, diastolic], axis=1)

if checkSysQ == True:

    fig = generate_graph_bp(merged_sysQ,"Quality of Sleep","Systolic")
    fig.update_layout(xaxis_title= "Sleep Quality", yaxis_title='Systolic Blood Pressure (mm Hg)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title='Effect of sleep quality on blood pressure')
    fig.update_traces(marker=dict(color='red'))
    st.plotly_chart(fig)
elif checkDiasQ == True:

    fig = generate_graph_bp(merged_diasQ,"Quality of Sleep","Diastolic")
    fig.update_layout(xaxis_title="Sleep Quality", yaxis_title='Diastolic Blood Pressure (mm Hg)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title='Effect of sleep quality on blood pressure')
    fig.update_traces(marker=dict(color='green'))
    st.plotly_chart(fig)

st.header("Heart rate")

heartRate = pd.DataFrame(file["Heart Rate"])

st.subheader("Sleep Duration")

merged_HR = pd.concat([sleepDuration,heartRate],axis = 1)

fig = generate_graph_bp(merged_HR,"Sleep Duration", "Heart Rate")
fig.update_layout(xaxis_title="Sleep Duration (hours)", yaxis_title='Heart Rate (bpm)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title = "Effects of duration of sleep on heart rate")
fig.update_traces(marker=dict(color='blue'))
st.plotly_chart(fig)

st.subheader("Sleep Quality")

merged_HRQ = pd.concat([sleepQuality, heartRate],axis = 1)

fig = generate_graph_bp(merged_HRQ,"Quality of Sleep", "Heart Rate")
fig.update_layout(xaxis_title="Sleep Quality", yaxis_title='Heart Rate (bpm)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title = "Effects of duration of sleep on heart rate")
fig.update_traces(marker=dict(color='purple'))
st.plotly_chart(fig)


