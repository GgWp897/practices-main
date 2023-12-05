def Mygenerator():
    current = -100
    while True:
        if current > 100:
            current = -100
        if current % 2 == 0 and current % 5 == 0:
            yield current
        current += 1

count = 1

Mylist=Mygenerator()

for num in Mylist:
    if count > 15:
        break   
    print(num)
    count += 1

print(Mylist.__next__())


