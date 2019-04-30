from tkinter import *
from tkinter import ttk
import os

print(os.getcwd())

app = Tk()
app.geometry("600x600")

pf = ttk.PanedWindow(app, orient=HORIZONTAL)
pf.pack(expand=True, fill=BOTH)
fr1 = Frame(pf, width=300, height=500, relief=SUNKEN, bd=1)
fr2 = Frame(pf, width=300, height=500, relief=SUNKEN, bd=1)
pf.add(fr1, weight=1)
pf.add(fr2, weight=3)
l1 = Label(fr1, text="Chita").pack()
l2 = Label(fr2, text="Hello").pack()
l3 = Label(fr2, text="Bye").pack()
l4 = Label(fr2, text="Hey").pack()
l5 = Label(fr2, text="Wait").pack()


app.mainloop()
