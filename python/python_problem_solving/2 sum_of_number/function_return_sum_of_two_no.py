def addtoNumber(a, b):
    return a+b


try:
    a = int(input("Enter the first number "))
    b = int(input("Enter the second number "))
    print(addtoNumber(a, b))
except BaseException:
    print("somthing went wrong please enter the integer number only")
