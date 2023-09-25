import math
import tkinter as tk

def evaluate_expression():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

def append_to_entry(value):
    entry.insert(tk.END, value)

def calculate_square_root():
    expression = entry.get()
    try:
        result = math.sqrt(float(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_trigonometric(func):
    expression = entry.get()
    try:
        angle = math.radians(float(expression))
        result = func(angle)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Smart Scientific Calculator")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = tk.Button(root, text="1", command=lambda: append_to_entry("1"))
button_2 = tk.Button(root, text="2", command=lambda: append_to_entry("2"))
button_3 = tk.Button(root, text="3", command=lambda: append_to_entry("3"))
button_4 = tk.Button(root, text="4", command=lambda: append_to_entry("4"))
button_5 = tk.Button(root, text="5", command=lambda: append_to_entry("5"))
button_6 = tk.Button(root, text="6", command=lambda: append_to_entry("6"))
button_7 = tk.Button(root, text="7", command=lambda: append_to_entry("7"))
button_8 = tk.Button(root, text="8", command=lambda: append_to_entry("8"))
button_9 = tk.Button(root, text="9", command=lambda: append_to_entry("9"))
button_0 = tk.Button(root, text="0", command=lambda: append_to_entry("0"))
button_dot = tk.Button(root, text=".", command=lambda: append_to_entry("."))
button_equal = tk.Button(root, text="=", command=evaluate_expression)
button_clear = tk.Button(root, text="C", command=clear_entry)
button_sqrt = tk.Button(root, text="√", command=calculate_square_root)
button_sin = tk.Button(root, text="sin", command=lambda: calculate_trigonometric(math.sin))
button_cos = tk.Button(root, text="cos", command=lambda: calculate_trigonometric(math.cos))
button_tan = tk.Button(root, text="tan", command=lambda: calculate_trigonometric(math.tan))

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
root.mainloop()