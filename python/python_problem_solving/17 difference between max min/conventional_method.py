def Difference(lis):
    large = lis[0]
    small = lis[0]
    for i in range(len(lis)):
        if small>lis[i]:
            small = lis[i]
    for i in range(len(lis)):
        if large<lis[i]:
            large = lis[i]
    print("diffrence between Number is : ",large-small)
try:
    lis = list(map(int,input("Enter the numbers : ").split()))
    Difference(lis)
except BaseException:
    print("somthing went wrong please enter the integer number only")