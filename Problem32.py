products = set()
x = sorted('123456789')
for i in range(1,10000):
    for j in range(1,1000):
        if(sorted(str(i)+str(j)+str(i*j)) == x):
            print(i,j,i*j)
            products.add(i*j)
total = 0
for product in products:
    total += product

print(total)            
