listA = [11, 2, 2, 2, 34, 76 , 55, 7, 2, 100, 154]
count = 0
add = 0
print(listA)

# swapping two elements in a list
listA[1], listA[-2] = listA[-2], listA[1]
print(listA)
for i in listA:
    if (i == 2):
        count = count + 1
add = add + i

print("The total occurence of the NO: 2 is ",count)
print("The total sum of the list is: ",add)

# print("cleared list: ", listA.clear())
print("-------------------------------End of Program---------------------------------------")


# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# printing original lists
print("The original list is : " + str(test_list))

result = ', '.join(test_list)
print("Joined list: ",result)

result = result.replace("e","o").split(',')
print("swapped results: "+ str(result))
print("-------------------------------End of Program---------------------------------------")

