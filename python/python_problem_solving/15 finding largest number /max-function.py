def largestNumber(lis):
    print("largest Number : ", max(lis))
try:
    lis = list(map(int,input("Enter the numbers : ").split()))
    largestNumber(lis)
except BaseException:
    print("somthing went wrong please enter the integer number only")