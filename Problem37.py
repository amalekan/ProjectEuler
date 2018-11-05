from math import sqrt
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

prime_sum = 0
count = 0

def isLeftPrime(n):
    if len(str(n)) == 1 and n in primes:
        return True
    if n in primes:
        return isLeftPrime(int(str(n)[1:]))
    else:
        return False

def isRightPrime(n):
    if len(str(n)) == 1 and n in primes:
        return True
    if n in primes:
        return isRightPrime(int(str(n)[:-1]))
    else:
        return False

for n in primes[4:]:
    if (isLeftPrime(n) and isRightPrime(n)):
        prime_sum += n
        count += 1
        print(n)

print(count, prime_sum)
