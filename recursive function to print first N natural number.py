# recursive function to print first N natural number in python progam.
def printNumber(n):
    #cheak if n is greater than zero/0
    if n>0:
        #recursively call print number function
        printNumber(n-1)
        print(n,end=' ')
        
n=20
printNumber(n)
