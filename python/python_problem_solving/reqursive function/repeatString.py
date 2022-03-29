def repeat(string,a):
    if a==0:
        return 1
    else:
        print(string)
        return repeat(string,a-1)
try:
    string = input("Enter the string : ")
    a = int(input("Enter repeat number : "))
    repeat(string,a)
except BaseException as e:
    print("somthing went wrong please enter as mentioned : error : ",e)