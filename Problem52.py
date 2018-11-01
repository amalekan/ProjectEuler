from collections import Counter
def is_permutation(a,b):
    return len(a) == len(b) and Counter(a) == Counter(b)

for n in range(1,1000000):
    if(is_permutation(str(n), str(2*n)) and is_permutation(str(n), str(3*n)) and is_permutation(str(n),str(4*n)) and is_permutation(str(n), str(5*n)) and is_permutation(str(n), str(6*n))):
        print(n)
        break
