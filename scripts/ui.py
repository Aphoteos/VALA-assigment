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
root.geometry('350x250')

# adding a label to the root window
lbl = Label(root, text = "Give any positive natural number.")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =0, row =1)


# function to display user text when 
# button is clicked
def clicked():
    # Validate input is a number 
    validate = prime_factor.validate_given_number(txt.get())
    if not validate:
        res = f'Given input is not a positive integer. Please use positive integers only!'
        lbl.configure(text = res)
        return
    
    # Change the given string input to integer
    number = int(txt.get())
    factors, t1, found_database = prime_factor.find_prime_factors(number)

    # Save to number, factors and time it took to find to a file
    save_file.save_to_ouput_file(number, factors, t1)

    # Save the info to database
    if found_database is False:
        factors = list(set(factors))
        database.database_csv().save_to_database(number, factors)
        factors = ', '.join(map(str,factors))

    # Style the text based on plurlar vs singular
    print(len(factors.split(',')))
    if len(factors.split(',')) > 1:
        factor_plular = 'factors'
        plular = 'are'
    else:
        factor_plular = 'factor'
        plular = 'is'

    res = f'Prime {factor_plular} for number {number} {plular} {factors}\n Time it took to find those was {t1:.4f}'
    lbl.configure(text = res)
    

# button widget with red color text inside
btn = Button(root, text = "Click" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=0, row=2)

# Execute Tkinter
root.mainloop()