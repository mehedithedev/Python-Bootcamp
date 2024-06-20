import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to increase your prdouctivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo: ",
 placeholder="Add new todo",
 on_change=add_todo,
 key='new_todo'
 )
print("The above script has been executed")

st.session_state