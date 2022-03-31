def smallestNumber(lis):
    large = lis[0]
    for i in range(len(lis)):
        if large>lis[i]:
            large = lis[i]
    print("smallest Number is : ",large)
try:
    lis = list(map(int,input("Enter the numbers : ").split()))
    smallestNumber(lis)
except BaseException:
    print("somthing went wrong please enter the integer number only")