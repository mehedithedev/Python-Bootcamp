import streamlit as st
import pandas
from send_email import send_email
df = pandas.read_csv("./topics.csv")

st.header("Contact Us")

with st.form(key="email_forms"):
    email = st.text_input("Your Email Address: ")
    option = st.selectbox(
        'What topic do you want to discuss?',
        df["topic"]
    )
    text_message = st.text_area("Your Message: ")
    message = f"""\
Subject: New email from {email}

From: {email}
Topic: {option}
{text_message}
"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email Sent!")