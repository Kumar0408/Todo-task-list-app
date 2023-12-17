"""
Program to create todo list
"""
from utils import get_todos, write_todos
import time

now = time.strftime("%B %d, %Y %H:%M:%S")
print("It is", now)

while True:    # Get user action and strip spaces from it.
    user_action = input("Type add (with todo item), display, remove (with task number), "
                        "edit (with task number), clear or exit: ")
    user_action = user_action.strip()

    # To add new item.
    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + '\n'
        todo_list = get_todos()   # return a list with items as each line strings
        todo_list.append(todo)
        # print(todo_list)
        write_todos(todo_list)   # writes the list in the file

    # To display the whole list.
    elif user_action.startswith("display") or user_action.startswith("show"):
        todo_list = get_todos()
        if len(todo_list) == 0:
            print("No items in list")
        else:
            # new_todos = [item.strip(\n) for item in todos] -> will create new list with no \n after every item.
            for index, item in enumerate(todo_list):
                print(f"{index+1}-{item.capitalize()}", end='')

    # To remove an item in the list.
    elif user_action.startswith("remove"):
        try:
            todo_list = get_todos()
            index = int(user_action[7:])
            todo_list.pop(index-1)
            write_todos(todo_list)

        except ValueError:
            print("Your command is not valid. Please provide the task number.")
        except IndexError:
            print("There is no item with this number.")

    # To edit an existing item.
    elif user_action.startswith("edit"):
        try:
            todo_list = get_todos()
            index = int(user_action[5:])
            old_task = todo_list[index-1]
            todo_list[index-1] = input("Add the new todo task: ") + "\n"
            write_todos(todo_list)

        except ValueError:
            print("Your command is not valid. Please provide the task number")
        except IndexError:
            print("There is no item with this number.")

    elif user_action.startswith("exit"):
        break

    # To clear the existing to-do list.
    elif user_action.startswith("clear"):
        todo_list = get_todos()
        if len(todo_list) == 0:
            print("List already empty")
        else:
            todo_list.clear()
            write_todos(todo_list)

    else:
        print("Wrong command, try again")

print("Bye!")
