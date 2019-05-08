from tkinter import ttk
from tkinter import *
from tkinter import filedialog

ch = False
def hello():
    global ch
    if not ch:
        b_lb2_var.set("Hello")
    else:
        b_lb2_var.set("")
    ch = not ch

def open_file():
    filename = filedialog.askopenfilename(filetypes=[("TEXT", 'txt')])
    if not filename:
        return
    with open(filename, 'r') as f:
        text = f.read()
    text_fr3.delete("1.0", END)
    text_fr3.insert("1.0", text)

def save_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if not filename:
        return
    text = text_fr3.get("1.0", END)
    with open(filename, mode='w') as f:
        f.write(text)

app = Tk()
app.geometry("400x400")
tab = ttk.Notebook(app)
fr1 = Frame(tab)
fr2 = Frame(tab)
fr3 = Frame(tab)
tab.add(fr1, text="tab1")
tab.add(fr2, text="tab2")
tab.add(fr3, text="cooltab")
tab.pack(expand=TRUE, fill=BOTH)
ph = PhotoImage(file="images/im1.png")
lb1 = Label(fr1, image=ph)
lb1.pack()
b_fr2 = Button(fr2, text="Hello", command=hello)
b_lb2_var = StringVar(fr2, "")
b_lb2 = Label(fr2, textvariable=b_lb2_var, text="")
b_fr2.grid(column=0, row=0)
b_lb2.grid(column=0, row=1)
b_lb3 = Button(fr3, text="Open", command=open_file)
b_lb3_2 = Button(fr3, text="Save", command=save_file)
text_fr3 = Text(fr3, width=40, height=10)
text_fr3.pack()
b_lb3.pack(side=LEFT, padx=(150, 10))
b_lb3_2.pack(side=LEFT)


app.mainloop()
