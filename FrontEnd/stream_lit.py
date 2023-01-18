import streamlit as st
import json
import requests


@st.cache
def clear_text():
    return ""


st.title("Language Detection app 🚀")
st.write("please enter an text to the text boxes")

def clear_form():
    st.session_state["Text_1"] = ""
    st.session_state["Text_2"] = ""

with st.form("myform"):
    f1, f2 = st.columns([1, 1])
    with f1:
        st.text_area("Text_1", key="Text_1")
    with f2:
        st.text_area("Text_2", key="Text_2")
    f3, f4 = st.columns([1, 1])
    with f3:
        submit = st.form_submit_button(label="Submit")
    with f4:
        clear = st.form_submit_button(label="Clear", on_click=clear_form)

if submit:
    st.write('Submitted')

if clear:
    st.write('Cleared')

st.write(st.session_state.Text_1)
st.write(st.session_state.Text_2)

