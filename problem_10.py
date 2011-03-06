from euler_util import is_prime

print 2+sum([2*x+1 for x in range(1, 1000000) if is_prime(2*x+1)])
