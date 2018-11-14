def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fac(n-1)

def digitFacSum(n):
    facSum = 0
    for c in str(n):
        facSum += fac(int(c))
    return facSum

cyclesWithLength60 = 0
for n in range (1,1000000):
    count = 1
    n_cycle = set()
    start = n
    n_cycle.add(start)
    while (digitFacSum(start) not in n_cycle):
        n_cycle.add(digitFacSum(start))
        count +=1
        start = digitFacSum(start)
    if count == 60:
        cyclesWithLength60 +=1
        print(n)
print(cyclesWithLength60)        
