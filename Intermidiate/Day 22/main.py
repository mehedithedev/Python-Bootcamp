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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Importing data.csv file
df = pandas.read_csv("/workspaces/Python-Bootcamp/Intermidiate/Day 22/data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        image_path = "/workspaces/Python-Bootcamp/Intermidiate/Day 22/images/" + row["image"]
        st.image(image_path)
        st.write(f"[Source Code]({row['url']})")    ### This is a special type of string

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        image_path = "/workspaces/Python-Bootcamp/Intermidiate/Day 22/images/" + row["image"]
        st.image(image_path)

