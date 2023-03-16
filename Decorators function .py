#Decorators function 
def decor_result(result_function):
    def distinction (marks):
        for m in marks:
            if m >=75:
                print("congrats!!, You have got distinction")
        else:
            result_function (marks)
    return distinction
@decor_result


def result ( marks):
    for m in marks:
        if m>=33:
            pass #students
        else:
            print("Fail student")
    else:
        print("Pass students")

result([45,48,92,65,45,76])
