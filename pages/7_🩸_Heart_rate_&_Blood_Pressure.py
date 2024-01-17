import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="Heart rate & Blood Pressure")

file = pd.read_csv("DATABASE RAW.csv",delimiter=',',encoding="latin-1")

def generate_graph_bp(df, type_1,type_2):
    fig = px.scatter(df, x=type_1, y=[type_2],
                labels={'value': 'Blood Pressure', 'variable': 'Type'},
                trendline="ols")

    return fig

st.title("Efectos del sueño en la presión sanguínea y las pulsaciones cardiacas")


st.header("Presión sanguínea")

bloodPressure = pd.DataFrame(file["Blood Pressure"])

bloodPressure[['Systolic', 'Diastolic']] = bloodPressure['Blood Pressure'].str.split('/', expand=True)
bloodPressure = bloodPressure.drop("Blood Pressure", axis = 1)
systolic = pd.DataFrame(bloodPressure["Systolic"])
diastolic = pd.DataFrame(bloodPressure["Diastolic"])
st.subheader("Duración del sueño")

sleepDuration = pd.DataFrame(file["Sleep Duration"])

merged_sys = pd.concat([sleepDuration, systolic], axis=1)
merged_dias = pd.concat([sleepDuration, diastolic], axis=1)

c1, c2= st.columns(2)
checkSys = c1.button("Sistólica", key = "1")
checkDias = c2.button("Diastólica", key = "2")

if checkSys == True:

    fig = generate_graph_bp(merged_sys,"Sleep Duration","Systolic")
    fig.update_layout(xaxis_title= "Duración del sueño (horas)", yaxis_title='Presión sistólica (mm Hg)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title='Efectos de la duración del sueño en la presión sistólica')
    fig.update_traces(marker=dict(color='red'))
    st.plotly_chart(fig)
elif checkDias == True:

    fig = generate_graph_bp(merged_dias,"Sleep Duration","Diastolic")
    fig.update_layout(xaxis_title="Duración del sueño (horas)", yaxis_title='Presión diastólica (mm Hg)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title='Efectos de la duración del sueño en la presión diastólica')
    fig.update_traces(marker=dict(color='green'))
    st.plotly_chart(fig)

st.subheader("Calidad del sueño")

sleepQuality = pd.DataFrame(file["Quality of Sleep"])

c1, c2= st.columns(2)
checkSysQ = c1.button("Sistólica", key= "3")
checkDiasQ = c2.button("Diastólica", key = "4")

merged_sysQ = pd.concat([sleepQuality, systolic], axis=1)
merged_diasQ = pd.concat([sleepQuality, diastolic], axis=1)

if checkSysQ == True:

    fig = generate_graph_bp(merged_sysQ,"Quality of Sleep","Systolic")
    fig.update_layout(xaxis_title= "Calidad del sueño", yaxis_title='Presión sistólica (mm Hg)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title='Efectos de la calidad del sueño en la presión sistólica')
    fig.update_traces(marker=dict(color='red'))
    st.plotly_chart(fig)
elif checkDiasQ == True:

    fig = generate_graph_bp(merged_diasQ,"Quality of Sleep","Diastolic")
    fig.update_layout(xaxis_title="Calidad del sueño", yaxis_title='Presión diastólica (mm Hg)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title='Efectos de la calidad del sueño en la presión diastólica')
    fig.update_traces(marker=dict(color='green'))
    st.plotly_chart(fig)


st.header("Pulsación cardiaca")

heartRate = pd.DataFrame(file["Heart Rate"])

st.subheader("Duración del sueño")

merged_HR = pd.concat([sleepDuration,heartRate],axis = 1)

fig = generate_graph_bp(merged_HR,"Sleep Duration", "Heart Rate")
fig.update_layout(xaxis_title="Duración del sueño (horas)", yaxis_title='Pulsación cardiaca (bpm)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title = "Efectos de la duración del sueño en las pulsaciones cardiacas")
fig.update_traces(marker=dict(color='blue'))
st.plotly_chart(fig)

st.subheader("Calidad del sueño")

merged_HRQ = pd.concat([sleepQuality, heartRate],axis = 1)

fig = generate_graph_bp(merged_HRQ,"Quality of Sleep", "Heart Rate")
fig.update_layout(xaxis_title="Calidad del sueño", yaxis_title='Pulsación cardiaca (bpm)',
                  legend_title='Legend', autosize=False, width=800, height=500,showlegend=False, title = "Efectos de la calidad del sueño en las pulsaciones cardiacas")
fig.update_traces(marker=dict(color='purple'))
st.plotly_chart(fig)

st.subheader("Trastornos del sueño")

file["Sleep Disorder"] = file["Sleep Disorder"].fillna(value="None")

avgHR = [file[file["Sleep Disorder"]==el]["Heart Rate"].mean() for el in ["None","Sleep Apnea", "Insomnia"]]

fig = go.Figure()
fig.add_trace(go.Bar(
    x=["None","Sleep Apnea","Insomnia"],
    y=avgHR,
    name='Primary Product',
    marker_color='indianred')
    )
fig.update_xaxes(title = "Trastorno del sueño")
fig.update_yaxes(title = "Pulsación cardiaca (bpm)")
fig.update_layout(title = "Efectos de los trastornos de sueño en las pulsaciones cardiacas")
st.plotly_chart(fig, use_container_width=True)