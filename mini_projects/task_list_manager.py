"""
Challenge : terminal based task manager

Create a python scripts that lets users manage a to-do list directly fron the terminal

Your programm should:
1. Allow users to :
    - Add a task
    - view all tasks
    - mark a task as completed
    - delete a task
    - exit the app
2. save all tasks in a test file named 'tasks.txt' so data persists between runs
3.Display tasks with a index number and a tick mark if completed

Example menu :
1. Add Task
2. View Tasks
3. Mark Task as completed
4. Delete a tasks
5. Exit

Example outputs:
Your tasks :

Buy groceries || not done
finish Python Project || done
read a book || not_done


Bonus:
- prevent empty tasks from being added
- validate task numbers before completing / deleting
"""

import os

TASK_FILE = "tasks.txt"

def load_task():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r', encoding="utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text.strip(), "done": status.strip() == "done"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']} || {status}\n")

def display_tasks(tasks):
    if not tasks:
        print("No task found.")
    else:
        for i, task in enumerate(tasks, 1):
            check_box = "✅" if task["done"] else " "
            print(f"{i}. [{check_box}] {task['text']}")
    print()

def task_manager():
    tasks = load_task()

    while True:
        print("\n--------- Task List Manager ----------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit App")

        choice = input("Choose an option (1-5): ").strip()

        match choice:
            case "1":
                text = input("Enter your task: ").strip()
                if text:
                    tasks.append({"text": text, "done": False})
                    save_tasks(tasks)
                else:
                    print("Task cannot be empty.")

            case "2":
                display_tasks(tasks)

            case "3":
                display_tasks(tasks)
                try:
                    num = int(input("Enter the task number to mark as done: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["done"] = True
                        save_tasks(tasks)
                        print("Task marked as done.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

            case "4":
                display_tasks(tasks)
                try:
                    num = int(input("Enter the task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_tasks(tasks)
                        print(f"Task removed: {removed['text']}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

            case "5":
                print("Exiting Task Manager.")
                break

            case _:
                print("Please choose a valid option.")

# Run the app
task_manager()



