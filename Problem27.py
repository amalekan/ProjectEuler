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

max_count = 0
max_prod = 0

for a in range(-999,1000):
    for b in range(-1000,1001):
        count = 0
        for n in range(0,1000):
            if((n**2 + a*n +b) < 2):
                break
            if(not isPrime(n**2 + a*n +b)):
                break
            else:
                count +=1
        if(count > max_count):
            max_count = count
            max_prod = a*b

print(max_count, max_prod)  
