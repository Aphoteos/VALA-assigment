import math
import self_made_timer
import database

@self_made_timer.timer_func
def prime_factors(n: int) -> list:
    factors = []

    # number of two's that divide n
    while n % 2 == 0:
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):

        # while i divides n , print i ad divide n    
        while n % i == 0:
            print(i)
            factors.append(i)
            n = n // i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)
        factors.append(n)

    return factors
    
def find_prime_factors(number):
    found_database = False
    factors, t1 = database.database_csv().search_from_database(number)
    if factors:
        print(f'Found factors for number {number} from databse.')
        print(factors)
        found_database = True
    else:
        print(f'Did NOT found {number} from databse.')
        factors, t1 = prime_factors(number)

    print(found_database)
    return factors, t1, found_database

if __name__ == "__main__":
    number = 142534
    find_prime_factors(number)