twice_squares = [2*(i**2) for i in range(1,5000)]
from math import sqrt
primes = [2]
def isPrime(n):
    for x in primes:
        if x > (sqrt(n)):
            return True
        if n%x == 0:
            return False

for k in range (3,10000):
    if (isPrime(k)):
        primes.append(k)

numbers_that_sum = set([x + y for x in primes for y in twice_squares])

x = sorted(numbers_that_sum)

for y in range(9,10000,2):
    if y in primes:
        continue
    if y not in x:
        print(y)
        break
