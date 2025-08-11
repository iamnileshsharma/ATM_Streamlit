import streamlit as st
from database import connect_db, create_table



def register(username, name,password, type):
    create_table()
    con=connect_db()
    cur=con.cursor()
    cur.execute("select username from users where username =?", (username,))
    data=cur.fetchone()
    if data is not None:
        st.warning("User already exists")
        return False
    else: 
        cur.execute("insert into users (username,name, password, type,balance) values(?,?,?,?,?)",(username, name,password,type,0.0))
        con.commit()
        cur.close()
        return True




def login_user(username, password):
    create_table()
    con=connect_db()
    cur=con.cursor()
    cur.execute("select username, password from users where username=?",(username,))
    data=cur.fetchone()

    if data is None:
        st.warning("User does not exists")
    else:
        db_username, db_password=data
        if db_username==username and db_password==password:
            st.session_state.logged_in=True
            st.session_state.username=username
            return True
        else: 
            st.warning("incorrect username or password")

def logout_user():
    st.session_state.logged_in=False
    st.session_state.username=""
    st.rerun()

def deposit_money(username,amount):
    con=connect_db()
    cur=con.cursor()
    cur.execute("update users set balance = balance+? where username =?",(amount,username))
    con.commit()
    con.close()

def withdraw_money(username, amount):
    con = connect_db()
    cur = con.cursor()
    data = cur.execute("SELECT balance FROM users WHERE username = ?", (username,)).fetchone()

    if data is None:
        con.close()
        return False, "User not found"

    balance = data[0]

    if balance < amount:
        cur.close()
        return False, "Insufficient funds"
    else:
        cur.execute("UPDATE users SET balance = balance - ? WHERE username = ?", (amount, username))
        con.commit()
        con.close()
        return True, "Withdrawal successful!"


def get_balance(username):
    con=connect_db()
    cur=con.cursor()
    data=cur.execute("select balance from users where username = ?",(username,)).fetchone()
    balance=round(data[0],2)
    return balance