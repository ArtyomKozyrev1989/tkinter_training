from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def move_bar():
    pr.step(10)
    print(pr_v.get())
    if pr_v.get() == 0:
        a = messagebox.showerror("Done", "Really?")

app = Tk()
app.geometry("300x300")
b = Button(app, text="Hello", width=100, command=move_bar)
pr_v = DoubleVar()
pr = ttk.Progressbar(app, length=50, mode='determinate', variable=pr_v)
b.pack(fill=X)
pr.pack(fill=X)
app.mainloop()
