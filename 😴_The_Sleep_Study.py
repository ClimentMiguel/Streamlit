import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="The Sleep Study", page_icon="=)", layout="centered", initial_sidebar_state="auto", menu_items=None)

if 'name' not in st.session_state:
    st.session_state['name'] = None

logged = False
st.session_state["Logged"] = logged
if st.session_state["name"] == None:
    st.title("¡Bienvenid@!")
else:
    st.title("¡Bienvenid@ %s!"%(st.session_state["name"]))
st.session_state["Logged"] = logged


st.image("./The Sleep study main.jpeg")
authentication_status = None
#st.session_states


with open('userdata.yml') as file:
    userdata = yaml.load(file, Loader=SafeLoader)


authenticator = stauth.Authenticate(userdata, 'some_cookie_name','some_signature_key')

name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status == None:
    st.warning('Por favor, introduzca su nombre de usuario y contraseña')
    logged = False
    st.session_state["name"] = None
elif authentication_status:
    authenticator.logout('Logout', 'main')
    logged = True
    st.session_state["Logged"] = logged
    st.session_state["name"] = name
elif authentication_status == False:
    st.error('Usuario/contraseña es incorrecto')
if not(logged):
    namenew = authenticator.register_user('Register',"main",False)
    with open("userdata.yml", "w") as f:
        yaml.dump(userdata, f)




