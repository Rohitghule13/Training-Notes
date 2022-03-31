try:
    a = int(input("Enter the first Number "))
    b = int(input("Enter the second Number "))
    print(a+b)
except BaseException:
    print("somthing went wrong please enter the integer number only")
