#Data structure to store tasks.
tasks = []

#Function to add task to the list until they are ready to stop.
def add_tasks():
    while True:
        task = input("Enter you task here(Type 'stop' to finish adding tasks): ")
        if task.lower() == 'stop':
            break #If the user wants to stop adding to the list.
        tasks.append({"task": task, "completed": False}) #Format of how the list appears to the user.
        print("Task successfully added.")

#Function to mark tasks as complete.
def mark_tasks_completed():
    view_tasks()
    choice = input("Would you like to mark a task as completed? (y/n): ").lower() #Gives the user the choice of completion.
    if choice == 'y': #If the user chooses yes.
        task_index = int(input("Enter the number of the task you want completed: ")) -1
        if 0 <=task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print("Task successfully marked as complete.")
        else:
            print("Invalid task index! Please enter correct index.")
    elif choice == 'n': #If the user chooses no, also confirms the user entered the correct option.
        print("No tasks were marked as completed.")
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")

#Function to view all tasks.
def view_tasks():
    print("View tasks:")
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found")



#Test add_task Function.
add_tasks()

#Loop for marking tasks as completed or continue to add more tasks.
while True:
    mark_tasks_completed()
    if input("Would you like to add more tasks? (y/n): ").lower() != 'y':
        break
    add_tasks() #Sends the user back adding tasks after requesting to.

#Test view_task function.
view_tasks()