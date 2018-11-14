def digitSquareSum(n):
    squareSum = 0
    for c in str(n):
        squareSum += int(c)**2
    return squareSum

cyclesWith89 = 0
for n in range (1,10000000):
    start = n
    while (start != 1 and start != 89):
        start = digitSquareSum(start)
    if start == 89:
        cyclesWith89 +=1
print(cyclesWith89) 
