import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mehedi Hasan")
    content = """
    Hi, I'm Mehedi Hasan, a student of Software Development. 
    """
    st.info(content)


content2 = """
    Below you can find some of the apps I have build in Python. 
    Feel free to contact me. 
    """

st.write(content2)

col3, col4 = st.columns(2)

# Importing data.csv file
df = pandas.read_csv("/data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])


