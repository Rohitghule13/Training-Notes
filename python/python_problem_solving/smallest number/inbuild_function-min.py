def smallestNumber(lis):
    print("smallest Number : ",min(lis))
try:
    lis = list(map(int,input("Enter the numbers : ").split()))
    smallestNumber(lis)
except BaseException:
    print("somthing went wrong please enter the integer number only")