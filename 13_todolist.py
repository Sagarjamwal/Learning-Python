# A basic to do list that stores data in a text file so that it keeps everything in memory
import os
FOLDER_NAME="13_todolist"
FILE_NAME="todo.txt"
FILE_PATH=os.path.join(FOLDER_NAME,FILE_NAME)
if not os.path.exists(FOLDER_NAME):
    os.mkdir(FOLDER_NAME)
# They will create whatever files necessary or check if they alr exists and make them work
#--Basic TO DO LIST--
def show_tasks():
    try:
        with open(FILE_PATH,"r")as file:
            tasks=file.readlines()
            if not tasks:
                print("Your to-do-list is empty!")
            else:
                print("---Your tasks are ----")
                for task in tasks:
                    print(f"-{task.strip()}")
    except:
        FileNotFoundError
        print("No tasks have been added yet.")
def add_tasks(task_text):
    with open(FILE_PATH,"a")as file:
        file.write(task_text + "\n")
    print(f"Tasks are saved in {FILE_PATH}")

while True:
    choice=input("Type 'view','add',exit:").lower()
    if choice=="add":
        new_task=input("What do you need to do?")
        add_tasks(new_task)
    elif choice=="view":
        show_tasks()
    else:
        break