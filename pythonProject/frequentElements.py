# frequency = input(input("Enter the frequency value: "))
li1 = [1,2,3,3,2,4,5,6,7,8,9,6,2,5,6,3,2,7]
li2= []
k = 3
for i in li1:
    if i not in li2:
        li2.append(i)
for n in li2:
    res = li1.count(n)
    print(n , " : " ,res)
