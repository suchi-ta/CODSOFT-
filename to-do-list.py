import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")
        
        
        self.tasks = []
        
       
        self.task_listbox = tk.Listbox(self.root, height=10, width=40)
        self.task_listbox.pack(pady=20)
        
       
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=5)
        
        
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)
        
        mark_done_button = tk.Button(self.root, text="Mark as Done", command=self.mark_task_done)
        mark_done_button.pack(pady=5)
        
        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)
        
        update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        update_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"description": task, "done": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_task_done(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["done"] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_task_index]["description"] = updated_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter the new task description.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task['description']
            if task["done"]:
                task_text += " [Done]"
            self.task_listbox.insert(tk.END, task_text)


root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
