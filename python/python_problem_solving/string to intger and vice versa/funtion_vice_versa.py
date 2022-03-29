from string import ascii_letters


def convert(st):
    print("this is in integer number : ",int(st))
    print("this is in string number : ",str(st))
    return 
try:
    st = input("Enter the string in 0-9 : ")
    convert(st)
except BaseException:
    print("somthing went wrong Enter the string only in 0-9 format ")