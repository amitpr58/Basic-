# frequency of tuple
A=(2,5,3,5,2,5,2,5,2,8,4,8,9,2,6,1)
print(A.count(5))
4
unique_A = set(A)
for item in unique_A:
    print(f" count of {item} in tuple A:{A.count(item)}")
