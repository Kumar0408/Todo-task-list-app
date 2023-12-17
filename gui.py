from utils import get_todos, write_todos
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = get_todos()
            todos.append(values['todo'] + "\n")
            write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
