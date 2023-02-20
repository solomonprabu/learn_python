import array
listA = [91, 28, 34, 55, 76 , 55, 72, 45, 55, 45, 55, 45, 100]
arr = array.array('i',listA)

print("Count",listA.remove(55))
print("Count",listA.count(55))



listB = []
indexOfB =[]
x = listA.sort(reverse= True)
i = 0
for i in listA:
    listB.append(i)
    indeX = listB.index(i)
    rank = indeX +1
    if (i<=100):
        i = i+rank
        listA = i

print(listA)
