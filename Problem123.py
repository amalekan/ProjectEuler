from math import sqrt, ceil
primes = [2]
def isPrime(n):
    for k in range(2,1+ ceil(sqrt(n))):
        if n%k == 0:
            return False
    return True

for m in range(2,1000000):
    if(isPrime(m)):
        primes.append(m)

for n in range(7036,78497):
    if((((primes[n]-1)**(n+1) + (primes[n]+1)**(n+1))% primes[n]**2) > 10**10):
        print(n+1)
        break
