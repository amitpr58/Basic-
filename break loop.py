#cheak tne is even  for 3 time
chance=1
while chance<=3:
    x=int(input("enter a Even number"))
    if x%2==0:
        break
    chance += 1
if chance ==4:
    print("you lost")
else:
    print("you win")
