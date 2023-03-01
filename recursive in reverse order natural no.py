# recursive function to print first N natural number in python progam.
def printNumber(n):
    #cheak if n is greater than zero/0
    if n>0:
        #recursively call print number function
       
        print(n,end=' ')
        printNumber(n-1)
        
n=20
printNumber(n)
