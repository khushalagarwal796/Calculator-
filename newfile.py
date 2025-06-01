from tkinter import *

# Create the main window
root = Tk()
root.title("Calculator")

# Create the entry field
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# Function to handle operators
def operator_click(operator):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(operator))

# Function to handle equals
def equals_click():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Function to handle clear
def clear_click():
    entry.delete(0, END)

# Create the buttons
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: operator_click("/"))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: operator_click("*"))

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: operator_click("-"))

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_decimal = Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."))
button_equals = Button(root, text="=", padx=40, pady=20, command=equals_click)
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: operator_click("+"))

button_clear = Button(root, text="C", padx=29, pady=20, command=clear_click)

# Place the buttons on the grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_decimal.grid(row=4, column=1)
button_equals.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_clear.grid(row=5, column=0, columnspan=4)

root.mainloop()