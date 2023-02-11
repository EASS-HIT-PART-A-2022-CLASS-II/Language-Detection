import requests
import streamlit as st
import socket
import psycopg2
import json

def get_host_ip():
    try:
        host_ip = socket.gethostbyname("host.docker.internal")
        return host_ip
    except:
        return "127.0.0.1"


url = f"http://{get_host_ip()}/predict"


# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="db",
    port="5432",
    user="postgres",
    password="mysecretpassword",
    database="postgres"
)

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id SERIAL PRIMARY KEY,
        text TEXT NOT NULL,
        result TEXT NOT NULL
    )
""")
conn.commit()

st.title("Language Detection app 🚀")
st.write("Language Detection is a tool designed to identify the language of text. Currently, it uses the "
         "https://www.kaggle.com/datasets/basilb2s/language-detection dataset to check for 17 supported languages.")

text_input = st.text_area("Enter a text:")

if st.button('Send API request'):
    payload = {"text": text_input}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        st.write(data)

        # Save the result to the database
        cursor = conn.cursor()
        data_str = json.dumps(data)
        cursor.execute("INSERT INTO results (text, result) VALUES (%s, %s)", (text_input, data_str))
        conn.commit()

    else:
        st.write("Error occured, please check the input")

conn.close()
