##GUI for to do list

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

tasks = []

def add_task():
    task = entry.get()
    if task.strip():
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except IndexError:
        pass


main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True, fill="both")


entry = ttk.Entry(main_frame, font=("Arial", 12))
entry.pack(pady=10, fill="x")


button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=10, fill="x")


add_btn = ttk.Button(button_frame, text="Add Task", command=add_task)
add_btn.pack(side="left", padx=5)

delete_btn = ttk.Button(button_frame, text="Delete Task", command=delete_task)
delete_btn.pack(side="left", padx=5)


listbox = tk.Listbox(
    main_frame,
    font=("Arial", 12),
    height=15,
    selectbackground="#e6e6e6",
    relief="flat"
)
listbox.pack(expand=True, fill="both")

root.mainloop()