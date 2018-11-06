def isPalindrome(x):
    if len(x) == 0:
        return False
    if len(x) == 1:
        return True
    if len(x) == 2:
        return x[0] == x[1]
    else:
        return x[0] == x[-1:] and isPalindrome(x[1:-1])

def reverseAndAdd(n):
    m =int(str(n)[::-1])
    return m + n

count = 0

for n in range(1,10000):
    m=n
    for k in range(1,51):
        if(isPalindrome(str(reverseAndAdd(m)))):
            count += 1
            print(n, k, reverseAndAdd(m))
            break
        m = reverseAndAdd(m)

print(9999-count)    
