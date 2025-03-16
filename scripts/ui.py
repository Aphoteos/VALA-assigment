# Import Module
from tkinter import *
import scripts.prime_factor as prime_factor

# create root window
root = Tk()

# root window title and dimension
root.title("Prime factors finder")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text = "Give any positive natural number.")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)


# function to display user text when 
# button is clicked
def clicked():
    number = int(txt.get())
    factors, t1 = prime_factor.primeFactors(number)
    #print(f'Prime factors for number {n} are {list(set(factors))}')
    res = f'Prime factors for number {number} are {list(set(factors))}\n time it took was {t1:.4f}'
    lbl.configure(text = res)

# button widget with red color text inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.mainloop()