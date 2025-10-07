from functions import get_todos, write_todos
import time

user_prompt = "Type add, show, edit, complete or exit: "
print("Welcome to the Todo App!")

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo+"\n")

        write_todos(todos)
      
    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1} - {item.capitalize()}")
    
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            if 0 < number <= len(todos):
                new_todo = input("Enter the new todo: ")
                todos[number - 1] = new_todo + "\n"
            else:
                print("Invalid todo number.")

            write_todos(todos)

        except ValueError:
            print("Your command is not valid. Following edit, you need to enter the number of the todo.")
            continue
    
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            if 0 < number <= len(todos):
                index = number - 1
                todo_to_remove = todos[index].strip("\n")
                print(f"Todo '{todo_to_remove}' was removed from the list.")
                todos.pop(index)
            else:
                print("Invalid todo number.")

            write_todos(todos)

        except ValueError or IndexError:
            print("Your command is not valid. Following complete, you need to enter the number of the todo.")
            continue
        
    elif user_action.startswith("exit"):
        print("Bye!")
        break

    else:
        print("Command is not valid. Try again.")