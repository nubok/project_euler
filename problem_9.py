# Since a < b < c and a+b+c = 1000 we get: a <= 332 
for a in range(1, 332+1):
    # Since a >= 1 and a+b+c = 1000, we get b <= 499 
    for b in range(a+1, 499):
        c = 1000-a-b
        if (c > b and a*a+b*b == c*c):
            print a, b, c
            print a*b*c
