from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def do_stuff():
    if give_name_surname.get() == 1:
        print(f"Name {e1.get()}, Surname {e2.get()}")
    else:
        print("N+S should be checked")
    s = sex.get()
    if s == 'male':
        print("Male")
    elif s == 'female':
        print("Female")
    else:
        print("Please choose you sex")

    chosen_country_index = country_listbox.curselection()
    if len(chosen_country_index) == 0:
        messagebox.showerror("Country", message="No country was chosen")
    else:
        for i in chosen_country_index:
            print(f"The chosen countries {country_opt[i]}")
    show_year = messagebox.askokcancel("Year", message="Do you want to see year?")
    if show_year:
        print(f"You was born in the year {year.get()}")
    x = textbox.get(1.0, END)
    print(x)



mw = Tk()
mw.geometry("300x500")
b = Button(mw, bg='red', text='Betton', command=do_stuff, pady=15).grid(column=1, row=9, sticky=W+E)
l1 = Label(mw, text="Name: ", pady=5).grid(column=0, row=0, sticky=W)
l2 = Label(mw, text="Syrname: ", pady=5).grid(column=0, row=1, sticky=W)
e1 = Entry(mw)
e2 = Entry(mw)
e1.insert(0, 'name')
e2.insert(0, 'surname')
e1.grid(column=1, row=0)
e2.grid(column=1, row=1)
give_name_surname = IntVar()
give_name_surname.set(0)
ch = Checkbutton(mw, variable=give_name_surname, text="Allow N + S").grid(column=1, row=2, sticky=W)
sex = StringVar()
sex.set("")
radio_male = Radiobutton(mw, text="Are you male? ", value="male", variable=sex).grid(column=1, row=3, sticky=W)
radio_female = Radiobutton(mw, text="Are you female? ", value="female", variable=sex).grid(column=1, row=4, sticky=W+E)
country = StringVar()
country.set("")
country_listbox = Listbox(mw, selectmode=MULTIPLE, listvariable=country)
country_opt = ['France', 'Armenia', 'Russia', 'Finland', 'Germany', 'England']
for i in country_opt:
    country_listbox.insert(END, i)
country_listbox.grid(column=1, row=5, sticky=W)
year = StringVar()
year_spinbox = Spinbox(mw, from_=1900, to=2019, textvariable=year, state="readonly")
year_spinbox.grid(column=1, row=6, sticky=W, pady=10)
textbox = Text(mw, width=20, height=5, pady=10, padx=50, wrap=WORD)
textbox.grid(column=0, row=7, sticky=W, columnspan=2)
mw.mainloop()
