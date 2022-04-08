try:
    
    lis1 = list(map(int, input("Enter First List : ").split()))
    lis2 = list(map(int, input("Enter Second List : ").split()))
    lis1 += lis2
    print("Concatenate List : ",lis1) # plue operator is used for concat list

except BaseException: # if there input from console get string so
    # value error is occured to handle that exception is there 

    print("somthing went wrong please enter number in integer only")
