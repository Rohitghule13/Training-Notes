def integer_to_string(a):
    print(str(a))

try:
    a = int(input("enter the number "))
    integer_to_string(a)
except BaseException:
    print("somthing went wrong please enter the number only")