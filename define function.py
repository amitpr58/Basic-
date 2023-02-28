#take nothing return something
def add():
    print("Enter any two number")
    a=eval(input())
    b=eval(input())
    s=a+b
    return s
x=add()
print("x=",x)
