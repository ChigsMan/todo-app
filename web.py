import streamlit as st
import functions

import pandas as me

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



todos = functions.get_todos()


st.title("My Todo App")
st.subheader("This is my todo add.")
st.write("This app is to increase my productivity.")

#enumerate gives back the count/index of the current iteration
#and value of the current iteration
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #The pop() method removes the item at the given index from the list
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter text", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
st.session_state

