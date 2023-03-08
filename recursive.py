# Recursive
# sum of N number 
def sum(n):
    if (n==1):
        return 1
    else:
        return n+sum(n-1)
print( "sum of  n number")

# multiplication of n number
def multi(n):
    if (n==1):
        return 1
    else:
        return n*multi(n-1)
print("multiplication of number")

#input body
print(sum(10))
print(multi(5))
