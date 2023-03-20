# handling
#Raise concepts
class InsufficientBalance (ZeroDivisionError):
    def __init__(self,arg):
        self.msg=arg
Balance=8000
W=int(input("Enter amount to withdrow the money"))
try:
    if W>Balance:
        raise InsufficientBalance("Insufficient Balancein the Account")
    Balance=Balance-W
except InsufficientBalance as i:
    print("Exception",i.msg)
else:
    print("Withdraw amount",W,"successfully" )
finally:
    print("Current Balance is ",Balance)
