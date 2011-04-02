def d(n):
    return sum([x for x in range(1, n) if n % x == 0])

print sum([x for x in range(1, 10000) if d(x) != x and d(d(x)) == x])
