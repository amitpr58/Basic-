
# Nth fibonacci number
# fn =fn-1 +fn-2
def Fibonacci(n):
    
    if n<=0:
        print("incorrect input")
    # first fibonacci number is 0
    elif n==1:
        return 0
    #second finonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

    #driver program

print(Fibonacci(5))  
