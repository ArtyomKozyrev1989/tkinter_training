from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry("400x400")
subframe = Frame(app, width=300, bg="red", height=300, relief=SUNKEN, bd=5)
#subframe.grid(column=0, row=0, padx=100)
subframe.pack(fill=X)
button1 = Button(subframe, text="NNNNN", width=20).grid(column=0, row=0, pady=10, padx=10)
button2 = Button(subframe, text="YYYYYYYY", width=20).grid(column=1, row=0)
button3 = Button(subframe, text="12231233", width=20).grid(column=0, row=1, pady=10)
button4 = Button(subframe, text="LOL!!", width=20).grid(column=1, row=1)

labelsubframe = LabelFrame(app, text="Fuuuu", bg="yellow", padx=100, pady=100)

label = Label(labelsubframe, text="FU!!!")
label.pack()
labelsubframe.pack()


app.mainloop()
