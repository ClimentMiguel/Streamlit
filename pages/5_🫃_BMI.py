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
    x =alt.X('variable').title("BMI Category"),
    y =alt.Y('value:Q').scale(domain=(5.8,7.6)).title("Sleep Duration (hours)"),
    color= alt.Color('variable',legend=None)
).configure_view(stroke='transparent').properties(title = "Effect of BMI on duration of sleep",height = 500).configure_title(
    anchor='middle'
)

chart_2 = alt.Chart(barchart_2, title='').mark_bar(clip=True,
    opacity=1,size=70
    ).encode(
    x =alt.X('variable').title("BMI Category"),
    y =alt.Y('value:Q').scale(domain=(5.8,7.6)).title("Sleep Quality"),
    color= alt.Color('variable',legend=None)
).configure_view(stroke='transparent').properties(title = "Effect of BMI on quality of sleep",height = 500).configure_title(
    anchor='middle'
)

st.title("Effects of BMI on Sleep")

st.header("Sleep Duration")
st.text("Text")
st.altair_chart(chart_1, use_container_width=True)

st.header("Sleep Quality")
st.text("Text")
st.altair_chart(chart_2, use_container_width=True)

with st.expander("Video sobre obesidad"):


    
    st.video("https://www.youtube.com/watch?v=llJsK0pjM2s")
c1, c2, c3, c4, c5 = st.columns(5)
c1.button("Mi botón")
c2.checkbox("Un Checkbox")
c3.number_input("Input de número", value=5, min_value=0, max_value=10, step=1)
test = c4.text_input("Input de texto")
c5.metric("EL bicho", "#7")


with st.empty():
    st.write(test)


