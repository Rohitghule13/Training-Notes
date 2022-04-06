from email.mime import base


def summing(lis):
    print("summing : ",sum(lis))
    return
try:
    lis = list(map(int,input("Enter the element : ").split()))
    summing(lis)
except BaseException:
    print("somthing went wrong enter the integer number only")