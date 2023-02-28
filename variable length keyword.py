#variable length keyword argument
def f1(**k):
    print("person information")
    for key,value in k.items():
        print(key,"-",value)
f1(name="Amit", Age=23)
f1(name="Ajay",marks=85,age=21)
f1(name="RAm",empid=12345,salary=12500000.000)
