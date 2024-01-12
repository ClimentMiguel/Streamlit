import streamlit as st

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

df = pd.read_csv('/Users/Tomasss/uni/23_24Master/Visualizacion_de_datos/Entrega/Sleep_health_and_lifestyle_dataset.csv')

# top-level filters
#Physical_activity_filter = st.selectbox("Select the physical activity level", pd.unique(df["Physical Activity Level"]))
#df = df[df["Physical Activity Level"] == Physical_activity_filter]
#df


st.markdown("### First Chart")
fig = px.density_heatmap(
    data_frame=df, y="Physical Activity Level", x="Quality of Sleep"
)
st.write(fig)
   

st.markdown("### Second Chart")
fig2 = px.histogram(data_frame=df, x="Daily Steps")
st.write(fig2)