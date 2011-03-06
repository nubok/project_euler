from fractions import Fraction
from euler_util import *

e = [Fraction(0, 1)]

for n in range(1, 33):
    temp_sum = Fraction(1, 2)**n+sum([binomial(n, i)*(Fraction(1, 2)**n)*(1+e[i]) for i in range(0, n)])
    next_e = Fraction(2**n, 2**n-1) * temp_sum
    e.append(next_e)

print float(e[32])
