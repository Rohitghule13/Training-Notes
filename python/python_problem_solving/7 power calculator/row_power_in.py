try:
    a = int(input("Enter the number : "))
    b = int(input("Enter the power : "))
    print("result : ",a**b)
except BaseException:
    print("somthing went wrong please enter the number in integer ")