# define the help functions
def get_todos(file_path="files/todos.txt"):
    """Read a text file and return the list of to-do items."""
    with open(file_path, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos, file_path="files/todos.txt"):
    """Write the list of to-do items to a text file."""
    with open(file_path, "w") as file:
        file.writelines(todos)

if __name__ == "__main__":
    print(get_todos())