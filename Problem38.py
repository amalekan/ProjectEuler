max_pandigital = 0
y = sorted('123456789')
for k in range (1,6):
    for i in range(1,10001):
        result = [i*j for j in range(1,k)]
        num = ""
        for x in result:

            num += str(x)
        if sorted(num) == y:
            max_pandigital = max(int(num), max_pandigital)

print(max_pandigital)            
