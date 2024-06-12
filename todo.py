import os
import pickle
import tkinter as tk

class ToDo:
    def __init__(self, title, status = "To Do"):
        self.title = title
        self.status = status
    
class ToDoApp:
    def __init__(self, root, todos, save_file='save.pkl'):
        self.root = root
        self.todos = todos
        self.filename = save_file
        self.load()
        self.createWidgets()

    def addTask(self):
        task_name = self.enter_task_txt.get()
        new_todo = ToDo(task_name)
        self.todos.append(new_todo)
        self.enter_task_txt.delete(0, tk.END)
        self.updateList()

    def createWidgets(self):
        self.todo_frame =tk.Frame(self.root)
        self.todo_frame.grid(row=0, column=0)
        self.enter_task_label = tk.Label(self.root, text = "Add task:")
        self.enter_task_label.grid(row=13, column=0)
        self.enter_task_txt = tk.Entry(self.root, width=30)
        self.enter_task_txt.grid(row=13, column=1)
        submit_button = tk.Button(self.root, text="OK", command=self.addTask)
        submit_button.grid(row=13, column=2)
        exit_button = tk.Button(self.root, text="Save & Exit", command=self.save)
        exit_button.grid(row=15,column=0)
        self.updateList()

    def deleteTask(self, index: int):
        del self.todos[index]
        self.updateList()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as file:
                self.todos = pickle.load(file)
        else:
            self.todos = []

    def save(self):
       with open(self.filename, "wb") as file:
           pickle.dump(self.todos, file)
       exit()

    def toggleStatus(self, index : int):
        if self.todos[index].status == "Done":
            self.todos[index].status = "To Do"
        else:
            self.todos[index].status = "Done"
        self.updateList()

    def updateList(self):
        FONT_SIZE = 10
        for widget in self.todo_frame.winfo_children():
            widget.destroy()

        header_task_label = tk.Label(self.todo_frame, text = "Task", font=("Arial", FONT_SIZE, "bold"))
        header_status_label = tk.Label(self.todo_frame, text = "Status", font=("Arial", FONT_SIZE, "bold"))
        header_task_label.grid(row=0, column = 0, padx=10,pady=5,sticky="w")
        header_status_label.grid(row=0, column = 1, padx=10,pady=5,sticky="w")
        for i, todo in enumerate(self.todos):
            row_index = i + 1
            title_label = tk.Label(self.todo_frame, text=todo.title)
            title_label.grid(row=row_index, column=0, padx=10, pady=5, sticky='w')

            status_label = tk.Label(self.todo_frame, text=todo.status)
            status_label.grid(row=row_index, column=1, padx=10, pady=5, sticky='w')
            if todo.status == "To Do":
                toggle_text = "Mark Done"
            else:
                toggle_text = "Mark To Do"
            toggle_status_button = tk.Button(self.todo_frame, text = toggle_text, command=lambda i=i: self.toggleStatus(i)) 
            toggle_status_button.grid(row=row_index, column=2, padx=10, pady=5, sticky="w")

            delete_button = tk.Button(self.todo_frame, text = "Delete", command=lambda i=i: self.deleteTask(i))
            delete_button.grid(row=row_index, column=3, padx=10, pady=5, sticky="w")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ToDo App")
    root.geometry("800x600")
    app = ToDoApp(root, todos = [])
    root.mainloop()
    