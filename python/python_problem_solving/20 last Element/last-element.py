try:
    lis = list(map(int,input("enter the number : ").split()))
    le = len(lis)-1
    print("this is last element of list : ",lis[le])
except BaseException:
    print("somthing went wrong please enter numbe only 0-9")