import streamlit as st
from utils import register,navigate
import time
def registration_page():
    st.title("Register Yourself")

    name = st.text_input("Name")
    username = st.text_input("Username", help="Username must be unique")
    acc_type = st.selectbox("Account type", ["Saving", "Current"])
    password = st.text_input("Password", type="password")
    confirm_password=st.text_input("Confirm Password", type="password")
    col1, col2,col3=st.columns(3)
    with col1:
        if st.button("Sign Up"):
                if name=="" or username=="" or password=="":
                    st.warning("Please fill all the details to proceed")
                elif register(username, name, password, acc_type):
                    st.success("Registered successfully! Please log in.")
                    time.sleep(1)
                    navigate("login")
                    st.rerun()
    with col3:
        col1,col2=st.columns(2)
        with col1:
            st.write("Already have an account?")
        with col2:
            if st.button("Login", type="tertiary"):
                navigate("login")
                st.rerun()