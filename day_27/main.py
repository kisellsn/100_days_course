from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=100, height=50)
window.config(padx=50, pady=50)


#Labels
label = Label(text="is equal to")
label.grid(column=0, row=1)

#Entries
entry = Entry(width=30)
# entry.insert(END, string="miles")
entry.config(width=10)
entry.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)



result = Label(text="")
result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def calculate():
    ml = entry.get()
    km = float(ml) * 1.6
    result.config(text=str(int(km)))

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



window.mainloop()
