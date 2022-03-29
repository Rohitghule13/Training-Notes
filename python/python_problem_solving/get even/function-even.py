def checkEven(a):
    if a%2==0:
        return True
    return False
try:
    a = int(input("Enter the number : "))
    print(checkEven(a))
except BaseException:
    print("somthing went wrong please enter the number in integer")