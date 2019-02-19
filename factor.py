from numpy import math

# Find the prime factorization of a number

def factor(number):

    factors = []

    for i in range(1, int(math.sqrt(number))+1):
        if number % i == 0:
            factors.append(i)
            factors.append(number / i)

    return factors
