from mcpi.minecraft import Minecraft
mc = Minecraft.create()

''' Program askt the user to input the tasks for the todo list and saves
    the tasks in a file to display the todo list later. '''

# Write into the todo list
def writeTodo():
    try:
        with open("todo.txt", "a") as todo:
            task = input("Enter your task ('exit' to quit): ")
            while task.lower() != "exit":
                todo.write(task + "\n")
                task = input("Enter your task ('exit' to quit): ")
    except:
        print("Could not open file!")


# Display the todo list
def displayTodo():
    display = input("Do you want to show your ToDo's? (Y/N) ")
    if display.lower() == "y":
        try:
            with open("todo.txt", "r") as todo:
                for line in todo:
                    print(line)
                    mc.postToChat(line)
        except:
            print("Could not open file!")
    else:
        addTodo = input("Do you want to add tasks? (Y/N) ")
        if addTodo.lower() == "y":
            writeTodo()
        else:
            print("Program finished!")
            exit()

writeTodo()
displayTodo()
