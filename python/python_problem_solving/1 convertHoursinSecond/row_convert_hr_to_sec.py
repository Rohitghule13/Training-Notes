try:
    x = int(input("Enter the hours in number "))
    minutes = x*60
    second = minutes*60
    print(second)
except BaseException:
    print("somthing went wrong please enter the hours in number only")