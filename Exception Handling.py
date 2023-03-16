# Exception Handling
x=float(input("number"))
y=float(input("2nd number"))
try:
    A=x/y
    print("division result",A)
#except:
 #   print("Default Exception")
except (ZeroDivisionError,ValueError,TypeError):
    print("wrong input")
#except ValueError :
 #   print("value error")
 except:
    print("Default Exception")
finally:
    print("in finally")
#except:
 #   print("Default Exception")
    
#print("division result",x/y)
print("Amit \n prajapati")
