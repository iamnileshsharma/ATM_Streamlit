import streamlit as st
from database import create_table
from utils import navigate
from utils import  logout_user, deposit_money, withdraw_money, get_balance, reset_password
import time
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

    account_tab, withdraw_tab, deposit_tab, reset_tab = st.tabs(["💼 Account", "💸 Withdraw", "💰 Deposit","🔑Reset password"])


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
    
    with reset_tab:
        st.header("reset password")
        password=st.text_input("current password",type="password")
        new_password=st.text_input("new password",type="password")
        confirm_new_pasword=st.text_input("confirm",type="password")
        
        if st.button("Change password"):
            if(new_password==confirm_new_pasword):
                if reset_password(st.session_state.username,password,new_password):
                    st.success("Password changed succesfully")
                    time.sleep(2)
                    logout_user()
                    st.rerun()
                else:
                    st.error("Incorrect current password, please check")
                    time.sleep(2)
            else:
                st.error("New password should match with confirmed password")

    st.markdown("---")

    if st.button("Logout"):
        logout_user()