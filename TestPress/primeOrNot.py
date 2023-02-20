num = int(input("enter no: "))
if num == 1:
    print("Not a Prime number")
elif num>1:
    for i in range(2,num):
        if(num % i)==0:
            print("Not a prime number")
            break
        else:
            print("Prime number")
            break
else:
    print("Prime number")