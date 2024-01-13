import streamlit as st

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/Tomasss/uni/23_24Master/Visualizacion_de_datos/Entrega/Sleep_health_and_lifestyle_dataset.csv')

# top-level filters
#Physical_activity_filter = st.selectbox("Select the physical activity level", pd.unique(df["Physical Activity Level"]))
#df = df[df["Physical Activity Level"] == Physical_activity_filter]
#df
st.markdown('## Correlacion actividad fisica ~ pasos diarios')
st.scatter_chart(data=df, x = 'Physical Activity Level', y = 'Daily Steps', color=None, size=None, width=0, height=0, use_container_width=True)


st.markdown("### First Chart")
fig = px.density_heatmap(
    data_frame=df, y="Physical Activity Level", x="Quality of Sleep"
)
st.write(fig)
   

st.markdown("### Second Chart")
fig2 = px.histogram(data_frame=df, x="Daily Steps")
st.write(fig2)

