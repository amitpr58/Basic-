class test:
    i=20
    def f1():
        print("Amit")

print(test.i)
test.f1()

class test:
    i=10
    def __init__(self):
        print("init")
    def f1():
        print("aaaaaa")
t1=test()
t2=test()
print(test.i)
test.f1()
class test:
    def __init__(self,x,y):
        self.a=x
        self.b=y

t1=test(3,4)
t2=test(20,45)
t3=test(50,57)
print(t1.a,t1.b)
print(t2.a,t2.b)
print(t3.a,t3.b)
