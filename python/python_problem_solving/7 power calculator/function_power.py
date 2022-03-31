def power(a,b):
    print("result : ",a**b)
try:
    a = int(input("enter the number : "))
    b = int(input("enter the power : "))
    power(a,b)
except BaseException:
    print("somthing went wrong please enter the number in intger ")