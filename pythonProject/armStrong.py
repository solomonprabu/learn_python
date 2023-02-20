n = int(input("Enter a number"))
s = n
b = len(str(n))
sum = 0

while n != 0:
    r = n % 10
    print("printing r", r)
    sum = sum + (r**b)
    print("printing sum", sum)
    n = n//10
    print("printing n", n)
if s == sum:
    print("The entered number is an armstrong number")
else:
    print("The entered number is NOT an armstrong number")