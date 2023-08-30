import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    new_todos = st.session_state["new_todo"] + "\n"
    TODO = new_todos.title()
    todos.append(TODO)
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    # checkbox_key = f"Checkbox_{index}"
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo item: ",
              placeholder="Add a new todo item.... ",
              on_change=add_todo, key="new_todo")

# print("Hello")

st.session_state

