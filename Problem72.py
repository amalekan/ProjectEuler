from math import gcd, sqrt

primes = [2]

def isPrime(n):
    for x in primes:
        if x > (sqrt(n)):
            return True
        if n%x == 0:
            return False

for k in range (3,1000000):
    if (isPrime(k)):
        primes.append(k)

def phi(n):
    if n == 1:
        return 1
    for p in primes:
        p_count = 0
        if(n%p == 0):
            while(n%p == 0):
                p_count +=1
                n = n/p
            return phi(n)*(p-1)*(p**(p_count-1))

total = 0

for n in range(2,1000001):
    total += phi(n)

print(total)
