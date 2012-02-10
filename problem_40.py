num_str = "";

for i in range(1000000):
    num_str = num_str + str(i)

prod = 1;

for i in range(0, 7):
    prod = prod * int(num_str[10**i])

print prod
