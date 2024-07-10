import streamlit as st
import pandas
# Set page layout to wide
st.set_page_config(layout="wide")
st.header("The best company")
st.write("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
          ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
         ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
         reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
         Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
          mollit anim id est laborum.

""")
st.subheader("Our Team")
col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data.csv")  # by default each data is divided by ,
with col1:
    for i, r in df[:4].iterrows():
        name = f"{r['first name']} {r['last name']}"
        st.subheader(name.title())
        st.write(r['role'])
        image_loc = "images/" +r['image']
        st.image(image_loc) 

with col2:
    for i, r in df[4:8].iterrows():
        name = f"{r['first name']} {r['last name']}"
        st.subheader(name.title())
        st.write(r['role'])
        st.image("images/"+r['image'])

with col3:
    for i, r in df[8:].iterrows():
        name = f"{r['first name']} {r['last name']}"
        st.subheader(name.title())
        st.write(r['role'])
        st.image("images/" + r['image'])

    


    
