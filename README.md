# VALA assigment - Prime factors

# Assigment:

THEORY:

A prime number is a natural number greater than 1 that has no positive divisors other 
than 1 and itself.
The prime factors of 26541 are 3, 3, 3, 983

TASK:

Create a program that take one number as an input from user via user interface. The 
programs task is to find all possible prime factors of that number, but not duplicates. It should 
print those numbers to screen and make an output file containing asked number and its prime 
factors.

To make it faster program should also make database file for already requested numbers, so 
there would not be need to make another search but get valid information from database. If 
this database file doesn’t exist, program should create it. Program should also output how long 
it took to calculate or get prime factors.

The content, syntax, name, style and etc. of database file can be freely decided by developer.
File name, UI look and feel can be freely chosen, but below is an example for simple 
(read minimal required implementation.)

Example UI:

    #>python prime_factors.py
    Give me the number: 26541
    Prime factor found: 3
    Prime factor found: 983
    It took 0,93 seconds to find those

Example output file content:

    Prime Factors of number 26541 are
    3, 983
    It took 0,93 seconds to find those

# How to Install

Used python standard libraries that comes with the full install of python.
- Install Python 3.13

# How to run:
You can use the program in two different mode: Clean GUI or command line.
To run this program use main.py.

To start GUI run:

        #> python main.py

Use from command line:

        #> python main.py <number>          e.g. python main.py 213451


# Contributors (code copied)
Prime factor calculation made by  Harshit Agrawal and improved by Sarthak Shrivastava:
https://www.geeksforgeeks.org/python-program-for-efficient-program-to-print-all-prime-factors-of-a-given-number/
