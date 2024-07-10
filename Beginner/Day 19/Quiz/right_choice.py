import streamlit as st
user_choice = st.radio("Amount", options=[10,20,30])
if user_choice == 30:
    st.info("You made the right choice") 