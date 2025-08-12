import streamlit as st
from utils import login_user
from utils import navigate
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username=="" or password=="":
            st.warning("Please fill all the details to proceed")
        elif login_user(username, password):
            navigate("dashboard")
            st.rerun()

    if st.button("Back to Register"):
        navigate("register")
        st.rerun()
