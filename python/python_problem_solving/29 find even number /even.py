try:
    number = int(input("Enter the number : "))
    print("Even Number : ",end="")
    for i in range(number):
        if i%2==0:
            print(i,end=",")
    print()
except BaseException:
    print("somthing went wrong please enter the number in integer only")