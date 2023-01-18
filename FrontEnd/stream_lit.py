import requests
import streamlit as st

st.title("Language Detection app 🚀")
st.write("Language-Detection is a tool for inorder to "
         "ideanfy what languease is the text . It checks strings and texts for now its based "
         "on https://www.kaggle.com/datasets/basilb2s/language-detection dataset "
         "and supports 17 Languages")

text_input = st.text_area("Enter a text:")

if st.button('Send API request'):
    payload = {"text": text_input}
    response = requests.post('http://0.0.0.0/predict', json=payload)
    if response.status_code == 200:
        data = response.json()
        st.write(data)
    else:
        st.write("Error occured, please check the input")
