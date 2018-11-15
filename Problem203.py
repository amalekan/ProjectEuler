import operator as op
from functools import reduce
from math import sqrt

primes = [2]

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom

def isPrime(n):
    for x in primes:
        if x > (sqrt(n)):
            return True
        if n%x == 0:
            return False

for k in range (3,10000000):
    if (isPrime(k)):
        primes.append(k)

binom_coeffs = set([])

for n in range (0, 51):
    for r in range(0,n+1):
        binom_coeffs.add(ncr(n,r))


prime_free_sum = 0

for x in binom_coeffs:
    for p in primes:
        if p > sqrt(x):
            break
        if x % p**2 == 0:
            prime_free_sum -= x
            break
    prime_free_sum += x

print(prime_free_sum)
