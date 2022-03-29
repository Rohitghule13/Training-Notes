try:
    lis = list(map(int,input("Enter the number : ").split()))
    add = 0
    for i in range(len(lis)):
        add += lis[i]
    print("summing : ",add)
except BaseException:
    print("somthing went wrong enter number only")