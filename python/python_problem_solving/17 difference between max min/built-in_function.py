def Difference(lis):
    print("diffrence between Number is : ",max(lis)-min(lis))
try:
    lis = list(map(int,input("Enter the numbers : ").split()))
    Difference(lis)
except BaseException:
    print("somthing went wrong please enter the integer number only")