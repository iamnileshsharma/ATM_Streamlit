import streamlit as st
from utils import register, login_user, logout_user, deposit_money, withdraw_money, get_balance
from database import create_table
import time

st.set_page_config(page_title="ATM App", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "register"  # default page
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

def navigate(page):
    st.session_state.page = page

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
    if st.button("Login"):
        navigate("login")
        st.rerun()

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(username, password):
            navigate("dashboard")
            st.rerun()

    if st.button("Back to Register"):
        navigate("register")
        st.rerun()

def dashboard_page():
    st.title("Dashboard")
    create_table()

    if not st.session_state.logged_in:
        st.warning("Please login to access your dashboard.")
        if st.button("Login"):
            navigate("login")
            st.rerun()
        return

    st.info(f"Welcome {st.session_state.username}!")


    from database import connect_db
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT name, type FROM users WHERE username = ?", (st.session_state.username,))
    name, acc_type = cur.fetchone()
    cur.close()
    con.close()

    st.success(f"Hello {name}, Account type: {acc_type}")

    account_tab, withdraw_tab, deposit_tab = st.tabs(["💼 Account", "💸 Withdraw", "💰 Deposit"])


    with account_tab:
        balance = get_balance(st.session_state.username)
        st.metric("Current Balance", f"₹ {balance:.2f}")

    with withdraw_tab:
        withdraw_input = st.text_input("Amount to Withdraw", key="withdraw_amount")
        if st.button("Withdraw"):
            try:
                amount = float(withdraw_input)
                if amount <= 0:
                    st.warning("Amount must be positive.")
                else:
                    success, msg = withdraw_money(st.session_state.username, amount)
                    if success:
                        st.success(msg)
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error(msg)
            except ValueError:
                st.error("Enter a valid number.")

    with deposit_tab:
        deposit_input = st.text_input("Amount to Deposit", key="deposit_amount")
        if st.button("Deposit"):
            try:
                amount = float(deposit_input)
                if amount <= 0:
                    st.warning("Amount must be positive.")
                else:
                    deposit_money(st.session_state.username, amount)
                    st.success("Deposit successful!")
                    time.sleep(1)
                    st.rerun()
            except ValueError:
                st.error("Enter a valid number.")


    st.markdown("---")
    if st.button("Logout"):
        logout_user()
        navigate("login")

if st.session_state.page == "register":
    registration_page()
elif st.session_state.page == "login":
    login_page()
elif st.session_state.page == "dashboard":
    dashboard_page()
