import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to increase your prdouctivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo: ",
 placeholder="Add new todo",)
print("Hello")