abundant_numbers = []

for n in range (1,28123):
    total = 0

    for k in range(1,n):
        if n%k == 0:
            total += k
    if total > n:
        abundant_numbers.append(n)

sums = set([])

for x in abundant_numbers:
    for y in abundant_numbers:
        if(x+y <28124):
            sums.add(x+y)

non_abundant_sum = 0

for x in range(1,28124):
    if (x not in sums):
        non_abundant_sum += x

print(non_abundant_sum)
