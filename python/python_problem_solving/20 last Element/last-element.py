try:
    lis = list(map(int,input("enter the number : ").split()))
    print("this is last element of list : ",lis[-1])
except BaseException:
    print("somthing went wrong please enter numbe only 0-9")