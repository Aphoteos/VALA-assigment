# Import Module
from tkinter import *
import prime_factor
import database
import save_file

# create root window
root = Tk()

# root window title and dimension
root.title("Prime factors finder")
# Set geometry(widthxheight)
root.geometry('450x250')

# adding a label to the root window
lbl = Label(root, text = "Give any positive natural number.")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =0, row =1)


# function to display user text when 
# button is clicked
def clicked():
    number = int(txt.get())
    factors, t1, found_database = prime_factor.find_prime_factors(number)
    # Save to output file
    save_file.save_to_ouput_file(number, factors, t1)
    # Save to database
    if found_database is False:
        factors = list(set(factors))
        database.database_csv().save_to_database(number, factors)
        factors = ', '.join(map(str,factors))
    
    #res = f'Prime factors for number {number} are {', '.join(map(str,factors))}\n time it took was {t1:.4f}'
    res = f'Prime factors for number {number} are {factors}\n time it took was {t1:.4f}'
    lbl.configure(text = res)
    

# button widget with red color text inside
btn = Button(root, text = "Click" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=0, row=2)

# Execute Tkinter
root.mainloop()