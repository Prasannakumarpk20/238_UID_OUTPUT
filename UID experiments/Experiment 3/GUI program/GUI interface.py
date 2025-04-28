import tkinter as tk
from tkinter import messagebox
import json
import os

TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Main application class
class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Task Manager")
        self.tasks = load_tasks()

        # UI Elements
        self.title_label = tk.Label(root, text="Task Title")
        self.title_label.pack()

        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack()

        self.desc_label = tk.Label(root, text="Task Description")
        self.desc_label.pack()

        self.desc_entry = tk.Entry(root, width=50)
        self.desc_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=80)
        self.task_listbox.pack()

        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.complete_task)
        self.complete_button.pack(pady=2)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=2)

        self.refresh_tasks()

    def add_task(self):
        title = self.title_entry.get()
        desc = self.desc_entry.get()
        if title:
            self.tasks.append({
                "title": title,
                "description": desc,
                "completed": False
            })
            self.save_and_refresh()
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Missing Info", "Task title is required.")

    def complete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["completed"] = True
            self.save_and_refresh()
        else:
            messagebox.showinfo("No Selection", "Select a task to mark as complete.")

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.save_and_refresh()
        else:
            messagebox.showinfo("No Selection", "Select a task to delete.")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✅" if task["completed"] else "❌"
            self.task_listbox.insert(tk.END, f"[{status}] {task['title']} - {task['description']}")

    def save_and_refresh(self):
        save_tasks(self.tasks)
        self.refresh_tasks()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
