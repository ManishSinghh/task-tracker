from datetime import datetime
import json


task_id= 1
task_list=[]
FILE_NAME = "tasks.json"

def load_tasks():
    global task_id, task_list
    try:
        with open(FILE_NAME, "r") as file:
            task_list = json.load(file)
            if task_list:
                task_id  = max(task["task_id"] for task in  task_list) + 1
    except FileNotFoundError:
        print("No existing task file found. Creating a new one...")
        save_tasks()
    except json.JSONDecodeError:
        print("Corrupted task file detected. Resetting data...")
        task_list = []
        save_tasks()

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(task_list,file, indent = 4)

def update_task():
    task_to_update = int(input("Enter the task id to be upated"))
    for task in task_list:
        if task['task_id'] == task_to_update:
            new_status = input("Enter the new status of the task (To Do | In Progress | Completed)")
            task['status'] = new_status

            if new_status.lower() =='completed':
                task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks()
            print("Task updated successfully")
            return
    
    print("Task Not Found. Please Enter the corret id")

def add_task():
    global task_id
    if len(task_list) >=7:
        print("Task Overload! Don't put too much stress on yourself!")
        return
    
    task= input("Enter your task details: ")
    createdAt=  createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = input("Enter the status of the task: ")
    completedAt = None

    task_dict={
        "task_id": task_id,
        "task_desc": task,
        "created_at": createdAt,
        "status": status,
        "completed_at": completedAt
    }

    task_list.append(task_dict)
    save_tasks()
    task_id+=1
def view_task():
    if len(task_list)==0:
        print("No tasks available")
    else:
        for task in task_list:
            print(f"ID: {task['task_id']}, Task: {task['task_desc']}, Created At: {task['created_at']}, Status: {task['status']}, Completed At: {task['completed_at']}")


load_tasks()
while True:
    print("Task Tracker Menu")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task Status")
    print("4. Exit")
    
    choice = input("Please Enter Your Choice: 1/2/3/4 ")

    if choice == "1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice == "3":
        update_task()
    elif choice =="4":
        print("Exiting Program. Goodbye")
        break
    else:
        print("Please Enter a valid choice")