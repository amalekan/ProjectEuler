def isPalindrome(x):
    if len(x) <= 2:
        return x[:1] == x[-1:]
    if x[:1] == x[-1:]:
        return isPalindrome(x[1:-1])
    else:
        return False

total = 0

for x in range(1, 1000000):
    if(isPalindrome(str(x)) and isPalindrome(bin(x)[2:])):
        total += x

print(total)
