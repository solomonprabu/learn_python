arr = [54, 546, 548, 60]
arr.reverse()
res = ""

for i in arr:
    temp = 0 + i
    # print(temp)
    for c in map(int, str(temp)):
        # print(c)
        if c<10:
         res = res + str(c)
print(res)
