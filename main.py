import streamlit as st
from registration import registration_page
from login import login_page
from dashboard import dashboard_page

st.set_page_config(page_title="ATM App", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "register"  # default page
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""


if st.session_state.page == "register":
    registration_page()
elif st.session_state.page == "login":
    login_page()
elif st.session_state.page == "dashboard":
    dashboard_page()