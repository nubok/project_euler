from euler_util import *

max_digit_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        max_digit_sum = max(sum(digits(a**b)), max_digit_sum)

print max_digit_sum
