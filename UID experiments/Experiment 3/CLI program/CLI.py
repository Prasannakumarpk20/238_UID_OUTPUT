import json
import os

TASK_FILE = "tasks.json"

# Load existing tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({
        "title": title,
        "description": description,
        "completed": False
    })
    print("✅ Task added.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. [{status}] {task['title']} - {task['description']}")

# Mark a task as complete
def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("🎉 Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["title"] = input("Enter new title: ")
            tasks[index]["description"] = input("Enter new description: ")
            print("🔁 Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("🗑️ Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n==== Task Manager ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            update_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
