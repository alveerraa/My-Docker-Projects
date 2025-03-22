import streamlit as st
import psycopg2

# Database connection
def connect_db():
    return psycopg2.connect(
        host="db",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )

st.title("📊 Streamlit & PostgreSQL App")

try:
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    st.success(f"Connected to database: {db_version[0]}")
    cur.close()
    conn.close()
except Exception as e:
    st.error(f"Error connecting to database: {e}")

