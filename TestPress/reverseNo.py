x = int(input("Enter a number within 10000 : "))
y = ""
if 0<x<10000:
        for i in str(x):
            if 1 < x < 10000:
                if x != 0:
                    y = str(i) + y
else:
    print("Enter a valid input")
    print("result: ",int(y))