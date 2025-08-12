import streamlit as st
from utils import register,navigate
import time
def registration_page():
    st.title("Register Yourself")

    name = st.text_input("Name")
    username = st.text_input("Username", help="Username is unique")
    acc_type = st.selectbox("Account type", ["Saving", "Current"])
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
            if register(username, name, password, acc_type):
                st.success("Registered successfully! Please log in.")
                time.sleep(1)
                navigate("login")
                st.rerun()
    st.write("Already have an account?")
    if st.button("Login", type="tertiary"):
        navigate("login")
        st.rerun()