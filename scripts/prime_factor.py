import math
import sys
from scripts import self_made_timer, database, save_file


@self_made_timer.timer_func
def calculate_prime_factors(number: int) -> list:
    '''Claculate prime factors for a given number'''
    factors = []
    
    # number of two's that divide n
    while number % 2 == 0:
        factors.append(2)
        number = number // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(number))+1,2):

        # while i divides n , print i ad divide n    
        while number % i == 0:
            print(i)
            factors.append(i)
            number = number // i

    # Condition if number is a prime
    # number greater than 2
    if number > 2:
        print(number)
        factors.append(number)

    return factors
    
def find_prime_factors(number):
    '''Finds factors for a given number. 
    Check database first and then calculate if not found'''
    found_database = False
    
    #Check database
    factors, t1 = database.databaseCsv().search_from_database(number)
    if factors:
        print(f'Found factors for number {number} from database.')
        print(factors)
        found_database = True
    # If not found from database calculate
    else:
        print(f'Did NOT found {number} from databse.')
        factors, t1 = calculate_prime_factors(number)

    print(found_database)
    return factors, t1, found_database

def validate_given_number(number: int):
    '''Validate if the given number is a positive number'''
    try:
        value = int(number)
    except ValueError:
        return False
    
    # Check number is positive
    if int(number) < 0:
        return False
    else:
        return True

def command_line_prime_factors(number):
    number = int(number)
    validate = validate_given_number(number)
    if not validate:
        print(f'Your input is not positive number. \nGiven input was: {number}')
        sys.exit()

    factors, t1, found_database = find_prime_factors(number)

    # Save to number, factors and time it took to find to a file
    file_name = save_file.save_to_ouput_file(number, factors, t1)

     # Save the info to database
    if found_database is False:
        factors = list(set(factors))
        database.databaseCsv().save_to_database(number, factors)
        factors = ', '.join(map(str,factors))

    # Output result
    print(f'Factors: {factors}. \nTime it take: {t1:.4f}.')
    print(f'Created file {file_name} with the results.')
