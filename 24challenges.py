##1. Create a GUI application that finds simple interest. Simple Interest (SI) = (P * R * T) /
##100 Where:
##● P = Principal amount ,● R = Rate of interest , ● T = Time

import tkinter as tk

def calculate_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    
    interest = (principal * rate * time) / 100
    result_label.config(text=f"Simple Interest: {interest:.2f}") 

root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("400x200")

principal_label = tk.Label(root, text="Principal Amount:")
principal_label.pack()

principal_entry = tk.Entry(root)
principal_entry.pack()

time_label = tk.Label(root, text="Time (years):")
time_label.pack()

time_entry = tk.Entry(root)
time_entry.pack()

rate_label = tk.Label(root, text="Rate of Interest:")
rate_label.pack()

rate_entry = tk.Entry(root)
rate_entry.pack()


calculate_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()


