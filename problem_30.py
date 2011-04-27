from euler_util import *

# The fifth power of digits sum of a number having n digits is
# a(n) := 9^5 * n
# while the smallest number having n digits is
# b(n) := 10^(n-1)
# For n >= 7 we have
# a(n) < b(n)
# So we can have at most 6 digits

print sum([n for n in range(10, 10 ** 6) if n == sum([x ** 5 for x in digits(n)])])
