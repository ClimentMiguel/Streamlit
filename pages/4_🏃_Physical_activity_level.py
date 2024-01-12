import streamlit as st

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

df = pd.read_csv('/Users/Tomasss/uni/23_24Master/Visualizacion_de_datos/Entrega/Sleep_health_and_lifestyle_dataset.csv')
df

# top-level filters
Physical_activity_filter = st.selectbox("Select the physical activity level", pd.unique(df["Physical Activity Level"].sort_index("Physical Activity Level")))