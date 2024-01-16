import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np
import plotly.graph_objects as go


st.set_page_config(page_title="BMI")

file = pd.read_csv("DATABASE RAW.csv",delimiter=',',encoding="latin-1")
file = file.replace(to_replace="Normal Weight", value= "Normal" )


Normal =file.loc[file["BMI Category"] == "Normal"]
normalTot = len(Normal.index)
normalDisorders = [len(file[((file["Sleep Disorder"].fillna(value="None" )) == "None") & (file["BMI Category"] == "Normal")]),len(file[(file["Sleep Disorder"] == "Sleep Apnea") & (file["BMI Category"] == "Normal")]),len(file[(file["Sleep Disorder"] == "Insomnia") & (file["BMI Category"] == "Normal")])]
avgNormal = round(Normal["Sleep Duration"].mean(), 2)
avgNormalQ = Normal["Quality of Sleep"].mean()
normalFracs = np.array([(element*100)/normalTot for element in normalDisorders])


Overweight =file.loc[file["BMI Category"] == "Overweight"]
avgOW = round(Overweight["Sleep Duration"].mean(), 2)
avgOWQ = Overweight["Quality of Sleep"].mean()
OWTot = len(Overweight.index)
OWDisorders = [len(file[((file["Sleep Disorder"].fillna(value="None" )) == "None") & (file["BMI Category"] == "Overweight")]),len(file[(file["Sleep Disorder"] == "Sleep Apnea") & (file["BMI Category"] == "Overweight")]),len(file[(file["Sleep Disorder"] == "Insomnia") & (file["BMI Category"] == "Overweight")])]
OWFracs = np.array([(element*100)/OWTot for element in OWDisorders])


Obese =file.loc[file["BMI Category"] == "Obese"]
avgObese = round(Obese["Sleep Duration"].mean(), 2)
avgObeseQ = Obese["Quality of Sleep"].mean()
obeseTot = len(Obese.index)
obeseDisorders = [len(file[((file["Sleep Disorder"].fillna(value="None" )) == "None") & (file["BMI Category"] == "Obese")]),len(file[(file["Sleep Disorder"] == "Sleep Apnea") & (file["BMI Category"] == "Obese")]),len(file[(file["Sleep Disorder"] == "Insomnia") & (file["BMI Category"] == "Obese")])]
obeseFracs = np.array([(element*100)/obeseTot for element in obeseDisorders])

BMIs = ["Normal", "Obese", "Overweight"]

def makeChart(n,dis):
    fig = go.Figure(layout_yaxis_range=[0,100])
    fig.add_trace(go.Bar(
        x=BMIs,
        y=[normalFracs[n],obeseFracs[n],OWFracs[n]],
        name='Primary Product',
        marker_color='indianred'))
    fig.update_xaxes(title = "BMI Category")
    fig.update_yaxes(title = dis)
        
    return fig

barchart_1 = pd.DataFrame({"Normal":[avgNormal], "Overweight": [avgOW], "Obese": [avgObese]})
barchart_1 = pd.melt(barchart_1)

barchart_2 = pd.DataFrame({"Normal":[avgNormalQ], "Overweight": [avgOWQ], "Obese": [avgObeseQ]})
barchart_2 = pd.melt(barchart_2)


chart_1 = alt.Chart(barchart_1, title='').mark_bar(clip=True,
    opacity=1,size=70
    ).encode(
    x =alt.X('variable').title("Categoría de BMI"),
    y =alt.Y('value:Q').scale(domain=(5.8,7.6)).title("Duración de sueño (hours)"),
    color= alt.Color('variable',legend=None)
).configure_view(stroke='transparent').properties(title = "Efecto del BMI en la duración de sueño",height = 500).configure_title(
    anchor='middle'
)

chart_2 = alt.Chart(barchart_2, title='').mark_bar(clip=True,
    opacity=1,size=70
    ).encode(
    x =alt.X('variable').title("Categoría de BMI"),
    y =alt.Y('value:Q').scale(domain=(5.8,7.6)).title("Calidad de sueño"),
    color= alt.Color('variable',legend=None)
).configure_view(stroke='transparent').properties(title = "Efectos del BMI en la calidad de sueño",height = 500).configure_title(
    anchor='middle'
)

st.title("Efectos del BMI en el sueño")

st.header("Duración del sueño")
st.altair_chart(chart_1, use_container_width=True)

st.header("Calidad del sueño")
st.altair_chart(chart_2, use_container_width=True)



st.header("Trastornos del sueño")

c1, c2, c3= st.columns([1.3,1,1])
checkNone = c1.button("Ningún trastorno de sueño", key = "1")
checkSA = c2.button("Apnea de sueño", key = "2")
checkInsomnia = c3.button("Insomnio", key = "3")

if checkNone:
    st.plotly_chart(makeChart(0, "% de ningún trastorno"), use_container_width=True)
elif checkSA:
    st.plotly_chart(makeChart(1, "% de apnea de sueño"), use_container_width=True)

elif checkInsomnia:
    st.plotly_chart(makeChart(2, "% de insomnio"), use_container_width=True)

with st.expander("Video sobre la relación entre la obesidad y el sueño"):


    
    st.video("https://www.youtube.com/watch?v=llJsK0pjM2s")
