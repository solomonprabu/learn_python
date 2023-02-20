arr = [54, 546, 548, 60]

x = []
z = []

for i in arr:
    x.append(i)
    z.append(i)

x.sort()
print("Minimum element in the given array: ",x[0])

z.sort(reverse=True)
print("Maximum element in the given array: ",z[0])