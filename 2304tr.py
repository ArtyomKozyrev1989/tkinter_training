from tkinter import *
from tkinter import ttk

def get_all():
    name = entry_name.get()
    surname = entry_surname.get()
    if is_LOL.get() == 1:
        print(f"{name}___{surname}")
    else:
        print("Nothing!")
    if gender.get() == "man":
        print("MAN!!!")
    elif gender.get() == "woman":
        print("Woman!!!")
    elif gender.get() == "cat":
        print("I am cat!")
    else:
        print("What are you?")
    print(combo_choice.get())
    print(year.get())

m = Tk()
m.geometry("350x350")
label_name = Label(m, text="Put your name here: ")
label_surname = Label(m, text="Put your surname here:")
entry_name = Entry(m)
entry_name.insert(0, "Name")
entry_surname = Entry(m)
entry_surname.insert(0, "Surname")
b = Button(m, text="Fuuu!", bg="red", command=get_all)
is_LOL = IntVar(m)
is_LOL.set(0)
chb = Checkbutton(m, text="LOL?", variable=is_LOL)
gender = StringVar()
gender.set("")
r1 = Radiobutton(m, value="man", variable=gender, text="Male")
r2 = Radiobutton(m, value="woman", variable=gender, text="Female")
r3 = Radiobutton(m, value="cat", variable=gender, text="Cat")
combo_choice = StringVar()
combo_choice_list = []
for i in range(0,11):
    combo_choice_list.append(str(i))
cb = ttk.Combobox(m, textvariable=combo_choice, values=combo_choice_list, state="readonly") # pay attention did not find it in docs
year = StringVar()
spinyear = Spinbox(m, from_=1999, to=2015, textvariable=year, state="readonly")
label_name.grid(column=0, row=0, sticky=W, padx=20)
label_surname.grid(column=0, row=1, padx=20)
entry_name.grid(column=1, row=0, pady=10)
entry_surname.grid(column=1, row=1)
b.grid(column=1, row=2, sticky=W + E, ipady=20, pady=10)
chb.grid(column=1, row=3, sticky=W)
r1.grid(column=1, row=4,  sticky=W)
r2.grid(column=1, row=5,  sticky=W)
r3.grid(column=1, row=6,  sticky=W)
cb.grid(column=1, row=7,  sticky=W)
spinyear.grid(column=1, row=8,  sticky=W, pady=10)
m.mainloop()
