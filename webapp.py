import streamlit as st
from utils import get_todos, write_todos

todos_list = get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n" # tex_input key
    todos_list.append(todo)
    write_todos(todos_list)

st.title("My Todo WebApp")

for index, todo in enumerate(todos_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos_list.pop(index)
        write_todos(todos_list)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add new todo..",
               on_change=add_todo, key = "new_todo")
