import streamlit as st
from utils import navigate

def reset_page():
    st.title("reset password")
    username=st.text_input("Username")
    password=st.text_input("current password", help="current password")
    new_password=st.text_input("new password")
    confirm_new_pasword=st.text_input("confirm")
    col1,col2,col3=st.columns(3)
    with col1:
        if st.button("reset"):
            if(new_password==confirm_new_pasword):
                pass
            else:
                st.warning("New password should match with confirmed password")
    with col3:
        if st.button("Login Page", type="tertiary"):
            navigate("login")
            st.rerun()