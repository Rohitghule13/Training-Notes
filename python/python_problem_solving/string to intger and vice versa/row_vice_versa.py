try:
    st = input("Enter the string 0-9 : ")
    print("this is in integer number : ",int(st))
    print("this is in integer number : ",str(st))
except BaseException:
    print("somthing went wrong please enter the string in 0-9")