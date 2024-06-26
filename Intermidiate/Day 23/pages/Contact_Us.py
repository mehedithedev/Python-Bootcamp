import streamlit as st
from send_email import send_email


st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    message = message + "\n" + user_email
    button = st.form_submit_button()
    if button:
        send_email(message)