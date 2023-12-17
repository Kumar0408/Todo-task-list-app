from utils import get_todos, write_todos
import PySimpleGUI as sg

# Label for the input box
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# Buttons
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
remove_button = sg.Button("Complete")
clear_button = sg.Button("Clear")
exit_button = sg.Button("Exit")

# List box
list_box = sg.Listbox(values=get_todos(), key='todos',
                      enable_events=True, size=(45, 10))

# Main Window
window = sg.Window('My To-do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, sg.Column([[edit_button], [remove_button]],
                            element_justification='left')],
                           [clear_button, exit_button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read()
    print("Event: ", event)
    print("Values: ", values)
    match event:
        case 'Add':
            todos_list = get_todos()
            todos_list.append(values['todo'] + "\n")
            write_todos(todos_list)
            window['todos'].update(values=todos_list)
            window['todo'].update(value='')
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_to_do = values['todo'] + "\n"
            todos_list = get_todos()
            index = todos_list.index(todo_to_edit)
            todos_list[index] = new_to_do
            write_todos(todos_list)
            window['todos'].update(values=todos_list)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            todo_to_remove = values['todo']
            todos_list = get_todos()
            todos_list.pop(todos_list.index(todo_to_remove))
            write_todos(todos_list)
            window['todos'].update(values=todos_list)
            window['todo'].update(value='')
        case "Clear":
            todos_list = get_todos()
            todos_list.clear()
            write_todos(todos_list)
            window['todos'].update(values=todos_list)
        case sg.WIN_CLOSED | "Exit":
            break


window.close()
