curr_sum = 0
prev_val = 1
curr_val = 1

while (curr_val < 4000000):
    if (curr_val % 2 == 0):
        curr_sum += curr_val
    (curr_val, prev_val) = (prev_val + curr_val, curr_val)

print curr_sum
