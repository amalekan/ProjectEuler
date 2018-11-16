from fractions import Fraction
from math import log10

def f(n, x):
    if n==0:
        return Fraction(3,2)
    
    if n == 1:
        return 1 + Fraction(1, x+2)
    
    return f(n-1, Fraction(1, x + 2))

count = 0

for n in range(0,1000):
    if int(log10(f(n,Fraction(1,2)).numerator)) > int(log10(f(n,Fraction(1,2)).denominator)):
        count +=1
print(count)   
