import tkinter as tk

root = tk.Tk()
root.title("first GUI app")
root.geometry("600x800")

label = tk.Label(root, text="Hello World", font=("Arial", 18))
label.place(relx=0.5,rely=0.5, anchor="center")

root.mainloop()
