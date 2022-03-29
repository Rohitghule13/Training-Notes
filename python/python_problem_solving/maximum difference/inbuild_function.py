def diffrence(lis):
    print("Diffrence Between smallest and largest Number : ",max(lis)-min(lis))
    return
try:
    lis = list(map(int,input("Enter the numbers : ").split()))
    diffrence(lis)
except BaseException:
    print("somthing went wrong please enter the integer number only")