li1 = [1,2,3,3,2,4,5,6,7,8,9,6]
product = 1
li2=[]
for i in li1:
   if i not in li2:
       li2.append(i)
print(li2)
print(len(li2))

#Next problem find the product of the original items
for i in li2:
    product = product * i

print(product)