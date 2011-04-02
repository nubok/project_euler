f_prev = 1
f_cur = 1
idx = 2

while (f_cur < 10**999):
    temp = f_cur
    f_cur = f_prev + f_cur
    f_prev = temp
    idx += 1

print idx
