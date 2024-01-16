import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="BMI")

file = pd.read_csv("DATABASE RAW.csv",delimiter=',',encoding="latin-1")
file = file.replace(to_replace="Normal Weight", value= "Normal" )


Normal =file.loc[file["BMI Category"] == "Normal"]
avgNormal = round(Normal["Sleep Duration"].mean(), 2)
avgNormalQ = Normal["Quality of Sleep"].mean()

Overweight =file.loc[file["BMI Category"] == "Overweight"]
avgOW = round(Overweight["Sleep Duration"].mean(), 2)
avgOWQ = Overweight["Quality of Sleep"].mean()

Obese =file.loc[file["BMI Category"] == "Obese"]
avgObese = round(Obese["Sleep Duration"].mean(), 2)
avgObeseQ = Obese["Quality of Sleep"].mean()

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


with st.expander("Video sobre la relación entre la obesidad y el sueño"):


    
    st.video("https://www.youtube.com/watch?v=llJsK0pjM2s")
