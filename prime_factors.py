from numpy import math
from factor import *

# Find the prime factorization of a number

def prime_factor():

    number = input("Number: ")
    factors = factor(number)
    prime_factors = []

    for number in factors:
        # test for primality
        test = factor(number)
        if len(test) == 2:
            prime_factors.append(number)

    print(prime_factors)
    return prime_factors


# Works, but could make it better by removing duplicates and 1's
prime_factor()
