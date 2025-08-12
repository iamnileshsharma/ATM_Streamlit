import streamlit as st
from utils import login_user
from utils import navigate
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(username, password):
            navigate("dashboard")
            st.rerun()
    if st.button("Forgot password?"):
        navigate("reset")
        st.rerun()
    if st.button("Back to Register"):
        navigate("register")
        st.rerun()
