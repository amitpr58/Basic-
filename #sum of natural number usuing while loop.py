#sum of natural number
num = float(input("enter the number"))

if num <= 0 :
      print("enter the positive number")
else:
      sum=0
      #used while loop
      while(num > 0):
        sum += num
        num -= 1
      print("the sum is",sum)
