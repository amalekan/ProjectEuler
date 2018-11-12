squares = [i**2 for i in range(1,1000)]

from math import sqrt
pythagorean_triples = []
for a in squares:
    for b in squares:
        if a+b in squares:
            pythagorean_triples.append(tuple((int(sqrt(a)),int(sqrt(b)),int(sqrt(a+b)))))

sum_triplets = []
for x in pythagorean_triples:
    sum_triplets.append(sum(x))
from collections import Counter
cnt = Counter(sum_triplets)
print(cnt.most_common(5))
