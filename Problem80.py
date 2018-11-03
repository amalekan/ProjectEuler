from decimal import *
getcontext().prec = 108

sqrt_nums = []

for n in range(1,100):
    sqrt_nums.append(Decimal(n).sqrt())

total = 0
for x in sqrt_nums:
    if str(x%1) == '0':
        continue
    for y in str(x)[:-8]:
        if y == '.':
            continue
        total += int(y)
print(total)     
