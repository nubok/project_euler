
def collatz_len(n):
    length = 1
    while (True):
        if (n==1):
            return length
        if (n % 2) == 0:
            n /= 2
        else:
            n = 3*n+1
        length+=1

max_collatz_len = 0
max_start_number = 0

for i in range(1, 1000000):
    col_len = collatz_len(i)
    
    if (col_len > max_collatz_len):
        max_collatz_len = col_len
        max_start_number = i

print max_start_number, max_collatz_len
