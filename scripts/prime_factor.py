import math
import self_made_timer
import database
import sys

@self_made_timer.timer_func
def prime_factors(number: int) -> list:
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
    found_database = False
    factors, t1 = database.database_csv().search_from_database(number)
    if factors:
        print(f'Found factors for number {number} from database.')
        print(factors)
        found_database = True
    else:
        print(f'Did NOT found {number} from databse.')
        factors, t1 = prime_factors(number)

    print(found_database)
    return factors, t1, found_database

def validate_given_number(number: int):
    # Check if the given number is number at all
    try:
        value = int(number)
    except ValueError:
        return False
    
    # Check number is positive
    if int(number) < 0:
        return False
    else:
        return True

if __name__ == "__main__":
    number = '-1'
    validate = validate_given_number(number)
    if not validate:
        print(f'Your input is not positive number. \nGiven input was: {number}')
        sys.exit()

    factors, t1, found_database = find_prime_factors(number)