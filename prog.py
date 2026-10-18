import tkinter as tk

def add_digit(digit):
    value = entry.get() + str(digit)
    entry.delete(0, tk.END)
    entry.insert(0, value)

def add_operation(op):
    value = entry.get()
    if value and value[-1] in "+-*/":
        value = value[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, value + op)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=20, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, col) in buttons:
    if text.isdigit() or text == ".":
        action = lambda x=text: add_digit(x)
    elif text in "+-*/":
        action = lambda x=text: add_operation(x)
    elif text == "=":
        action = calculate
    elif text == "C":
        action = clear

    tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
              command=action).grid(row=row, column=col)

root.mainloop()
