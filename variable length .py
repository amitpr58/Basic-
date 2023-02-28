#variable length argument
def avg (*n):
    s=0
    for x in n:
        s=s+x
    return s/len(n)
x=avg(10,20,30)
print("Average is" ,x)
