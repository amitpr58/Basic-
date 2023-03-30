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
