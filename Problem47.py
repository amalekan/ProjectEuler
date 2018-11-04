from math import sqrt
primes = [2]
def isPrime(n):
    for x in primes:
        if x > (sqrt(n)):
            return True
        if n%x == 0:
            return False

for k in range (3,100000):
    if (isPrime(k)):
        primes.append(k)

def pcount(n):
    count = 0
    for p in primes:
        if n ==1:
            break
        if(n%p == 0):
            count += 1
            while(n%p == 0):
                n = n/p

    return count

for k in range(646,1000000):
    if pcount(k) == 4:
        if pcount(k+1) == 4:
            if pcount(k+2) == 4:
                if pcount(k+3) == 4:
                    print(k)
                    break
