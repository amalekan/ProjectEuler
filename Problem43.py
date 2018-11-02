from itertools import permutations
perms = [''.join(p) for p in permutations('0123456789')]

total = 0

for x in range(362880,3628800):
    if(int(perms[x][1:4]) % 2 != 0):
        continue
    if(int(perms[x][2:5]) % 3 != 0):
        continue
    if(int(perms[x][3:6]) % 5 != 0):
        continue
    if(int(perms[x][4:7]) % 7 != 0):
        continue
    if(int(perms[x][5:8]) % 11 != 0):
        continue
    if(int(perms[x][6:9]) % 13 != 0):
        continue
    if(int(perms[x][7:]) % 17 != 0):
        continue
    total+=int(perms[x])
print(total)
