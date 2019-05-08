from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def print_text_from_radio():
    a = r_value.get()
    if a:
        messagebox.showinfo("shaddy", "hello {}".format(a))
    r_value.set(NONE)

def hello():
    if x.get() == 1:
        l1.config(text="LOLOLO")
        hiden_b.grid(column=3, row=0)
    else:
        l1.config(text="Hello")
        hiden_b.grid_remove()

def bye():
    a = y.get()
    if a:
        l2.config(text=a)
    else:
        l2.config(text="Bye")
    y.set("")

def say_list():
    x = lb.curselection()
    h = []
    for i in x:
        h.append(listbox_list[i])
    if x:
        messagebox.showinfo("Counries", "The following countries were selected {}".format(h))

listbox_list = ("It", "Fr", "USA", "Deu", "Aus", "Mag", "X1", "E", "Z", "DD", "QQ", "DD")

def get_textbox():
    y = some_text_box.get(1.0, END)
    print(y)
    if y:
        l1.config(text=y)
        messagebox.showinfo("textbox", y + sp_v.get() + " " + cb_var.get())

def frame_b():
    x = my_frame_e1_var.get()
    y = my_frame_e2_var.get()
    messagebox.showinfo("frame_textbox", x + " " + y)


app = Tk()
app.geometry('500x700')

l1 = Label(app, text="Hello")
l2 = Label(app, text="Bye")
b1 = Button(app, text="X", command=hello, width=20)
b2 = Button(app, text="Y", command=bye)
b3 = Button(app, text="Country", command=say_list)
b4 = Button(app, text="Country", command=get_textbox)
x = IntVar(app, value=0)
ch = Checkbutton(app, variable=x)
y = StringVar(app, "")
e = Entry(app, textvariable=y)
hiden_b = Button(app, text="Type", command=print_text_from_radio)

r_value = StringVar(app, value="man")
r1 = Radiobutton(app, value="man", variable=r_value, text="M")
r2 = Radiobutton(app, value="woman", variable=r_value, text="W")
r3 = Radiobutton(app, value="lol", variable=r_value, text="L")

lb_v = StringVar(app)
yScroll = Scrollbar(orient=VERTICAL)
lb = Listbox(app, selectmode=MULTIPLE, listvariable=lb_v, height=8, yscrollcommand=yScroll.set)
yScroll['command'] = lb.yview
for i in listbox_list[::-1]:
    lb.insert(0, i)

some_text_box = Text(app, width=40, height=10, wrap=WORD)

sp_v = StringVar()
sp = Spinbox(app, values=('red', 'blue', 'green', "dark", "bright", "orange"), textvariable=sp_v,
             state='readonly')

cb_var = StringVar(app)
cb = ttk.Combobox(app, textvariable=cb_var, values=('red', 'blue', 'green', "dark", "bright", "orange"),
                  state='readonly')

my_frame = Frame(app, width=400, height=400, bg="red", bd=3, relief=SUNKEN)
my_frame_e1_var = StringVar(my_frame)
my_frame_e1 = Entry(my_frame, textvariable=my_frame_e1_var)
my_frame_e2_var = StringVar(my_frame)
my_frame_e2 = Entry(my_frame, textvariable=my_frame_e2_var)
ph = PhotoImage(file="images/im1.png")
my_frame_b = Button(my_frame, image=ph, command=frame_b, cursor="pirate", activeforeground="yellow", bd=4)
Label(my_frame, image=ph).grid(column=0, row=1, sticky=W+E, padx=10)

b1.grid(column=0, row=0, padx=10, pady=10, sticky=E+W)
l1.grid(column=1, row=0, sticky=E)
b2.grid(column=0, row=1, sticky=W+E, padx=10, pady=10)
l2.grid(column=1, row=1)
ch.grid(column=2, row=0)
e.grid(column=1, row=3)
r1.grid(column=0, row=4, sticky=E+W, padx=10, pady=10)
r2.grid(column=1, row=4, sticky=E+W, padx=10, pady=10)
r3.grid(column=2, row=4, sticky=E+W, padx=10, pady=10)
lb.grid(column=1, row=5)
b3.grid(column=0, row=5)
yScroll.grid(row=5, column=2, sticky=N+S)
some_text_box.grid(row=6, column=0, pady=10, padx=10, columnspan=2)
b4.grid(column=0, row=7)
sp.grid(column=0, row=8)
cb.grid(column=1, row=8)
my_frame.grid(column=0, row=9, columnspan=2, sticky=W, pady=20, padx=10)
my_frame_e1.grid(column=0, row=0, padx=10, pady=10)
my_frame_e2.grid(column=1, row=0, padx=10)
my_frame_b.grid(column=1, row=1, sticky=E, padx=10, pady=10)

#l1.pack()
#l2.pack()
#b1.pack()
#b2.pack()
#ch.pack()
#e.pack()
app.mainloop()
