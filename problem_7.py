from euler_util import *

def nth_prime(n):
    currentNumber = 1;
    currentPrimeIndex = 1;

    if (n==1):
        return 2
    
    while True:
        if (is_prime(currentNumber)):
            currentPrimeIndex+=1
            if (currentPrimeIndex == n):
                return currentNumber
        currentNumber+=2

print nth_prime(10001)
