listA = [11, 2, -2, 2, 34, 76 , 55, 7, -4, 2, 100, 154, -32, -4, -12]
pos = 0
neg = 0
dup = 0

for i in listA:
    if i<0:
        print("Negative numbers in the List are: ",i)
for i in listA:
    if i>0:
        print("Positive numbers in the list are: ",i)

for i in range(-10,10):
    if i<0:
        pos+=1
        print(i)
print("Number of negative numbers",pos)

for i in range(-10,10):
    if i>0:
        neg+=1
        print(i)
print("Number of positive numbers",neg)

for i in listA:
    if i == i:

        dup+=1
        print("Duplicates",dup)