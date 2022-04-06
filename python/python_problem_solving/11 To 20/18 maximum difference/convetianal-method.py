def Difference(lis):
    large = lis[0]
    small = lis[0]
    for i in range(1,len(lis)):
        if large<lis[i]:
            large = lis[i]
    for i in range(1,len(lis)):
        if small>lis[i]:
            small = lis[i]
    print("Diffrence Between smallest and largest Number : ",large-small)
    return 
    
try:
    lis = list(map(int,input("Enter the numbers : ").split()))
    Difference(lis)
except BaseException:
    print("somthing went wrong please enter the integer number only")