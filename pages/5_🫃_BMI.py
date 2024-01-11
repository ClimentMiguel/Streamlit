import streamlit as st
st.set_page_config(page_title="BMI")

hola = "hola"

st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Text")
st.image("BMI to avg sleep.png", caption="BMI to Average Sleep")
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


