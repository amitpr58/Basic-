#useing while else to find the number you want

i=1
while i<=3:
    x=int(input("Enter an Even number"))
    if x%2==0:
        print("you Win")
        break
    i=i+1
else:
    print("you lost")
