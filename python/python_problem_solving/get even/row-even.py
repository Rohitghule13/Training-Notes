try:
    a = int(input("Enter the number : "))
    if a%2==0:
        print("Even")
    else:
        print("Odd")
except BaseException:
    print("somthing went wrong please enter the number in integer")