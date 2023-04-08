#calculator of two number
#withinput:
a=float(input("Enter a first number"))
b=float(input("Enter a Second number"))
c = int(input(
  "Enter 1 for addition\nEnter 2 for subtration\nEnter 3 for multiplication\nEnter 4 for division\n"))

#put any number 

if c==1:
    print(a+b)

elif c==2:
    print(a-b)

elif c==3:
    print(a*b)

elif c==4:
    print(a/b)
else:
  print("wrong choice")

    
"""print("addition of two number is", a +b)
print("subtration of two number is ", a-b )
print("multiplication of two number is", a*b)
print("division of two number is",a/b)
print("modular of two number is ", a//b)
"""


#without input:
"""a=56    
b=65
s=a+b
print(s)"""
