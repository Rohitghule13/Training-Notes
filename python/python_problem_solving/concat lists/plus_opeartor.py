try:
    lis1 = list(map(int, input("Enter First List : ").split()))
    lis2 = list(map(int, input("Enter First List : ").split()))
    lis1 += lis2
    print("Concatenate List : ",lis1)
except BaseException:
    print("somthing went wrong please enter number in integer only")
