def digitSum(n):
    digit_sum = 0
    for c in str(n):
        digit_sum += int(c)
    return digit_sum
    
seq = set([])
for n in range(2, 100):
    for k in range(1,50):
        if digitSum(n**k) == n and len(str(n**k)) > 2:
            seq.add(n**k)
sorted(seq)[29]
