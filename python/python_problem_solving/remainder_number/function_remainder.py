def remainder(a, b):
    print("reminder ", a % b)


try:
    a = int(input("Enter the number "))
    b = int(input("Enter the number "))
    remainder(a, b)
except BaseException:
    print("somthing went wrong please enter the number only ")
