from math import sqrt
primes = [2]
def isPrime(n):
    for x in primes:
        if x > (sqrt(n)):
            return True
        if n%x == 0:
            return False

for k in range (3,10000000):
    if (isPrime(k)):
        primes.append(k)

for x in primes:
    if(x > 1000000):
        if (sorted(str(x)) == sorted('1234567')):
            print(x)
