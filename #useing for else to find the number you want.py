#useing for else to find the number you want
a=int(input("Enter smaller number"))
b=int(input("Enter greater number"))
s=range(a,b)
for x in s:
    for num in range (2,x):
        if x%num==0:
            break
    else:
        print(x,"is a prime in range")
