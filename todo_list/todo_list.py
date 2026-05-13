print("Welcome! ")
tasks = []
def add_todo_list():
    while True:
        try:
            task = input("Enter your task: ").capitalize()
            if task.lower() == "exit":
                break
            if task  and task not in tasks:
                tasks.append(task)
                print(f"Todo List: {tasks}")
        except (KeyboardInterrupt, EOFError): 
            print("The program is completed")
            break    
    return tasks        

add_todo_list()
print(f"Current List: {tasks}")      
        






