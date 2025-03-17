# Import Module
from tkinter import *
from scripts import prime_factor, database, save_file


class MainWindow:
    def __init__(self, parent):
        self.parent = parent

        # adding a label to the root window
        self.lbl = Label(self.parent, text = "Give any positive natural number.")
        self.lbl.grid()

        # adding Entry Field
        self.txt = Entry(self.parent, width=20)
        self.txt.grid(column =0, row =1)

        # button widget with red color text inside
        btn = Button(self.parent, text = "Click" ,
                     fg = "red", command=self.clicked)
        # Set Button Grid
        btn.grid(column=1, row=1)

    def clicked(self):
        # Validate input is a number 
        validate = prime_factor.validate_given_number(self.txt.get())
        if not validate:
            res = f'Given input is not a positive integer. Please use positive integers only!'
            self.lbl.configure(text = res)
            return
        
        # Change the given string input to integer
        number = int(self.txt.get())
        factors, t1, found_database = prime_factor.find_prime_factors(number)

        # Save to number, factors and time it took to find to a file
        file_name = save_file.save_to_ouput_file(number, factors, t1)

        # Save the info to database
        if found_database is False:
            factors = list(set(factors))
            database.databaseCsv().save_to_database(number, factors)
            factors = ', '.join(map(str,factors))

        # Style the text based on plurlar vs singular
        print(len(factors.split(',')))
        if len(factors.split(',')) > 1:
            factor_plular = 'factors'
            plular = 'are'
        else:
            factor_plular = 'factor'
            plular = 'is'

        res = f'Prime {factor_plular} for number {number} {plular} {factors}.\n' + \
            f'Time it took to find those was {t1:.4f}.\n' + \
            f'Crated a file {file_name} with the results.'
        self.lbl.configure(text = res)

def main():
    # create root window
    root = Tk()

    # root window title and dimension
    root.title("Prime factors finder")
    # Set geometry(widthxheight)
    root.geometry('400x250')
    
    MainWindow(root)
    # Execute Tkinter
    root.mainloop()

if __name__ == '__main__':
    main()