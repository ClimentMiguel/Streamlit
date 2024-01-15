import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="The Sleep Study", page_icon="=)", layout="centered", initial_sidebar_state="auto", menu_items=None)

logged = False
st.session_state["Logged"] = logged
if st.session_state["name"] == None:
    st.header("Welcome!")
else:
    st.header("Welcome %s!"%(st.session_state["name"]))
st.session_state["Logged"] = logged


authentication_status = None
#st.session_states

passwords = ['123', '456']
hashed_passwords = stauth.Hasher(passwords).generate()
usernames = {'jsmith':{"name": "jsmith", "password":hashed_passwords[0]}, "rbriggs": {'name':"rbriggs","password":hashed_passwords[1]}}

names = {"usernames": usernames, "passwords": passwords}


with open('userdata.yml') as file:
    userdata = yaml.load(file, Loader=SafeLoader)


authenticator = stauth.Authenticate(userdata, 'some_cookie_name','some_signature_key')

name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status == None:
    st.warning('Please enter your username and password')
    logged = False
elif authentication_status:
    authenticator.logout('Logout', 'main')
    logged = True
    st.session_state["Logged"] = logged
elif authentication_status == False:
    st.error('Username/password is incorrect')
if not(logged):
    namenew = authenticator.register_user('Register',"main",False)
    with open("userdata.yml", "w") as f:
        yaml.dump(userdata, f)




