from math import *

def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1), 1)

def binomial(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, sqrt(n)+1):
        if (n % i == 0):
            return False
    return True

def digits(n):
    return [int(x) for x in str(n)]
