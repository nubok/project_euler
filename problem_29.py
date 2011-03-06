s = set()

for a in range(2, 101):
    for b in range(2, 101):
        current = a**b
        if (current not in s):
            s.add(current)

print len(s)
