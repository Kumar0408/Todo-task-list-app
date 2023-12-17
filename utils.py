FILEPATH = "todos.txt"


def get_todos(path=FILEPATH):
    """
    :param path: path to the .txt file.
    :return: list of existing to-do tasks in .txt file.

    Reads the .txt file and returns the list of to-do items.
    """
    with open(path, 'r') as file:
        content = file.readlines()
    return content


# Function to write todo tasks in .txt file.
def write_todos(todos_list, path=FILEPATH):
    """
    :param todos_list: to-do tasks to be written in the .txt file
    :param path: path to the .txt file
    :return: None

    Writes the new to-do list in the .txt file
    """
    with open(path, 'w') as file:
        file.writelines(todos_list)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
