import tkinter as tk

root = tk.Tk()
root.title("Hello, World!")
root.minsize(200, 200)

label = tk.Label(root, text="Hello, World")
label.pack()

root.mainloop()
