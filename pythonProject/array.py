import array

num = array.array('i', [1, 2, 3, 5, 2, 8, 7, 11, 2])
print(num)
num.reverse()
print(num[0], num[1])
num.append(10)
print(num.buffer_info()[1] * num.itemsize)
print("count",num.count(7))
print(num.extend(num))
print(num.tobytes())
print(num)
