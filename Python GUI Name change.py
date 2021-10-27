import tkinter as tk
from tkinter import *


def show_the_path():
    print("Path of product file: %s\nPath of RC file: %s\nPath of Company_naming_convention: %s" % (
    e1.get(), e2.get(), e3.get()))


root = tk.Tk()
root.title('Geography Mapping')
w = Canvas(root, width=100, height=100)
tk.Label(root, text="Path of product file").grid(row=0)
tk.Label(root, text="Path of RC File").grid(row=1)
tk.Label(root, text="Path of Company_naming_convention").grid(row=2)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(root, text="Upload", command=root.destroy).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(root, text="Execute", command=root.destroy).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.Button(root, text="Download", command=root.destroy).grid(row=3, column=2, sticky=tk.W, pady=4)

tk.mainloop()