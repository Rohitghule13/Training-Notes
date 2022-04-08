try:
    
    lis1 = list(map(int, input("Enter First List : ").split())) # getting 1 integer from console
    lis2 = list(map(int, input("Enter First List : ").split())) # getting 2 integer from console
    lis1.extend(lis2)    # using inbulit function concate two list
    print("Concatenate List : ",lis1)   # print concate list

except BaseException:    # exception is used for if input get string rather than integer so value error is occure so 
    # exception handlling there to handle exception

    print("somthing went wrong please enter number in integer only")
