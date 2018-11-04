count = 0
day = 1

for year in range(1901,2001):
    for month in range(1,13):
        if (month in list([1,3,5,7,8,10,12])):
            if day%7 == 6:
                count += 1
            day +=31
        if month == 2:
            if year%4 == 0:
                if day%7 == 6:
                    count += 1
                day +=29
            else:
                if day % 7 == 6:
                    count += 1
                day += 28
        if (month in list([4,6,9,11])):
            if day%7 == 6:
                count += 1
            day += 30

print(count)
                
